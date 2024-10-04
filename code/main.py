import pygame
from os.path import join
from random import randint

pygame.init()

VERSION = "0.2.0"
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(f"Asteroid Wars {VERSION}")
running = True

surf = pygame.Surface((100, 200))
surf.fill("white")
x = 100

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	display_surface.fill('black')
	for pos in star_positions:
		display_surface.blit(star_surf, pos)
			
	x += 0.1
	display_surface.blit(player_surf, (x, 150))

	pygame.display.update()

pygame.quit()