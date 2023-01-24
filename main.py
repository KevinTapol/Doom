# On my python learning journey, I found a pygame tutorial in Pycharm IDE that had so many in depth concepts and math. It's a 52 minute video but I spent 5 days understanding and making it work in VSCode.

# I used ScreenToGif to record my gameplay of success and fail resets. The yellow circle is a representation of my mouse location on click seen through ScreenToGif.

# Doom Python Pygame in Pycharm IDE tutorial by Coder Space https://www.youtube.com/watch?v=ECqUrT7IdqQ&t=133s


# Thank you to Coder Space for this tutorial youtube link. https://www.youtube.com/watch?v=ECqUrT7IdqQ&t=133s
# There are so many concepts and math in this tutorial that I had to watch several times over to understand. For example the concept and math of raycasting for field of vision. The idea here is they took a 2d grid map and converted it into 3d draw of the players location in the grid. I commented out the code 

# The tutorial uses pycharm. To get this to work in VSCode, I converted the mp3 files into wav files. 
# In sound.py change the class sound and change the file path of your new theme.wav file to self.theme. I used self.theme = pg.mixer.Sound(self.path + 'theme (1).wav') 
# Then go to main.py and comment out pg.mixer.music.play(-1) and replace it with self.sound.theme.play(-1)
# Finally go to player.py import sound at top by typing from sound import * and add the line self.game.sound.theme.stop() under the function check_game_over if conditional of player health < 1. This will stop the theme sound when the player dies.

# Enable God mode or don't take damage by commenting out self.health -= damage in the player.py function get_damage

# I tried to use pip install playsound both current version and the pip install playsound==1.2.2 command for 1.2.2 but I couldn't get it running.
# from playsound import playsound
# playsound('filepath')
# filepath = C:\\Users\\theme.mp3
# filepath = resources/sound/theme.mp3
# pygame.mixer.music.load(filepath)
import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

# constructor class
class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False) # hide mouse cursor
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()
        self.pathfinding = Pathfinding(self)
        
    # create instance of class
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        # self.static_sprite = SpriteObject(self)
        # self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        print(self.clock.get_time()) # printing out to the console the current time curious about death new game tracking
        self.sound.theme.play(-1).set_volume(0.4) # value -1 loops the sound indefinitely .set_volume() Return a value from 0.0 to 1.0 representing the volume for this Sound.

    def update(self):
        self.player.update()
        self.raycasting.update()
        # self.static_sprite.update()
        # self.animated_sprite.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
        # 2d mode comment out above and uncomment below Also go to npc.py and uncomment line 30 self.draw_ray_cast() to see the enemies as red circles and their line of sight of player
        # self.screen.fill('black') # fill ceiling and floor black
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

# create instance of the game and run it
if __name__ == '__main__':
    game = Game()
    game.run()