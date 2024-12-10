from PIL import Image, ImageDraw, ImageFont


class TextToBook:
    def __init__(self, image_path, text_file_path, font_path, font_size=20):
        self.image_path = image_path
        self.text_file_path = text_file_path
        self.font_path = font_path
        self.font_size = font_size
        self.img = self.open_image()
        self.font = self.load_font()
        self.text = self.read_text_file()

    def open_image(self):
        return Image.open(self.image_path)

    def load_font(self):
        return ImageFont.truetype(self.font_path, self.font_size)

    def read_text_file(self):
        with open(self.text_file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def draw_text_on_image(self):
        draw = ImageDraw.Draw(self.img)
        text_position = (10, 10)
        line_spacing = 5
        max_width = self.img.width - 20
        current_height = text_position[1]
        lines = []

        # split text into lines that fit image width
        for line in self.text.split('\n'):
            words = line.split(' ')
            current_line = ""
            for word in words:
                test_line = current_line + word + " "
                width = draw.textbbox((0, 0), test_line, font=self.font)[2]
                if width <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line.strip())
                    current_line = word + " "
            lines.append(current_line.strip())

        # draw lines on image, extend page if necessary
        while lines:
            for line in lines[:]:
                if current_height + self.font.size + line_spacing > self.img.height - 20:
                    self.img = self.extend_image()
                    draw = ImageDraw.Draw(self.img)
                    current_height += 40  # add padding at start of extended page

                draw.text((text_position[0], current_height), line, font=self.font, fill="black")
                current_height += self.font.size + line_spacing
                lines.pop(0)

        return self.img

    def extend_image(self):
        new_height = self.img.height + self.img.height // 2
        new_img = Image.new('RGB', (self.img.width, new_height))
        new_img.paste(self.img, (0, 0))

        original_img = Image.open(self.image_path)
        original_img = original_img.resize((self.img.width, self.img.height))

        for i in range(self.img.height, new_height, self.img.height):
            paste_height = min(original_img.height, new_height - i)
            cropped_original = original_img.crop((0, 0, original_img.width, paste_height))
            new_img.paste(cropped_original, (0, i))

        return new_img

    def add_text_to_image(self):
        self.img = self.draw_text_on_image()

    def show(self):
        self.img.show()
