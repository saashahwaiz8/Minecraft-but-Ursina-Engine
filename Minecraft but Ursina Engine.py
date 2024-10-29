from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        sword.active()
    else:
        sword.passive()

class Voxel(Button):
    def __init__(self,position=(0,0,0)):
        super().__init__(
            parent = scene,
            color = color.white,
            highlight_color = color.lime,
            model = 'cube',
            collider = 'box',
            texture = 'my_grass',
            origin_y = 0.5,
            position=position
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)

for x in range(26):
    for z in range(26):
        voxel = Voxel(position=(x,0,z))

class Sword(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'blade',
            texture = 'sword',
            scale = (0.2,0.15),
            position = (0.5,-0.6),
            rotation = (30,-40)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)
        self.rotation = Vec2(30,-40)

    def passive(self):
        self.position = Vec2(0.5,-0.6)
        self.rotation = Vec2(30,-40)

player = FirstPersonController()
window.fullscreen = True
Sky(texture = 'sky_sunset')

sword = Sword()

player.position = Vec3(13,60,13)
app.run()
