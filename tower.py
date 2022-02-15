
import pygame as pg


color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red
color4 = pygame.Color(0, 255, 0)       # Green
color4 = pygame.Color(0, 0, 255)       # Blue


DISPLAYSURF = pygame.display.set_mode((300,300))


while True:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()



