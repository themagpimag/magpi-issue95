from PIL import Image
from inky import InkyWHAT

inky_display=InkyWHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.open("MagPi-Logo.png")
inky_display.set_image(img)
inky_display.show()
