# C
import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

ENTITY_HEALTH = {'LEVEL1Bg0': 999,
                 'LEVEL1Bg1': 999,
                 'LEVEL1Bg2': 999,
                 'LEVEL1Bg3': 999,
                 'LEVEL1Bg4': 999,
                 'LEVEL1Bg5': 999,
                 'LEVEL1Bg6': 999,
                 'LEVEL2Bg0': 999,
                 'LEVEL2Bg1': 999,
                 'LEVEL2Bg2': 999,
                 'LEVEL2Bg3': 999,
                 'LEVEL2Bg4': 999,
                 'LEVEL2Bg5': 999,
                 'LEVEL2Bg6': 999,
                 'player1': 300,
                 'Player1Shot': 1,
                 'player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 50,
                 'Enemy1Shot': 1,
                 'Enemy2': 60,
                 'Enemy2Shot': 1,}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 3P - COMPETITIVE',
               'SCORE',
               'EXIT')
# p
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w,
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s,
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a,
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d,
}

PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_RCTRL,
    'Player2': pygame.K_LCTRL,
}

# S
SPAWM_TIME = 4000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
