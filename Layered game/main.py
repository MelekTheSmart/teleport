#Import statements are to enable the code to use the functions from the library
import pygame
import sys
import os
import pytmx


throg = 1
key_pickup = throg
cycle_key = 1
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
teleport = tiled_map.get_layer_by_name('collision')
MOVEMENTSPEED = 5
COOLDOWN = 100
can_teleport = COOLDOWN
key_pickup = 1
TELEPORTDIST = 192
objects = tiled_map.get_layer_by_name('objectLayers')
DoorsToDisable = 0
keyDoor = []
for object in objects:
    if object.type == "Key":
        keyDoor.append(object)
doorDoors = tiled_map.get_layer_by_name('placeholder')



tiles = []
for x, y, tile in collision.tiles():
        if (tile):
             tiles.append(pygame.Rect([(x*tilewidth), (y*tileheight), tilewidth, tileheight]));
spaces = []
for x, y, space in teleport.tiles():
        if (space):
             spaces.append(pygame.Rect([(x*tilewidth), (y*tileheight), tilewidth, tileheight]));
CAMERA = tiled_map.get_object_by_name("player")
#caption for the game
pygame.display.set_caption("My first game in pygame")
player = pygame.image.load(os.path.join("../Sprites/crown Guy/cguyfront.png")).convert_alpha() # load in coin image, convert_alpha will keep transparent background
# player = pygame.transform.scale(player, (64, 64)) # resize player image, this should be the same size as the map object
key = pygame.image.load(os.path.join("../Sprites/Objects/Key.png")).convert_alpha(); # load in coin image, convert_alpha will keep transparent background
# key = pygame.transform.scale(key, (16, 16)) # resize coin image
door_img = pygame.image.load(os.path.join("../Sprites/doortile.png")).convert_alpha()
def checkkey(playerrec):
    for item in keyDoor:
        itemrec = pygame.Rect([item.x, item.y, item.width, item.height])
        if (itemrec.colliderect(playerrec) and (item.visible!=0)):
            item.visible = 0
def checkkey(playerrec):
    for item in keyDoor:
        itemrec = pygame.Rect([item.x, item.y, item.width, item.height])
        if (itemrec.colliderect(playerrec) and (item.visible!=0) and (item.type=="Key")):
            item.visible = 0
#game loop
while True:
    for events in pygame.event.get(): #get all pygame events
        if events.type == pygame.QUIT: #if event is quit then shutdown window and program
            pygame.quit()
            sys.exit()
    if cycle_key == 1:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-1.png")).convert_alpha();
    elif cycle_key == 2:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-2.png")).convert_alpha();
    elif cycle_key == 3:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-3.png")).convert_alpha();
    elif cycle_key == 4:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-4.png")).convert_alpha();
    elif cycle_key == 5:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-5.png")).convert_alpha();
    elif cycle_key == 6:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-6.png")).convert_alpha();
    elif cycle_key == 7:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-7.png")).convert_alpha();
    elif cycle_key == 8:
             key = pygame.image.load(os.path.join("../Sprites/Objects/keyframes/Key-8.png")).convert_alpha();
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
                elif (object.type == "Key" and key_pickup == 1):
                    SCREEN.blit(key,
                                [object.x - CAMERA.x + (SCREENWIDTH / 2),cycle_key + object.y - CAMERA.y + (SCREENHEIGHT / 2)])
                elif (object.type == "door" and doorDoors.visible == 1 ):
                    SCREEN.blit(door_img,
                                [object.x - CAMERA.x + (SCREENWIDTH / 2),
                                 object.y - CAMERA.y + (SCREENHEIGHT / 2)])

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
        if playerrec.collidelistall(spaces):
            pos[1] = 100
            pos[0] = 502.00
        # check key with the current position of the player
        checkkey(pygame.Rect([tiled_map.get_object_by_name("player").x, tiled_map.get_object_by_name("player").y,
                              tiled_map.get_object_by_name("player").width,
                              tiled_map.get_object_by_name("player").height]))
        def checkkey(playerrec):
            for item in keyDoor:
                itemrec = pygame.Rect([item.x, item.y, item.width, item.height])
                if (itemrec.colliderect(playerrec) and ( key_pickup == 1 ) and (item.type == "Key")):
                    throg = 0
                    DoorsToDisable = item.open
                    # Code to get the position of the door and create a rectangle
                    for door in doorDoors:
                        if door.open == DoorsToDisable:
                            doorrec = pygame.Rect([door.x, door.y, door.width, door.height])
                            tilestodelete = []  # will add tiles to remove to this list
                            for tile in tiles:
                                # create rectangle for tile, if it collides with player add this tile to the remove list
                                tilerec = pygame.Rect([tile.x, tile.y, tile.width, tile.height])
                                if (doorrec.colliderect(tilerec)):
                                    tilestodelete.append(tile)
                            # for loop to remove each tile in the remove list
                            for tile in tilestodelete:
                                tiles.remove(tile)
                            doorDoors.visible = 0

        if (checkbounds(playerrec)):
            pos = [0, 0]
            me = 1
        tiled_map.get_object_by_name("player").x += pos[0]
        tiled_map.get_object_by_name("player").y += pos[1]
        if can_teleport > 0:
            can_teleport -= 5
        pygame.display.update()
