#Import statements are to enable the code to use the functions from the library
import pygame
import sys
import os
import pytmx
#initialize pygame & window
from pytmx.util_pygame import load_pygame
def checkbounds(playerrec):
    check = False
    if (playerrec.collidelistall(tiles)): #this tests every tile with the player rectangle
        check = True
    return check
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
SCREENWIDTH = 1900
SCREENHEIGHT = 1000
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)
tiled_map = load_pygame('../maps/map01.tmx')
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight
collision = tiled_map.get_layer_by_name('collision')
MOVEMENTSPEED = 5
COOLDOWN = 100
can_teleport = COOLDOWN
TELEPORTDIST = 192
tiles = []
for x, y, tile in collision.tiles():
        if (tile):
             tiles.append(pygame.Rect([(x*tilewidth), (y*tileheight), tilewidth, tileheight]));
CAMERA = tiled_map.get_object_by_name("player")
#caption for the game
pygame.display.set_caption("My first game in pygame")
player = pygame.image.load(os.path.join("../Sprites/crown Guy/cguyfront.png")).convert_alpha() # load in coin image, convert_alpha will keep transparent background
# player = pygame.transform.scale(player, (64, 64)) # resize player image, this should be the same size as the map object
key = pygame.image.load(os.path.join("../Sprites/Objects/Key.png")).convert_alpha(); # load in coin image, convert_alpha will keep transparent background
# key = pygame.transform.scale(key, (16, 16)) # resize coin image

#game loop
while True:
    for events in pygame.event.get(): #get all pygame events
        if events.type == pygame.QUIT: #if event is quit then shutdown window and program
            pygame.quit()
            sys.exit()
    for layer in tiled_map.layers:
        if isinstance(layer, pytmx.TiledTileLayer): # and (layer != collision):
            for x, y, tile in layer.tiles():
                if (tile):
                    SCREEN.blit(tile, [(x * tilewidth) - CAMERA.x + (SCREENWIDTH / 2),
                                       (y * tileheight) - CAMERA.y + (SCREENHEIGHT / 2)])

        elif isinstance(layer, pytmx.TiledObjectGroup):
            for object in layer:

                if (object.name == 'player'):
                    SCREEN.blit(player,
                                [object.x - CAMERA.x + (SCREENWIDTH / 2) ,-25 + object.y - CAMERA.y + (SCREENHEIGHT / 2)])
                elif (object.type == "Key"):
                    SCREEN.blit(key,
                                [object.x - CAMERA.x + (SCREENWIDTH / 2), object.y - CAMERA.y + (SCREENHEIGHT / 2)])
        pos = [0, 0]
        for events in pygame.event.get():  # get all pygame events
            if events.type == pygame.QUIT:  # if event is quit then shutdown window and program
                pygame.quit()
                sys.exit()

        PRESSED = pygame.key.get_pressed()

        if PRESSED[pygame.K_a]:
            pos[0] -= MOVEMENTSPEED
        elif PRESSED[pygame.K_d]:
            pos[0] += MOVEMENTSPEED
        if PRESSED[pygame.K_w]:
            pos[1] -= MOVEMENTSPEED
        elif PRESSED[pygame.K_s]:
            pos[1] += MOVEMENTSPEED
        if PRESSED[pygame.K_RIGHT]:
            if can_teleport < 1:
                pos[0] += TELEPORTDIST
                can_teleport = COOLDOWN
        elif PRESSED[pygame.K_LEFT]:
            if can_teleport < 1:
                pos[0] -= TELEPORTDIST
                can_teleport = COOLDOWN
        if PRESSED[pygame.K_UP]:
            if can_teleport < 1:
                pos[1] =- TELEPORTDIST
                can_teleport = COOLDOWN
        elif PRESSED[pygame.K_DOWN]:
            if can_teleport < 1:
                pos[1] =+ TELEPORTDIST
                can_teleport = COOLDOWN

        x = tiled_map.get_object_by_name("player").x + pos[0]
        y = tiled_map.get_object_by_name("player").y + pos[1]
        w = tiled_map.get_object_by_name("player").width
        h = tiled_map.get_object_by_name("player").height

        playerrec = pygame.Rect([x, y, w, h])


        if (checkbounds(playerrec)):
            pos = [0, 0]
            me = 1
        tiled_map.get_object_by_name("player").x += pos[0]
        tiled_map.get_object_by_name("player").y += pos[1]
        if can_teleport > 0:
            can_teleport -= 5
        pygame.display.update()
