import pygame
import time

pygame.init()

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

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
	
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',100) #text details
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((width/2),(height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(3)

	game_loop()


def crash():
	message_display('You Crashed!')

rd = pygame.image.load('roadmap1.png')
gameDisplay.blit(rd,(0,0))
l1 = pygame.image.load('r3.png')

pygame.display.set_caption('SAR Game1')
clock = pygame.time.Clock()
carImg=pygame.image.load('car2.png')

def game_loop():
	roady=-120
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
				pygame.quit()
				quit()


			if(event.type==pygame.KEYDOWN):
				if(event.key==pygame.K_LEFT):
					x_change=-10
				

				if(event.key==pygame.K_RIGHT):
					x_change=10
					
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
		roady+=10

		if(roady>90): #will make the road go back
			roady=-120

		if(x>=width-69 or x<0):
			x=width
			print ("You crashed..!!")
			ExitGame=True
			crash()

		if(y>=height-135 or y==0):
			y-=y_change

		

		
		pygame.display.update()
		gameDisplay.blit(rd,(0,0))
		gameDisplay.blit(l1,(141,roady))
		car(x,y)
		clock.tick(100)
		
game_loop()
pygame.quit()
quit()



