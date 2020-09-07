import pygame
from mutagen.mp3 import MP3 as mp3
from pygame.locals import *
import sys
import numpy as np
from board import board
from board import piece
import os
from os.path import join as pjoin


class field():
    def __init__(self,pos):
        self.board = board(pos[0],pos[1])
        self.font = pygame.font.SysFont(None,80)
        music_path = pjoin(os.getcwd(),"music")
        self.stack = [2,2]
        self.black_img = pygame.image.load(pjoin(os.getcwd(),pjoin("figure","stack_black.png"))).convert_alpha()
        self.white_img = pygame.image.load(pjoin(os.getcwd(),pjoin("figure","stack_white.png"))).convert_alpha()
        pygame.mixer.init()
        self.bgm = pygame.mixer.Sound(pjoin(os.getcwd(),pjoin(music_path,"bacchus.ogg")))
        self.bgm.set_volume(0.3)
        self.bgm.play(-1)
        self.bgm_end = pygame.mixer.Sound(pjoin(music_path,"passionate.ogg"))
        self.bgm_end.set_volume(0.3)
        self.cant_put_se = pygame.mixer.Sound(pjoin(music_path,"cant_put.ogg"))
        self.cant_put_se.set_volume(1.0)
        self.now_turn = 1

    def put(self,pos):
        if self.board.put(piece(pos[0],pos[1],self.now_turn)):
            self.now_turn = -self.now_turn
            self.stack[self.now_turn//2] += 1
            if self.board.num == 40:
                pygame.mixer.stop()
                self.bgm_end.play(-1)
            return self.now_turn
        else:
            self.cant_put_se.play(1)
            return self.now_turn

    def pass_turn(self):
        self.now_turn = -self.now_turn

    def putdemo(self,pos,screen):
        pie = piece(pos[0],pos[1],self.now_turn)
        pie.draw(screen)


    def draw(self,screen):
        self.board.draw(screen)
        return self.isBattle()

    def isBattle(self):
        if self.board.num >= self.board.maxNum:
            return False
        else:
            return True

    def bw_num(self):
        return len(self.board.listBoard(1)),len(self.board.listBoard(-1))

    def leftturn(self):
        return self.board.maxNum - self.board.num

    def result(self):
        blackNum,whiteNum = self.bw_num()
        if blackNum > whiteNum:# black-win
            return 1
        elif blackNum < whiteNum:# white-win
            return -1
        else:# draw
            return 0
