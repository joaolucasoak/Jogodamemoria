import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('music/game.music.mp3')
pygame.music.play()
pygame.event.wait()