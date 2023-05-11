import pygame
import random
import math

# initialize pygame
pygame.init()

# set the screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# set the title of the window
pygame.display.set_caption("Colorful Animation")

# set the clock for the game
clock = pygame.time.Clock()

# define the colors
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# define the circles
circles = []
for i in range(10):
    radius = random.randint(10, 30)
    x = random.randint(radius, width - radius)
    y = random.randint(radius, height - radius)
    color = random.choice(colors)
    speed = random.randint(1, 5)
    direction = random.randint(0, 360)
    circle = {"x": x, "y": y, "radius": radius, "color": color, "speed": speed, "direction": direction}
    circles.append(circle)

# define the game loop
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the circles
    for circle in circles:
        radians = circle["direction"] * (3.14 / 180)
        x = circle["x"] + circle["speed"] * round(math.cos(radians))
        y = circle["y"] + circle["speed"] * round(math.sin(radians))
        if x > width - circle["radius"] or x < circle["radius"]:
            circle["direction"] = 180 - circle["direction"]
        elif y > height - circle["radius"] or y < circle["radius"]:
            circle["direction"] = -circle["direction"]
        circle["x"], circle["y"] = x, y

    # clear the screen
    screen.fill((255, 255, 255))

    # draw the circles
    for circle in circles:
        pygame.draw.circle(screen, circle["color"], (circle["x"], circle["y"]), circle["radius"])

    # update the display
    pygame.display.flip()

    # set the frame rate
    clock.tick(60)

# quit pygame
pygame.quit()



