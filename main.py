import pygame, sys

from pygame.locals import *

black = (0, 0, 0)
brown = (153, 76, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (105, 105, 105)

dirt = 0
grass = 1
water = 2
coal = 3
rock = 4
lava = 5
'''
textures = {
    dirt : pygame.image.load('src/textures/dirt.jpg'),
    grass : pygame.image.load('src/textures/grass.png'),
    water : pygame.image.load('src/textures/water.jpg'),
    coal : pygame.image.load('src/textures/coal.jpg'),
    rock : pygame.image.load('src/textures/rock.jpg'),
    lava : pygame.image.load('src/textures/lava.jpg')
}'''

colors = {
    blue : (0, 0, 255),
    green : (0, 255, 0)
}

tilemap = [
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],
    [blue, blue, green, green, blue, blue, blue, blue, green, green, blue, blue, blue, blue, blue],

]

tilesize = 40
mapwidth = 15
mapheight = 20


pygame.init()
dispalySurf = pygame.display.set_mode((mapwidth*tilesize,mapheight*tilesize))

pygame.display.set_caption('RPG')

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    for row in range(mapheight):
        for column in range(mapwidth):
            pygame.draw.rect(dispalySurf,
                             colors[tilemap[row][column]],
                             (column*tilesize,
                              row*tilesize,
                              tilesize,
                              tilesize))

    pygame.display.update()