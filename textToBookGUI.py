import tkinter as tk
from tkinter import filedialog
from textToBook import TextToBook

class TextToBookApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text to Book")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Book Texture Path:").grid(row=0, column=0, padx=10, pady=5)
        self.img_entry = tk.Entry(self.window, width=50)
        self.img_entry.insert(0, "assets/book_texture_648_864.jpg")
        self.img_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.window, text="Browse", command=self.browse_img).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.window, text="Text File Path:").grid(row=1, column=0, padx=10, pady=5)
        self.text_entry = tk.Entry(self.window, width=50)
        self.text_entry.insert(0, "text.txt")
        self.text_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.window, text="Browse", command=self.browse_text).grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self.window, text="Font Path:").grid(row=2, column=0, padx=10, pady=5)
        self.font_entry = tk.Entry(self.window, width=50)
        self.font_entry.insert(0, "assets/fonts/EBGaramond-VariableFont_wght.ttf")
        self.font_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self.window, text="Browse", command=self.browse_font).grid(row=2, column=2, padx=10, pady=5)

        tk.Button(self.window, text="Run", command=self.run_text_to_book).grid(row=3, column=1, pady=20)

    def browse_file(self):
        return filedialog.askopenfilename()

    def browse_img(self):
        filename = self.browse_file()
        self.img_entry.delete(0, tk.END)
        self.img_entry.insert(0, filename)

    def browse_text(self):
        filename = self.browse_file()
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, filename)

    def browse_font(self):
        filename = self.browse_file()
        self.font_entry.delete(0, tk.END)
        self.font_entry.insert(0, filename)

    def run_text_to_book(self):
        img = self.img_entry.get()
        text = self.text_entry.get()
        font = self.font_entry.get()

        text_to_book = TextToBook(img, text, font)
        text_to_book.add_text_to_image()
        text_to_book.show()

    def run(self):
        self.window.mainloop()
