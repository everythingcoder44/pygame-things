#! /usr/bin/env python

import pygame

width = 640
height = 400
screen = pygame.display.set_mode((width, height))
bgcolor = 255, 255, 255
running = 1
x = 0
x2 = 0
l1pos1_1 = 0
l1pos1_2 = 0 
l1pos2_1 = l1pos1_1
l1pos2_2 = height-1
l2pos1_1 = 0
l2pos1_2 = 0
l2pos2_2 = height-1
diry = 1
dirx = 0.5
dirx2 = 0.5
diry2 = 1
linecolor = []
for i in range(1, 63):
	linecolor.append((0, 0, i*4))
for i in range (1, 63):
	linecolor.append((0, 0, 255 - i*4 ))
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	
	screen.fill(bgcolor)
	pygame.draw.aaline(screen, linecolor[i], (l1pos1_1, l1pos1_2),(l1pos1_1, l1pos2_2))	
	pygame.draw.aaline(screen, linecolor[i], (0, x), (width-1, x))
	pygame.draw.aaline(screen, linecolor[i], (0, x2), (width-1, x2))
	pygame.draw.aaline(screen, linecolor[i], (l2pos1_1, l2pos1_2),(l2pos1_1, l2pos2_2))
	l1pos1_1 += dirx
	x += diry
	x2 += dirx2
	l2pos1_1 += diry2
	if l1pos1_1 == 0 or l1pos1_1 == width-1:
		dirx *= -1
	if x == 0 or x == height-1:
		diry *= -1
	if x2 == 0 or x2  == height-1:
		dirx2 *= -1
	if l2pos1_1 == 0  or l2pos1_1 == width-1:
		diry2 *= -1
	pygame.display.flip()
