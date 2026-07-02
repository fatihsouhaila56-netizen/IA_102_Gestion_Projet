import tkinter as tk
import math


def pentagram_points(cx, cy, outer_radius, inner_radius, rotation=0):
    points = []
    angle = math.radians(rotation)
    for i in range(10):
        r = outer_radius if i % 2 == 0 else inner_radius
        a = angle + i * math.pi / 5.0  # 36 degrees step
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        points.append((x, y))
    # Reorder points to create a continuous star (pentagram) path
    order = [0, 2, 4, 1, 3]
    path = []
    for idx in order:
        path.append(points[idx * 2])
        path.append(points[idx * 2 + 1])
    return path


def draw_moroccan_flag(width=900, height=600):
    root = tk.Tk()
    root.title('Moroccan Flag')
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # Red background
    canvas.create_rectangle(0, 0, width, height, fill='#C1272D', width=0)

    # Star (green pentagram) centered
    cx, cy = width // 2, height // 2
    outer = min(width, height) * 0.18
    inner = outer * 0.45
    pts = pentagram_points(cx, cy, outer, inner, rotation=-90)
    flat = [coord for point in pts for coord in point]
    canvas.create_polygon(flat, fill='#006233', outline='#006233')

    root.mainloop()


if __name__ == '__main__':
    draw_moroccan_flag()
