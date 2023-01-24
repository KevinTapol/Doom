import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        # to load wav use .Sound()
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        # to load mp3 use music.load() doesn't work in vscode pip install playsound 1.2.2 is suggested but I'm still having trouble with it I converted the mp3 to a wav file instead
        self.theme = pg.mixer.Sound(self.path + 'theme (1).wav')
        # self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
