import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(output_path, text, font_path, font_size, text_position, text_color):
    # Create a blank image with white background
    width, height = 1080, 1080
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Add text to the image
    draw.text(text_position, text, font=font, fill=text_color)

    # Save the edited image
    image.save(output_path)
    print(f"Image saved to {output_path}")

def add_text():
    text = text_entry.get("1.0", tk.END).strip()
    font_size = int(font_size_entry.get())
    text_position_x = int(text_position_x_entry.get())
    text_position_y = int(text_position_y_entry.get())
    text_color = colorchooser.askcolor(title="Choose text color")[1]
    text_color_rgb = tuple(int(text_color[i:i+2], 16) for i in (1, 3, 5))

    text_position = (text_position_x, text_position_y)
    output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    font_path = "Raleway-Regular.ttf"  # Path to the Raleway TTF font file

    create_image_with_text(output_path, text, font_path, font_size, text_position, text_color_rgb)

# Create the main window
root = tk.Tk()
root.title("Image Text Editor")

# Create and place the widgets
tk.Label(root, text="Enter the text to be placed on the image:").pack()
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

tk.Label(root, text="Enter the font size:").pack()
font_size_entry = tk.Entry(root)
font_size_entry.pack()

tk.Label(root, text="Enter the x-coordinate for the text position:").pack()
text_position_x_entry = tk.Entry(root)
text_position_x_entry.pack()

tk.Label(root, text="Enter the y-coordinate for the text position:").pack()
text_position_y_entry = tk.Entry(root)
text_position_y_entry.pack()

tk.Button(root, text="Choose Text Color", command=lambda: colorchooser.askcolor(title="Choose text color")).pack()
tk.Button(root, text="Add Text to Image", command=add_text).pack()

# Run the main loop
root.mainloop()