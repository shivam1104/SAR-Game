import pygame
import time
import random

pygame.init()

pause = False
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue=(0,0,255)
width=800
height=600
speedchanger = random.randrange(1,2)
gameDisplay = pygame.display.set_mode((width,height))

rd = pygame.image.load('roadmap1.png')
gameDisplay.blit(rd,(0,0))
l1 = pygame.image.load('r3.png')

pygame.display.set_caption('SAR Game!')
clock = pygame.time.Clock()
carImg=pygame.image.load('car2.png') #player car
carImg2=pygame.image.load('car21.png') #game icon
vcar = pygame.image.load('vcar.png') # villain car
rcar = pygame.image.load('rcar.png') # 2nd villain car
keys = pygame.image.load('keys.png')
pygame.display.set_icon(carImg2)
intro_background = pygame.image.load('background.png')
opening = pygame.mixer.Sound("opening.wav")
crashmusic = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("cheapT.wav")
credits_music = pygame.mixer.Sound("credits.wav")						   


def things_dodged(count):
	font = pygame.font.SysFont(None , 25)
	text = font.render("Score : " + str(count), True, white)
	gameDisplay.blit(text, (35,10))
def level_indicator(numb):
	font = pygame.font.SysFont(None ,50)
	text1 = font.render("Level : " + str(numb), True, red)
	gameDisplay.blit(text1,(340,300))
	pygame.display.update()
	clock.tick(100)



def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
	#pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
	gameDisplay.blit(vcar,(thingx,thingy))
		

def things2(thingx2, thingy2):
	gameDisplay.blit(rcar,(thingx2, thingy2))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None): # 2ndlast 2 are inactive and active color
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x+w>mouse[0]>x and y+h>mouse[1]>450: #denotes X position
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))

		if click[0]==1 and action!=None:
			action()
#			if action == "play":
#				game_loop()
#			elif action == "quit":
#				pygame.quit()
#				quit()
	else :
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, TextRect = text_objects(msg, smallText)
	TextRect.center = ((x+(w/2)), (y+(h/2)))
	gameDisplay.blit(textSurf,TextRect)




def crash(): #pause functionality copied
	pygame.mixer.Sound.play(crashmusic)
	largeText = pygame.font.Font('freesansbold.ttf',100)
	TextSurf, TextRect = text_objects("You Crashed!", largeText)
	TextRect.center = ((width/2),(height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.mixer.music.stop()
	while True:
		for event in pygame.event.get(): #asking for quit event
			if event.type  == pygame.QUIT:
				pygame.quit()
				quit()
		#gameDisplay.fill(white)
		button("Play Again",140,450,120,50,green,bright_green,game_loop)
		button("Quit",550,450,100,50,red,bright_red,quitgame)
		pygame.mixer.music.stop()
		pygame.display.update()
		clock.tick(500)

def finishgame():
	gameDisplay.blit(congo, ((width/2),(height/2)))

def quitgame():
	pygame.quit()
	quit()
def credits():
	pygame.mixer.Sound.stop(opening)
	pygame.mixer.Sound.play(credits_music)
	largeText = pygame.font.Font('freesansbold.ttf',20)
	TextSurf, TextRect = text_objects("Created by: Abhiram Satpute, Shivam Srivastava and Rutuparn Satpute.", largeText)
	TextRect.center = (390,25)
	while True:
		for event in pygame.event.get(): #asking for quit event
			if event.type  == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		gameDisplay.blit(TextSurf, TextRect)
		gameDisplay.blit(keys,(125,50))
		button("Main Menu",340,500,120,50,green,bright_green,game_intro)
		pygame.display.update()
		clock.tick(500)

def game_intro(): #will run just ONE time..!!!
	pygame.mixer.Sound.stop(credits_music)
	pygame.mixer.Sound.play(opening)
	intro = True
	while intro:
		for event in pygame.event.get(): #asking for quit event
			if event.type  == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(intro_background,(0,0))
		largeText = pygame.font.Font('freesansbold.ttf',100)
		TextSurf, TextRect = text_objects("SAR Game", largeText)
		TextRect.center = ((width/2),(height/4))
		gameDisplay.blit(TextSurf, TextRect)
		button("Play!",150,450,100,50,green,bright_green,game_loop)
		button("Quit",550,450,100,50,red,bright_red,quitgame)
		for event in pygame.event.get():	
			if(event.type==pygame.KEYDOWN):
				if event.key==pygame.K_F1:
					credits()
		pygame.display.update()
		clock.tick(500)




def unpause():

	global pause
	pause = False


def Paused(): 
	largeText = pygame.font.Font('freesansbold.ttf',100)
	TextSurf, TextRect = text_objects("Game Paused", largeText)
	TextRect.center = ((width/2),(height/2))
	gameDisplay.blit(TextSurf, TextRect)
	while pause:
		for event in pygame.event.get(): #asking for quit event
			if event.type  == pygame.QUIT:
				pygame.quit()
				quit()
		#gameDisplay.fill(white)
		button("Resume",150,450,100,50,green,bright_green,unpause)
		button("Quit",550,450,100,50,red,bright_red,quitgame)
		pygame.mixer.music.pause()

		pygame.display.update()
		clock.tick(500)
	pygame.mixer.music.unpause()



def game_loop():
	global pause
	x=(width*0.47)
	y=(height*0.75)
	thing_startx = random.randrange(x-70, x+150)
	thing_starty = -600
	thing_starty2= -400
	thing_startx2 = random.randrange(40, width-150)
	thing_speed = 7
	thing_speed2u = 0
	thing_speed2d = 0
	thing_width = 100
	thing_height = 100
	dodged = 0
	speedup = 0
	speeddown = 0
	pygame.mixer.music.play(-1)
	roady=-120
	x_change=0
	y_change=0
	counter=0
	pygame.mixer.Sound.fadeout(opening,1)
	#carDamaged=False
	#carDamagedPercent=0
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
					if dodged>20:
						x_change=-15
					if dodged>30:
						x_change=-20
				

				if(event.key==pygame.K_RIGHT):
					x_change=10
					if dodged>20:
						x_change=15
					if dodged>30:
						x_change=20
					
				if(event.key==pygame.K_UP):
					#y_change=-10
					#if dodged>20:
					#	y_change=-15
					#if dodged>30:
					#	y_change=-20
					speedup=1
					speeddown=0
					thing_speed2d=0
						
				if(event.key==pygame.K_DOWN):
					#y_change=10
					#if dodged>20:
					#	y_change=5
					#if dodged>30:
					#	y_change=2
					speeddown=-1
					speedup=0
					thing_speed2u=0			
				
				if (event.key == pygame.K_p):
					pause = True
					Paused()


			if event.type==pygame.KEYUP:
				if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
					x_change=0

				if(event.key==pygame.K_UP or event.key==pygame.K_DOWN):
					y_change=0
					speedup=0
					speeddown=0
			#else:
			#	speedup=0
			#	thing_speed2u=0
			#else:
			#	speeddown=0
			#	thing_speed2d=0
		if thing_speed2u<5:
			thing_speed2u+=speedup
			thing_speed+=thing_speed2u
		elif 0>thing_speed2u>5:
			thing_speed2u=0

  		if thing_speed2d>-5:
			thing_speed2d+=speeddown
			thing_speed+=thing_speed2d
		elif -5>thing_speed2d>0:
			thing_speed2d=0




		#if 7<thing_speed<15:	
		#	thing_speed+=thing_speed2u
		#	thing_speed+=thing_speed2d
									
		#if 0>thing_speed2u>20:
		#	thing_speed-=thing_speed2u
		#if -4>thing_speed2d>0:
		#	thing_speed+=thing_speed2d

		x+=x_change
		y+=y_change
		roady+=6+thing_speed
		



					
		if(roady>90): #will make the road go back
			roady=-120

		if(x>=width-74 or x<15): #boundary crashing
			x=width
			ExitGame=True
			crash()

		#if(y>=height-135 or y==0):
		#	y-=y_change

		if thing_starty > height :
			thing_starty = 0 - thing_height-49 #49 after vcar addition
			thing_startx = random.randrange(x-200, x+150)
			dodged+=1
			if dodged%4==0 and dodged<30:
				thing_speed+=2
				if dodged==23:
					thing_speed = thing_speed -3
				#if dodged ==50:
					#thing_speed = thing_speed - 3
					if dodged==80:
						thing_speed+=5


		if dodged==25:
			level_indicator(2)
		if 52>dodged>50:
			level_indicator(3)
		if 80<dodged<83:
			level_indicator(4)
		if dodged>=50:
			things2(thing_startx2, thing_starty2)
			if thing_starty2 > height :
				thing_starty2 = 0 - thing_height-25-random.randrange(150,1000) #25 after rcar addition
				thing_startx2 = random.randrange(200, width-250)
				dodged+=1
			
			if y>thing_starty2 and y< thing_starty2+thing_height + 25 or y +132 > thing_starty2 and y+132 < thing_starty2+ thing_height +25: #remove 49 if vcar removed
				#if x > thing_startx and x < thing_startx + thing_width or x + 69 > thing_startx and x + 69 < thing_startx + thing_width : # DAMN
				if (thing_startx2<x+65 and thing_startx2+42>x ): #replace 47 by thing_width
					crash()



			#thing_speed +=1
			#thing_width+= (dodged*1.2)
		#for collision, one of the side AND y has to be hit
		if y>thing_starty and y< thing_starty+thing_height + 49 or y +132 > thing_starty and y+132 < thing_starty+ thing_height +49: #remove 49 if vcar removed
			#if x > thing_startx and x < thing_startx + thing_width or x + 69 > thing_startx and x + 69 < thing_startx + thing_width : # DAMN
			if (thing_startx<x+65 and thing_startx+72>x ): #replace 72 by thing_width
				crash()

		if (thing_startx+75<0 or thing_startx>800):
			dodged-=1
		if (thing_startx2+62<0 or thing_startx2>800):
			dodged-=1


		pygame.display.update()
		gameDisplay.blit(rd,(0,0))
		
		gameDisplay.blit(l1,(141,roady))
		
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		
		thing_starty += thing_speed
		thing_starty2 += thing_speed	
		car(x,y)
		things_dodged(dodged)
		clock.tick(1000)		
game_intro()
credits()
game_loop()
pygame.quit()
quit()
#ending the game @line 333... halfway to hell!! XD ; ADDED LATER --> SO CLOSE
