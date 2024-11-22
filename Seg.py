import pygame
import math

FINAL_POINT_RAD = 5
COLORS = True

def give_color(multiplier, offset, color_value):
    return math.floor((math.sin(color_value * multiplier + offset) + 1) / 2 * 255)

# figuring the new point placement
def rotate_by_center(center, point, rad):
    dx = point[0] - center[0]
    dy = point[1] - center[1]

    newX = (math.cos(rad) * dx - math.sin(rad) * dy) + center[0]
    newY = (math.sin(rad) * dx + math.cos(rad) * dy) + center[1]

    return [newX, newY]

# the class used for drawing each segment
class Seg:
    # holding the lines list as following
    # [(x, y), (x, y), ...] in a way that the lines will form from one point to another
    lines = []
    rotation = None

    def __init__(self,rotation , lines=None):
        if lines is None:
            lines = []

        self.lines = lines
        self.rotation = rotation

    def draw(self, WINDOW):
        for i in range(len(self.lines)):
            if i + 1 == len(self.lines):
                x = self.lines[i][0]
                y = self.lines[i][1]

                pygame.draw.circle(WINDOW, (190, 120, 120, 255), (x, y), FINAL_POINT_RAD)

                break

            # Feel free to mess with these colors!
            # Some really interesting results can be generated.
            pygame.draw.line(WINDOW,(give_color(0.0001,0, i)/3 + 60,
                                    give_color(0.0002, 10, i)/2 + 50,
                                    give_color(0.0003, 40, i)) 
                            if COLORS else (255,255,255,255),
                            self.lines[i], self.lines[i + 1])

    def rotate(self):
        # selecting the last point and the new array
        last_circle = self.lines[-1]
        copy = self.lines.copy()
        copy.reverse()

        # going through the lines in reverse
        for (i, point) in enumerate(copy):
            if i == 0:
                continue

            self.lines.append(rotate_by_center(last_circle, point, -self.rotation))