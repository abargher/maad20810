from typing import Callable
from PIL import Image

IMG_HEIGHT = 256

# borrowed from
# https://stackoverflow.com/a/58382956
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

def main():
    generate_img(256, gen_pixel_rainbow, "test_img1.png")
    generate_img(1000, lambda x, y: (100, 200, 50), "test_img2.png")
    generate_img(2000, gen_pixel_rainbow, "test_img3.png")
    return

if __name__ == "__main__":
    main()
