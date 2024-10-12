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

def main():
    # Define parameters
    output_path = 'created_image.jpg'
    text = input("Enter the text to be placed on the image: ")
    font_path = "Raleway-Regular.ttf"  # Path to a TTF font file
    font_size = int(input("Enter the font size: "))
    text_position_x = int(input("Enter the x-coordinate for the text position: "))
    text_position_y = int(input("Enter the y-coordinate for the text position: "))
    text_color_r = int(input("Enter the red component of the text color (0-255): "))
    text_color_g = int(input("Enter the green component of the text color (0-255): "))
    text_color_b = int(input("Enter the blue component of the text color (0-255): "))
    text_position = (text_position_x, text_position_y)
    text_color = (text_color_r, text_color_g, text_color_b)

    # Create the image with text
    create_image_with_text(output_path, text, font_path, font_size, text_position, text_color)

if __name__ == "__main__":
    main()