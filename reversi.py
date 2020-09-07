import pygame
from mutagen.mp3 import MP3 as mp3
from pygame.locals import *
import sys
import numpy as np
import board as bd
import field as fie
import os
from os.path import join as pjoin

def main():
    screen = pygame.display.set_mode((720, 600)) # ウィンウサイズの指定
    next = ""
    while(True):
        if next == "":
            next = select_window(screen)
        elif next == "Battle":
            next = battle_window(screen)
        elif next == "Rule":
            next = Rule_window(screen)

def select_window(screen):
    myfont = pygame.font.SysFont(None,40)
    title = pygame.image.load(pjoin(os.getcwd(),pjoin("figure","title.png"))).convert_alpha()
    start = myfont.render("press S to start",True,(0,0,0))
    while(True):
        screen.fill((122,255,122))
        screen.blit(start,(200,400))
        screen.blit(title,(20,50))
        pygame.display.update() # 画面更新
        pygame.time.wait(20) # 更新間隔
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_s:
                    return "Rule"


def result_window(screen,winner,field):
    myfont = pygame.font.SysFont(None,40)

    if winner > 0:
        winner = "black"
        res = myfont.render("{} win!".format(winner),True,(220,30,30))
    elif winner < 0:
        winner = "white"
        res = myfont.render("{} win!".format(winner),True,(220,30,30))
    else:
        res = myfont.render("tie game!",True,(220,30,30))

    ret = myfont.render("press R to replay".format(winner),True,(220,30,30))
    while(True):
        screen.fill((122,255,122))
        field.draw(screen)
        screen.blit(res,(200,200))
        screen.blit(ret,(200,350))
        pygame.display.update() # 画面更新
        pygame.time.wait(20) # 更新間隔
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_r:
                    return

def battle_window(screen):
    myfont = pygame.font.SysFont(None,120)
    myfont2 = pygame.font.SysFont(None,80)
    winrect = screen.get_rect()
    f = fie.field((90,80))
    flag = 0
    mouseDown_flag = False
    isBattle = True

    while(isBattle):
        screen.fill((122,255,122))
        bnum,wnum = f.bw_num()
        leftturn = f.leftturn()
        screen.blit(myfont.render("{}".format(bnum),True,(0,0,0)),(0,0))
        screen.blit(myfont.render("{}".format(wnum),True,(255,255,255)),(600,0))
        screen.blit(myfont2.render("{} turns left".format(leftturn),True,(255,122,0)),(180,0))
        isBattle = f.draw(screen)
        if not isBattle:
            pygame.mixer.stop()
            winner = f.result()
            result_window(screen,winner,f)
            return ""

        if pygame.mouse.get_pressed()[0]:#押している間は牌を表示
            pos = pygame.mouse.get_pos()
            f.putdemo(pos,screen)
            mouseDown_flag = True

        pygame.display.update() # 画面更新
        pygame.time.wait(20) # 更新間隔

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_p:
                    f.pass_turn()
            if event.type == MOUSEBUTTONUP and mouseDown_flag:
                pos = pygame.mouse.get_pos()
                f.put(pos)
                mouseDown_flag = False

def Rule_window(screen):
    myfont = pygame.font.SysFont(None,40)
    start = myfont.render("press S to start",True,(0,0,0))
    rule = pygame.image.load(pjoin(os.getcwd(),pjoin("figure","rulesetumei.png"))).convert_alpha()
    isRule = True

    while(isRule):
        screen.fill((122,255,122))
        screen.blit(start,(200,560))
        screen.blit(rule,(100,0))
        pygame.display.update() # 画面更新
        pygame.time.wait(20) # 更新間隔
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_s:
                    return "Battle"


if __name__ == "__main__":
    pygame.init() # 初期
    pygame.display.set_caption("reversi") # ウィンドウの上の方に出てくアレの指定
    main()
