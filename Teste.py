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

MAX_CHARS = 28
N_Elements = 20
Max_value = 100

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
 
	# move to next digit
	placement *= RADIX

	
def DrawBars(Lista):
	i = 0
	for i in range (0, len(Lista)):
		pg.draw.rect(screen, WHITE, (0+(i*32),HEIGHT-(Lista[i]*4.8),30,1000))
		i = i + 1
		
screen = pg.display.set_mode((WIDTH, HEIGHT))
i=0
Lista = []

rd.seed(5)

for i in range(0,N_Elements):
	Lista.append(rd.randrange(0, Max_value))

DrawBars(Lista)
	
#print(Lista)
radixsort(Lista)
#print(Lista)

while(True):
	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
	pg.display.update()