import pygame

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
width=800
height=600


											   
gameDisplay = pygame.display.set_mode((width,height))
	



def car(x,y):
	gameDisplay.blit(carImg,(x,y))
	

rd = pygame.image.load('roadmap.png')
gameDisplay.blit(rd,(0,0))
pygame.display.set_caption('SAR Game1')
clock = pygame.time.Clock()
carImg=pygame.image.load('car2.png')

def game_loop():
	x=(width*0.45)
	y=(height*0.75)
	x_change=0
	y_change=0
	counter=0
	carDamaged=False
	carDamagedPercent=0
	ExitGame=False
	while not ExitGame:
		for event in pygame.event.get():
			counter+=1
			if event.type==pygame.QUIT:
				ExitGame=True


			if(event.type==pygame.KEYDOWN):
				if(event.key==pygame.K_LEFT):
					x_change=-5
				if(event.key==pygame.K_RIGHT):
					x_change=5

				if(event.key==pygame.K_UP):
					y_change=-10


				if(event.key==pygame.K_DOWN):
					y_change=10


			if event.type==pygame.KEYUP:
				if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
					x_change=0

				if(event.key==pygame.K_UP or event.key==pygame.K_DOWN):
					y_change=0



		x+=x_change
		y+=y_change

		if(x>=width-69 or x<0):
			x=width
			print (" You crashed")
			ExitGame=True

		if(y>=height-132 or y<0):
			y=height
			print(" You crashed")
			ExitGame = True


		
		pygame.display.update()
		gameDisplay.blit(rd,(0,0))
		car(x,y)
		clock.tick(500)
		
game_loop()
pygame.quit()
quit()



