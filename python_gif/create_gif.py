from PIL import Image, ImageDraw, ImageFont

def create_frame(text, opacity):
    """Create a single frame with given text and opacity."""
    width, height = 200, 100
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype("arial.ttf", 36)

    # Calculate text size and position using textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) / 2, (height - text_height) / 2)

    # Draw the text
    draw.text(position, text, fill=(0, 0, 0, opacity), font=font)

    return image

def create_gif(filename):
    """Create an animated GIF with fading text."""
    frames = []
    text = "Hello, World!"

    # Create frames with varying opacity
    for opacity in range(0, 256, 10):
        frame = create_frame(text, opacity)
        frames.append(frame)

    for opacity in range(255, -1, -10):
        frame = create_frame(text, opacity)
        frames.append(frame)

    # Save the frames as an animated GIF
    frames[0].save(filename, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

# Create the GIF
create_gif("animated_text.gif")
