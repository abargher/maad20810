from typing import Callable
from PIL import Image
from random import randint

IMG_HEIGHT = 256

# This is the general purpose image generation function. It's unoptimized, but
# it simply iterates over the grid space and fills in every pixel value at each
# location using the provided pgen() function.
def generate_img(width: int,
                 pgen: Callable[[int, int], tuple[int,int,int]],
                 path: str):
    img = Image.new('RGB', (width, IMG_HEIGHT), 255)
    data = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            data[x,y] = pgen(x, y)

    img.save(path)

### Pixel gen functions

def gen_rand(x: int, y: int) -> tuple[int, int, int]:
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )

# borrowed from
# https://stackoverflow.com/a/58382956
def gen_pixel_rainbow(x: int, y: int) -> tuple[int, int, int]:
    p = (x % 255,
         y % 255,
         (x**2-y**2) % 255)
    return p


# These list comprehensions define every pixel that I want to fill in for the
# "three" stripe function.
filled = (
    [(180, i) for i in range(0, 200)] +

    [(160, i) for i in range(200, 400)] +
    [(170, i) for i in range(200, 400)] +
    [(90, i) for i in range(200, 400)] +

    [(165, i) for i in range(400, 600)] +

    [(175, i) for i in range(600, 800)] +

    [(170, i) for i in range(800, 1000)] +

    [(155, i) for i in range(1000, 1200)] +

    [(150, i) for i in range(1200, 1300)] +
    [(170, i) for i in range(1200, 1300)] +
    [(70, i) for i in range(1200, 1300)] +

    [(152, i) for i in range(1300, 1400)] +

    [(155, i) for i in range(1400, 1600)] +

    [(185, i) for i in range(1600, 1800)] +
    [(165, i) for i in range(1600, 1800)] +

    [(160, i) for i in range(1800, 2000)]
)

def mid_stripe(x: int, y: int) -> tuple[int, int, int]:
    r, g, b = 0, 0, 0
    if y == 200:
        r = 200
        g = 0
        b = 29
    return (r, g, b)

def gen_horiz(x: int, y: int) -> tuple[int, int, int]:
    return (
        x % 255,
        x % 255,
        x % 255
    )

def gen_tri_grad(x: int, y: int) -> tuple[int, int, int]:
    return (
        x % 255 - y,
        x % 255 - y,
        x % 255 - y
    )

# This function was what I used to generate most of my final images, including
# the "tornado siren" image mentioned in the blog post, as well as the "melody"
# image. Its name is not quite accurate anymore, but I originally used this one
# to generate a three note chord by placing a pixel at three different y values,
# as you can see in the commented out if-statement.
def gen_three_stripe(x: int, y: int) -> tuple[int, int, int]:
    r, g, b = 0, 0, 0
    if (y, x) in filled:
    # if y == 180 or y == 186: # or y == 205:
        r = 255
        g = 0
        b = 255
    return (r, g, b)


def main():
    # "rainbow" square like the stack overflow post
    generate_img(256, gen_pixel_rainbow, "test_img1.png")

    # Solid color rgb:(100,200,50)
    generate_img(1000, lambda x, y: (100, 200, 50), "test_img2.png")

    # rainbow square repeated to make a rectangle
    generate_img(2000, gen_pixel_rainbow, "test_img3.png")

    # Fully random color at every pixel
    generate_img(2000, gen_rand, "rand_img.png")

    # Triangular gradient, seen in blog post
    generate_img(2000, gen_tri_grad, "tri_grad.png")

    # Horizontal gradient
    generate_img(2000, gen_horiz, "grad.png")

    # solid middle stripe, not really a gradient
    generate_img(2000, mid_stripe, "stripe_grad.png")

    # "three" stripes, I modified this one repeatedly in my final experiments
    generate_img(2000, gen_three_stripe, "three_stripe.png")

if __name__ == "__main__":
    main()
