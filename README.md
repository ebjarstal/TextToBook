# Text to Book

Text to Book is a Python application that converts a text file into a stylized image resembling a book page. The program uses a GUI to enable users to customize the input and view the output easily. This is ideal for generating visual representations of text overlaid on book textures.

## Features

- Converts text files into images styled as book pages.
- Automatically adjusts text wrapping to fit the image dimensions.
- Extends the image dynamically to fit longer texts.
- User-friendly GUI for selecting text files, book textures, and font files.
- Preview the final image in real time.

## Installation

### Prerequisites
Ensure you have the following installed:

- Python 3.8 or later
- Required Python libraries:
  - `Pillow`
  - `tkinter` (comes with most Python installations)

### Setup
1. Clone or download this repository.
2. Install the required libraries using pip:
   ```bash
   pip install Pillow
   ```

## Usage

### Running the Application
1. Navigate to the directory where the files are located.
2. Run the application by executing:
   ```bash
   python main.py
   ```

### Using the GUI
1. **Book Texture Path**: Specify the path to an image file to be used as the background texture.
2. **Text File Path**: Select the text file containing the content to overlay on the book texture.
3. **Font Path**: Provide the path to a `.ttf` font file to customize the text appearance.
4. Click **Run** to generate the image and preview the result.

### Example
The GUI comes pre-filled with default paths for demonstration purposes. Ensure these files exist or replace them with your own:
- Example texture: `assets/book_texture_648_864.jpg`
- Example font: `assets/fonts/EBGaramond-VariableFont_wght.ttf`

## File Descriptions

### `main.py`
The entry point of the program. It initializes and runs the graphical user interface (GUI).

### `textToBook.py`
Contains the logic for processing the image and overlaying text:
- Opens the texture image.
- Reads the input text.
- Dynamically adjusts text wrapping and page extension.
- Outputs the final image.

### `textToBookGUI.py`
Defines the GUI for user interaction, allowing users to provide input paths and execute the text-to-book process visually.

## Future Improvements
- Add options for customizing text alignment and color.
- Save the generated images to a specified directory.
- Support for multiple pages or multi-image exports for long texts.

## License
This project is open-source and available under the MIT License.

## Acknowledgments
- [Pillow](https://pillow.readthedocs.io/) for image manipulation.
- Fonts and book textures sourced from publicly available resources.

