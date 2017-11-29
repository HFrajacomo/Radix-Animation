import pygame as pg
import random as rd
import time
from pygame.locals import *
import sys
import os

pg.init()

WIDTH = 640
HEIGHT = 480
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

N_Elements = 320
Max_value = 400

def radixsort( aList ):
  RADIX = 3
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
	maxLength = True
	# declare and initialize buckets
	buckets = [list() for _ in range( RADIX )]
 
	# split aList between lists
	for	 i in aList:
	  tmp = i / placement
	  buckets[tmp % RADIX].append( i )
	  if maxLength and tmp > 0:
		maxLength = False
 
	# empty lists into aList array
	a = 0
	for b in range( RADIX ):
	  buck = buckets[b]
	  for i in buck:
		aList[a] = i
		a += 1
		screen.fill(BLACK)
		DrawBars(aList)
		DrawRedBar(a, aList[a-1])
		pg.display.update()
		time.sleep(0.005)
 
	# move to next digit
	placement *= RADIX


	
def DrawBars(Lista):
	i = 0
	for i in range (0, len(Lista)):
		BlitTitle()
		pg.draw.rect(screen, WHITE, ((i*(WIDTH/N_Elements)),HEIGHT-(Lista[i]*(HEIGHT/Max_value)),((WIDTH/N_Elements)-2),1000))
		i = i + 1
		
def DrawRedBar(Index, ValIndex):
	BlitTitle()
	pg.draw.rect(screen, RED, ((Index*(WIDTH/N_Elements)),HEIGHT-(ValIndex*(HEIGHT/Max_value)),((WIDTH/N_Elements)-2),1000))
	pg.display.update()
	
def DrawGreenBars(Lista):
	i = 0
	for i in range (0, len(Lista)):
		pg.draw.rect(screen, GREEN, ((i*(WIDTH/N_Elements)),HEIGHT-(Lista[i]*(HEIGHT/Max_value)),((WIDTH/N_Elements)-2),1000))
		BlitTitle()
		pg.display.update()
		time.sleep(0.001)
		i = i + 1
	
def BlitTitle():
	screen.blit(Surf,(10, 10, 250, 76))
	
#				  #
#		Main	  #
#				  #
screen = pg.display.set_mode((WIDTH, HEIGHT))
	
Title = pg.font.Font("Arial.ttf", 24)
Surf = Title.render("Radix Sort (LSD) - " + str(N_Elements) + " elements", 1, WHITE)
BlitTitle()

i=0
Lista = []
rd.seed(rd.randint(0,10000000000))

for i in range(0,N_Elements):
	Lista.append(rd.randint(0, Max_value))

	

radixsort(Lista)
DrawGreenBars(Lista)
pg.display.update()

while(True):
	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
	pg.display.update()
