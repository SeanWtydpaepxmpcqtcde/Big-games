#This is a pygame program, I'm going to make Megalovania game(Especially the sans boss fight)
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Megalovania Game")
# Define colors(THere wil be lack background, white text, red for the player(heart), blue and orange for boss atttacks)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
# Set up the player properties
