# hangman-gui

import pygame
from pygame.locals import *

import os
import random
from string import ascii_letters


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Hangman")


class Hangman:
    def __init__(self) -> None:
        with open("./words.txt", "r") as file:
            # picks secret word and passing it's length
            words = file.read().split("\n")
            self.secret_word = random.choice(words)
            # passing secret word`s length for making letter blanks
            self.guessed_word = "*" * len(self.secret_word)
        self.wrong_guesses = []
        self.wrong_guesses_count = 0
        self.taking_guess = True
        self.running = True
