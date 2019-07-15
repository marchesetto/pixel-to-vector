from PIL import Image as img
from sys import argv


path = argv[1]
try:
  image = img.open(path, "r")
except:
  print("Image might be missing or in an unknown format")
  quit()
squares_list = []
for a in range(image.height):
  for b in range(image.width):
    c = image.getpixel((a, b))
    color = "{0}, {1}, {2}".format(c[0], c[1], c[2])
    opacity = "{0}".format(c[3] / 255)
    rect = "  <rect\n   x=\"{0}\"\n   y=\"{1}\"\n   height=\"1\"\n   width=\"1\"\n   style=\"fill:rgb({2});fill-opacity:{3};stroke:none\"\n   id=\"{0}{1}\"\n  />".format(a, b, color, opacity)
    squares_list.append("\n{0}".format(rect))
squares = ""
for a in squares_list:
  squares += a
vector = "<svg\n width=\"{0}\"\n height=\"{1}\"\n viewBox=\"0 0 {0} {1}\"\n>\n <g>{2}\n </g>\n</svg>".format(image.width, image.height, squares)
file = open(path + ".svg", "w")
file.write(vector)
file.close()
