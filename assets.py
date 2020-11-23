# Importando Bibliotecas
import pygame
import os
from config import DIAMETER_COOKIE, DIAMETER_SNOWBALL

#Fundo e imagens do jogo
BACKGROUND = 'background'
SNOWBALL_IMG = 'snowball_img'
COOKIE_IMG = 'cookie_img'

#Imagens tela inicial
SANTALIGHT = 'santalight'
SANTAHAT = 'santahat'
SANTAFRONT = 'santafront'

#Fontes
INIT_FNT = 'init_fnt'
TITLE_FNT = 'title_fnt'
SCORE_FNT = 'score_fnt'
RECORD_FNT = 'record_fnt'
GAMEOVER_FNT = 'gameover_fnt'
RESULT_FNT = 'result_fnt'

#Sons
HOHOHO_SOUND = 'hohoho_sound'
DEATH_SOUND = 'death_sound'
JUMP_SOUND = 'jump_sound'
EAT_SOUND = 'eat_sound'

def load_assets():
    assets = {}

    #Fundo e imagens do jogo
    assets[SNOWBALL_IMG] = pygame.image.load(os.path.join('Assets','Images', 'SnowBall.png')).convert_alpha()
    assets[SNOWBALL_IMG] = pygame.transform.scale(assets['snowball_img'], (DIAMETER_SNOWBALL, DIAMETER_SNOWBALL))
    assets[COOKIE_IMG] = pygame.image.load(os.path.join('Assets','Images', 'Cookie.png')).convert_alpha()
    assets[COOKIE_IMG] = pygame.transform.scale(assets['cookie_img'], (DIAMETER_COOKIE, DIAMETER_COOKIE))

    #Imagens tela inicial
    assets[SANTALIGHT] = pygame.image.load(os.path.join('Assets','Images','Santa-light.png')).convert_alpha()
    assets[SANTAHAT] = pygame.image.load(os.path.join('Assets','Images','SantaHat.png')).convert_alpha()
    assets[SANTAHAT] = pygame.transform.scale(assets['santahat'], (115, 80))

    #Fontes
    assets[SCORE_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 28)
    assets[INIT_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 28)
    assets[TITLE_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 65)
    assets[RECORD_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 40)
    assets[GAMEOVER_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 55)
    assets[RESULT_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 20)

    #Sons
    assets[HOHOHO_SOUND] = pygame.mixer.Sound('Assets/Sounds/HoHoHo.mp3')
    assets[DEATH_SOUND] = pygame.mixer.Sound('Assets/Sounds/Death.wav')
    assets[JUMP_SOUND] = pygame.mixer.Sound('Assets/Sounds/Jump.wav')
    assets[EAT_SOUND] = pygame.mixer.Sound('Assets/Sounds/Eat.mp3')

    return assets