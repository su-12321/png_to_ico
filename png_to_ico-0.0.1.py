from PIL import Image as img

a = ""


def to(a: str, b: str):
    image = img.open(a)
    image.save(b, format="ICO")
    print(f"已完成 位置：{a}")
