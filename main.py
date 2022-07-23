import pygame
from pygame.locals import *
from constants import *
from event import HandleEvent
from utils.vector import Vector3
from utils.camera import Camera
from utils.light import Light
from utils.mesh.base import Mesh
from utils.mesh.point import *
from utils.matrix import *
from utils.tools import *
from utils.world import Scene

pygame.init()
screen = pygame.display.set_mode(Size)
clock = pygame.time.Clock()
fps = 120

#mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)

#create mesh
stadium = Mesh() 
stadium.triangles = LoadMesh("stadium.obj", (153, 255, 51)) #Triangles and Color of Object

# create scene and the world
scene = Scene()

#add object you want to display into the world
scene.world.append(stadium)

#camera setup
camera = Camera(Vector3(0, 100, -350), 0.1, 1000.0, 45.0) #Camera Position, Near, Far, Field of View

#light setup
light = Light(Vector3(800,800,-800))
angle = 0
moveLight = True

run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps" + str(camera.position))
    run = HandleEvent(camera, dt)
    # handle input
    camera.HandleInput(dt)

    if moveLight == True and light != None:
        mx, my = pygame.mouse.get_pos()
        _x = translateValue( mx, 0,  Width,  -1,  1)
        _y = translateValue( my, 0, Height, -1, 1)
        light = Light(Vector3(-_x,- _y, -1))

    
    # display scene
    scene.update(
        dt = dt,
        camera=camera,
        light=light,
        screen=screen,
        fill=True, #Fills the object when True
        wireframe=True, #Draws wireframe model of the Poject When True
        vertices=False, #Shows Vertices of the Object When True
        depth=True, #for Painter's Algorithm
        showNormals=False, #Shows Normal of Each Face
        radius=2,
        verticeColor=True,
        wireframeColor=(0, 0, 0))

    pygame.display.flip() #For refresh
    angle -= 0.1
    #stadium.transform = Matrix.rotation_x(angle)
    stadium.transform = Matrix.rotation_y(angle)
    #stadium.transform = Matrix.rotation_z(angle)

pygame.quit()