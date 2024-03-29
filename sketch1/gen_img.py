from typing import Callable
from PIL import Image
from random import randint

IMG_HEIGHT = 256

# borrowed from
# https://stackoverflow.com/a/58382956
def gen_rand(x: int, y: int) -> tuple[int, int, int]:
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )

def gen_pixel_rainbow(x: int, y: int) -> tuple[int, int, int]:
    p = (x % 255,
         y % 255,
         (x**2-y**2) % 255)
    return p

def generate_img(width: int,
                 pgen:Callable[[int, int], tuple[int,int,int]],
                 path: str):
    img = Image.new('RGB', (width, IMG_HEIGHT), 255)
    data = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            data[x,y] = pgen(x, y)

    img.save(path)

reds = ([(180, i) for i in range(0, 200)] +
        [(160, i) for i in range(200, 400)] +
        [(165, i) for i in range(400, 2000)])

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

def gen_three_stripe(x: int, y: int) -> tuple[int, int, int]:
    r, g, b = 0, 0, 0
    if (y, x) in reds:
    # if y == 180 or y == 186: # or y == 205:
        r = 255
        g = 255
        b = 0
    return (r, g, b)


def main():
    generate_img(256, gen_pixel_rainbow, "test_img1.png")
    generate_img(1000, lambda x, y: (100, 200, 50), "test_img2.png")
    generate_img(2000, gen_pixel_rainbow, "test_img3.png")
    generate_img(2000, gen_rand, "rand_img.png")
    generate_img(2000, gen_tri_grad, "tri_grad.png")
    generate_img(2000, gen_horiz, "grad.png")
    generate_img(2000, mid_stripe, "stripe_grad.png")
    generate_img(2000, gen_three_stripe, "three_stripe.png")
    return

if __name__ == "__main__":
    main()
