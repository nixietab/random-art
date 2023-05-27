from PIL import Image, ImageDraw
import random
import os

ORIGINAL_SIZE = (32, 32)
UPSCALE_SIZE = (256, 256)
BACKGROUND_COLOR = (0, 0, 0)
OUTPUT_DIRECTORY = "gen.images"
IMAGE_NAME = "image.png"

def generate_gen_image():
    original_image = Image.new("RGB", ORIGINAL_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(original_image)

    num_shapes = random.randint(3, 10)
    for _ in range(num_shapes):
        shape_type = random.choice(["circle", "rectangle", "triangle"])
        shape_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if shape_type == "circle":
            draw_circle(draw, shape_color)
        elif shape_type == "rectangle":
            draw_rectangle(draw, shape_color)
        else:
            draw_triangle(draw, shape_color)
    upscaled_image = original_image.resize(UPSCALE_SIZE, resample=Image.NEAREST)
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    image_path = os.path.join(OUTPUT_DIRECTORY, IMAGE_NAME)
    counter = 1
    while os.path.exists(image_path):
        image_name, image_ext = os.path.splitext(IMAGE_NAME)
        image_name = f"{image_name}_{counter}"
        image_path = os.path.join(OUTPUT_DIRECTORY, f"{image_name}{image_ext}")
        counter += 1

    # Save the image as a PNG file
    upscaled_image.save(image_path, "PNG")
    print(f"Image Generated!: {image_path}")


def draw_circle(draw, color):
    x = random.randint(1, ORIGINAL_SIZE[0] - 1)
    y = random.randint(1, ORIGINAL_SIZE[1] - 1)
    radius = random.randint(1, 3)
    draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=color)


def draw_rectangle(draw, color):
    x1 = random.randint(1, ORIGINAL_SIZE[0] - 2)
    y1 = random.randint(1, ORIGINAL_SIZE[1] - 2)
    x2 = random.randint(x1 + 1, ORIGINAL_SIZE[0] - 1)
    y2 = random.randint(y1 + 1, ORIGINAL_SIZE[1] - 1)
    draw.rectangle([(x1, y1), (x2, y2)], fill=color)


def draw_triangle(draw, color):
    x1 = random.randint(1, ORIGINAL_SIZE[0] - 1)
    y1 = random.randint(1, ORIGINAL_SIZE[1] - 1)
    x2 = random.randint(1, ORIGINAL_SIZE[0] - 1)
    y2 = random.randint(1, ORIGINAL_SIZE[1] - 1)
    x3 = random.randint(1, ORIGINAL_SIZE[0] - 1)
    y3 = random.randint(1, ORIGINAL_SIZE[1] - 1)

    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=color)

generate_gen_image()
