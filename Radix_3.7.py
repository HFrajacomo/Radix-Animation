import pygame as pg
import pyaudio
import numpy as np
import random as rd
import time
from pygame.locals import *
import sys
import os

pg.init()
P = pyaudio.PyAudio()

volume = 0.5
sample_rate = 44100
duration = 0.1
freq = 100

WIDTH = 640
HEIGHT = 480
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

# MAIN CONTROLLERS
N_Elements = 320
Max_value = 400
No_Sound = True

def radixsort( aList ):
	RADIX = 10
	maxLength = False
	tmp , placement = -1, 1
	buckets = []
 
	while not maxLength:
		maxLength = True
		# declare and initialize buckets
		buckets = [list() for _ in range( RADIX )]
 
		# split aList between lists
		for	 i in aList:
			tmp = int(i / placement)
			buckets[tmp % RADIX].append( i )
			if maxLength and tmp > 0:
				maxLength = False
	 
		# empty lists into aList array
		a = 0
		for b in range( RADIX ):
			buck = buckets[b]
			for i in buck:
				aList[a] = i
				a = a + 1
				screen.fill(BLACK)
				DrawWhiteBars(aList)
				DrawRedBar(a, aList[a-1])

	 
		# move to next digit
		placement = placement * RADIX

	
def DrawWhiteBars(Lista):
	i = 0
	for i in range (0, len(Lista)):
		BlitTitle()
		pg.draw.rect(screen, WHITE, ((i*(WIDTH/N_Elements)),HEIGHT-(Lista[i]*(HEIGHT/Max_value)),((WIDTH/N_Elements)-2),1000))
		i = i + 1
	
def DrawRedBar(Index, ValIndex):
	BlitTitle()
	GenerateSound(ValIndex)
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
	
def GenerateSound(Index):
	if(No_Sound):
		return
	samples = (np.sin(2*np.pi*((freq+(Index*3))/sample_rate)*np.arange(sample_rate*duration))).astype(np.float32)
	#samples = (np.sin(2*np.pi*np.arange(sample_rate*duration)*(freq+Index)/sample_rate)).astype(np.float32)
	stream = P.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, output=True)
	stream.write(volume*samples) # Play
	
	
#				  #
#		Main	  #
#				  #


# Aumenta o Display horizontalmente
if(N_Elements > 320):  
	WIDTH = N_Elements*2
	
# Sincroniza as barras horizontalmente
elif(WIDTH%N_Elements != 0):
	HSync = (WIDTH%N_Elements)
	WIDTH = (WIDTH - HSync)*2


screen = pg.display.set_mode((WIDTH, HEIGHT))
	
Title = pg.font.Font("Arial.ttf", 24)
Surf = Title.render("Radix Sort (LSD) - " + str(N_Elements) + " elements", 1, WHITE)
BlitTitle()

i=0
Lista = []
rd.seed(rd.randint(0,10000000000))

for i in range(0,N_Elements):
	Lista.append(rd.randint(0, Max_value))

DrawWhiteBars(Lista)

radixsort(Lista)

DrawGreenBars(Lista)

while(True):
	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
	pg.display.update()
