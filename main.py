import sys
import pygame
import math
from Seg import Seg

# setting up the display
SIZE = (700, 400)
STARTING_SIZE = 2
ROTATION = math.pi / 2
STARTING_SEG = [(SIZE[0] / 2, SIZE[1] / 2),
                (SIZE[0] / 2, SIZE[1] / 2 - STARTING_SIZE)]

print("HI Hi! ✨\nFeel free to change any of the above values.\n" +
"This would affect the starting state. What shape, which angle. (Even the color, from the 'Seg.py' file.)\n" +
"Tested with some stuff. not too different I would say, but hey, it's something.\n" +
"Feel free to make any changes or make it more interesting!")

pygame.init()
WINDOW = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Dragon Curve")

seg = Seg(ROTATION, STARTING_SEG)

for i in range(16):
    seg.rotate()

# main loop
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    WINDOW.fill((0, 0, 0, 0))

    seg.draw(WINDOW)

    pygame.display.update(0, 0, 700, 400)
