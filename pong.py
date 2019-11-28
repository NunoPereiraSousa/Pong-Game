import pygame
import math
import random
import time
import sys
from pygame.locals import *
from random import randint
from paddles import*
from ball import *
from ghostball import *

pygame.init()

# ---------------------------- GLOBAL VARIABLES ------------------------------------- #

# window variables
window_width = 1024
window_height = 700
window = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Pong 91805")

# define the classes instances in variables
ball = Ball()
ball2 = Ball2()
paddle1 = Paddle1()
paddle2 = Paddle2()
paddleCenter = PaddleCenter()

# Player Scores
score1 = 0
score2 = 0

# When the ball leaves the center of the window the ball and colides with the top or bottom wall, it can go to the right or the left
# And when the ball colides with ones of the paddles, the ball can no longer go the same side 
lastTouch = randint(1, 2)
secondBallLastTouch = randint(1, 2) # This variable has the same explanation as the variable of top of this. But is used to the Wind Area game mode

# "Get the Player Ready for the mach"
ready = False

# color variables
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
darkOrange = [255, 140, 0]
opaqueBlack = [0, 0, 0, 0.5]
deepskyblue = [0, 191, 255]

# functions runners controllers
run1 = True # Main menu 
pause = False # Pause menu
resuming = False # When the match is resumed... 3, 2, 1, ... 
fillUpgrade = False # This variables will turn on / off the game modes
gameUpgrade = randint(1, 4) # Type of upgrade that is going to be done in each sub game mode
firstTimeDisplay = True # Show ready, set, go
fireON = False # Variable used in the Fire Ball game mode. When the ball is in the big center of the giant ball this ball turns true, if not, turns false. Consequence: change/ not change of ball speed

# ---------------------------- END OF GLOBAL VARIABLES ------------------------------------- #

#* Function that displays the text of "3, 2, 1, Go!" when the game starts after pause
def drawText():
    font = pygame.font.Font(None, 80)

    pygame.draw.rect(window, BLACK, (window_width / 2 - 50, window_height / 2 - 50, 120, 100))
    pygame.display.update()

    textReady = font.render("3", True, WHITE, BLACK)
    text_rect = textReady.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textReady, text_rect)

    pygame.display.update()
    time.sleep(0.7)

    textReady2 = font.render("3", True, BLACK, BLACK)
    text_rect = textReady2.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textReady2, text_rect)

    pygame.display.update()
    time.sleep(0.7)

    textSet = font.render("2", True, WHITE, BLACK)
    text_rect = textSet.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textSet, text_rect)

    pygame.display.update()
    time.sleep(0.7)

    textSet2 = font.render("2", True, BLACK, BLACK)
    text_rect = textSet2.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textSet2, text_rect)

    pygame.display.update()
    time.sleep(0.7)

    textGo = font.render("1", True, WHITE, BLACK)
    text_rect = textGo.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textGo, text_rect)

    pygame.display.update()
    time.sleep(0.7)

    textGo2 = font.render("1", True, BLACK, BLACK)
    text_rect = textGo2.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textGo2, text_rect)

    pygame.display.update()
    time.sleep(0.7)

#* Function that displays the text of "Ready, Set, Go" when the game/ round begins
def drawTextReadySetGo():
    font = pygame.font.Font(None, 60)

    pygame.draw.rect(window, BLACK, (window_width / 2 - 50, window_height / 2 - 50, 250, 100))
    pygame.display.update()

    textReady = font.render("Ready", False, WHITE, BLACK)
    text_rect = textReady.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textReady, text_rect)

    pygame.display.update()
    time.sleep(0.6)

    textReady2 = font.render("Ready", True, BLACK, BLACK)
    text_rect = textReady2.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textReady2, text_rect)

    pygame.display.update()
    time.sleep(0.7)

    textSet = font.render("Set", True, WHITE, BLACK)
    text_rect = textSet.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textSet, text_rect)

    pygame.display.update()
    time.sleep(0.5)

    textSet2 = font.render("Set", True, BLACK, BLACK)
    text_rect = textSet2.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textSet2, text_rect)

    pygame.display.update()
    time.sleep(0.5)

    textGo = font.render("Go", True, WHITE, BLACK)
    text_rect = textGo.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textGo, text_rect)

    pygame.display.update()
    time.sleep(0.5)

    textGo2 = font.render("Go", True, BLACK, BLACK)
    text_rect = textGo2.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(textGo2, text_rect)

    pygame.display.update()
    time.sleep(0.3)

#* ------------------------ END FUNCTION -----------------------------------------

#* Function that draw and displays the net
def drawNet():
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  0, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  50, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  100, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  150, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  200, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  250, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  300, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  350, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  400, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  450, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  500, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  550, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  600, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  650, 6, 40))
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(6/2),  700, 6, 40))

#* ------------------------ END FUNCTION -----------------------------------------

#* Function that restart the values
def initialization():
    global paddle1, paddle2,paddleCenter, ball, ball2, direction, ready, negativeY, negativeX, score2, score1, lastTouch, firstTimeDisplay, gameUpgrade, secondBallLastTouch
    paddle1.y = window_height / 2 - 50  # first player paddle position in y
    paddle2.y = window_height / 2 - 50  # second player paddle position in y
    paddleCenter.y = 1 # paddle wall position in y
    paddleCenter.step = 2 # Increment of position in the x axis
    ball.x = window_width / 2 # place ball in the center of the window
    ball.y = window_height / 2 # place ball in the center of the window
    ball.dt = 1 # ball movement
    ball.vel = 5 # ball velocity
    ball2.x = window_width / 2 # Wind Area - place ball in the center of the window
    ball2.y = window_height / 2 # Wind Area - place ball in the center of the window
    ball2.dt = 1 # Wind Area - ball movement
    ball2.vel = 5 # Wind Area - ball velocity
    direction = random.uniform(-0.25 * math.pi, 0.25 * math.pi) # Angle 
    ball.vx = ball.vel * math.cos(direction) # position change in the x axis
    ball.vy = ball.vel * math.sin(direction) # position change in the y axis
    direction = random.uniform(-0.25 * math.pi, 0.25 * math.pi) # Angle for the wind area mode
    ball2.vx = ball2.vel * math.cos(direction) # Wind Area - position change in the x axis
    ball2.vy = ball2.vel * math.sin(direction) # Wind Area - position change in the x axis
    ball2.color = deepskyblue # Wind Area - ball color
    negativeX = randint(0, 1) # Variable that secures the side the ball is sent when the/ round starts (goes left or right)
    # Classic Pong ball
    if negativeX == 1:
        ball.vx = -ball.vx
    negativeY = randint(0, 1)
    if negativeY == 0:
        ball.vy = -ball.vy

    # Wind Area ball
    negativeX = randint(0, 1)
    if negativeX == 1:
        ball2.vx = -ball2.vx
    negativeY = randint(0, 1)
    if negativeY == 0:
        ball2.vy = -ball2.vy

    ready = False
    lastTouch = randint(1, 2)
    secondBallLastTouch = randint(1,2)
    firstTimeDisplay = True
    gameUpgrade = randint(1, 4)

#* Function of the main menu
def myMainMenu():
    global run1, event
    
    while run1:
        initialization()
        window.fill(BLACK) # fill window
        for event in pygame.event.get():
            pass

        # PONG GAME TEXT
        font = pygame.font.Font(None, 80)
        text = font.render("Pong Game", True, WHITE)
        text_rect = text.get_rect(center = (window_width/2, window_height / 2 - 250))
        window.blit(text, text_rect)

        # CREATE BUTTONS
        button(window_width / 2 - 100, window_height / 2 - 80, 200, 40, "classic")
        button(window_width / 2 - 100, window_height / 2 - 5, 200, 40, "superPong")
        button(window_width / 2 - 100, window_height / 2 + 70, 200, 40, "Quit")
        
        # HUGE BORDER
        pygame.draw.rect(window, (WHITE), (window_width / 2 - 300,  window_height / 2 - 150, 600, 400), 10)
        pygame.display.update()

#* ------------------------ END FUNCTION -----------------------------------------

#* Function that has the objective to stop the game when the players asks 
def buttonPause(x, y, width, height, action=None):
    global pause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(window, WHITE, (x, y, width, height), 2)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == 'pause':
                pause = True
                paddle1.dt = 0
                paddle2.dt = 0
                ball.dt = 0
                myPauseMenu()

    font = pygame.font.Font(None, 40)
    buttonText = font.render('||', True, WHITE)
    window.blit(buttonText, [22, 15])

#* ------------------------ END FUNCTION -----------------------------------------

#* Function that defines the main menu buttons 
def button(x, y, width, height, action=None):
    global run1, pause, resuming, ready, fillUpgrade

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(window, WHITE, (x, y, width, height), 2)
    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == 'classic':
                run1 = False
                pause = False
                resuming = False
                ready = False
                fillUpgrade = False
                action = ""
            elif action == 'superPong':
                run1 = False
                pause = False
                resuming = False
                ready = False
                fillUpgrade = True
            elif action == 'Quit':
                pygame.quit()
                quit()

    font = pygame.font.Font(None, 20)
    buttonText = font.render('Classic Pong', True, WHITE)
    window.blit(buttonText, [window_width / 2 - 40, window_height / 2 - 65])

    buttonText2 = font.render("Super Pong", True, WHITE)
    window.blit(buttonText2, [window_width / 2 - 36, window_height / 2 + 10])

    buttonText4 = font.render("Exit", True, WHITE)
    window.blit(buttonText4, [window_width / 2 - 10, window_height / 2 + 83])

    font = pygame.font.Font(None, 25)
    buttonText = font.render('This game was developed by Nuno and Tiago', True, WHITE)
    window.blit(buttonText, [window_width / 2 - 180, window_height / 2 + 160])
  
#* ------------------------ END FUNCTION -----------------------------------------

#* Function that created the pause menu buttons
def myPauseMenu():
    global event, key_pressed, mouse, pause
    while pause:
        window.fill(opaqueBlack)
        for event in pygame.event.get():
            pass
        key_pressed = pygame.key.get_pressed()

        # PONG GAME TEXT
        font = pygame.font.Font(None, 80)
        text = font.render("GAME PAUSED", True, WHITE)
        text_rect = text.get_rect(center = (window_width / 2, window_height / 2 - 250))
        window.blit(text, text_rect)

        mouse = pygame.mouse.get_pos()
        # CREATE BUTTONS
        pauseOptionsButton(window_width / 2 - 450, window_height / 2 - 150, 200, 40, "HOME")
        pauseOptionsButton(window_width / 2 - 100, window_height / 2 - 150, 200, 40, "RESUME")
        pauseOptionsButton(window_width / 2 + 250, window_height / 2 - 150, 200, 40, "CLOSE GAME")

        # COPY RIGHT TEXT
        font = pygame.font.Font(None, 25)
        buttonText = font.render('This game was developed by Nuno and Tiago', True, WHITE)
        window.blit(buttonText, [window_width / 2 - 180, window_height / 2 + 280])
        pygame.display.update()

    window.fill(BLACK)
    pygame.display.update()

#* ------------------------ END FUNCTION -----------------------------------------

#* Function that sets the pause menu buttons
def pauseOptionsButton(x, y, width, height, action = None):
    global pause,run1,resuming,ready,score1,score2

    font = pygame.font.Font(None, 20)
    buttonText = font.render('HOME', True, WHITE)
    window.blit(buttonText, [window_width / 2 - 375, window_height / 2 - 135])

    # SECOND BUTTON TEXT
    buttonText2 = font.render("RESUME", True, WHITE)
    window.blit(buttonText2, [window_width / 2 - 30, window_height / 2 - 135])

    # THIRD BUTTON TEXT
    buttonText3 = font.render("CLOSE GAME", True, WHITE)
    window.blit(buttonText3, [window_width / 2 + 305, window_height / 2 - 135])

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # FIRST BUTTON
    pygame.draw.rect(window, WHITE, (x, y, width, height), 2)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == 'HOME':
                run1 = True
                pause = False
                resuming = False
                ready = True
                score1 = 0
                score2 = 0
            elif action == 'RESUME':
                pause = False
                resuming = True
            elif action == 'CLOSE GAME':
                pygame.quit()
                quit()

#* ------------------------ END FUNCTION -----------------------------------------

#* Function that inform that a player has scored a goal
def goalScored():
    pygame.draw.rect(window, BLACK, (window_width / 2 - 100, window_height / 2 - 50, 250, 100))
    font = pygame.font.Font(None, 60)
    goal = font.render("GOAL!!!!!!!", False, WHITE, BLACK)
    text_rect = goal.get_rect(center = (window_width / 2, window_height / 2))
    window.blit(goal, text_rect)
    pygame.display.update()
    time.sleep(0.7)

#* ------------------------ END FUNCTION -----------------------------------------               

#? ------------------------- GAME MODE AREA -------------------------------------
#* Function that makes the fill upgrade putting a fog in the middle of the field 
def fogOfWar():
    pygame.draw.rect(window, (WHITE), (window_width / 2 -(200 / 2),  0, 200, window_height))

#* ------------------------ END FUNCTION -----------------------------------------

#  *function that makes the fill upgrade putting a circle of fire in the middle that makes the ball faster  
def fireball():
    global ball, fireON
    pygame.draw.circle(window, (darkOrange), (int(window_width / 2), int(window_height / 2)), 100)
    if ball.x>window_width / 2 - 100 and ball.x <= window_width / 2 + 100 and ball.y < window_height / 2 + 100 and ball.y > window_height / 2 - 100:
        fireON = True

#* ------------------------ END FUNCTION -----------------------------------------

#**function that makes the fill upgrade putting a wall that changes the direction of the ball after contact
def directionChange():
    global ball, lastTouch, direction, paddleCenter
    pygame.draw.rect(window, (deepskyblue), (paddleCenter.x,  paddleCenter.y, paddleCenter.width, paddleCenter.height))
    
#* ------------------------ END FUNCTION -----------------------------------------
   
#* Wind Area - wall paddle movement
    paddleCenter.y += paddleCenter.step
    if paddleCenter.y < 0:
       paddleCenter.step = paddleCenter.step * -1
    if paddleCenter.y + paddleCenter.height >= window_height:
       paddleCenter.step = paddleCenter.step * -1    

#* Wind Area - touch on the wall
    if lastTouch == 1:
        if (ball.y) >= paddleCenter.y and (ball.y) <= (paddleCenter.y + paddleCenter.height) and (ball.x + ball.radius) > paddleCenter.x and (ball.x + ball.radius) < paddleCenter.x + paddleCenter.width / 2: 
            direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)

            # This variable changes the position in X
            ball.vx = ball.vel * math.cos(direction)

            # This variable changes the position in y
            ball.vy = ball.vel * math.sin(direction)

            negativeY = randint(0, 1)

            if ball.vx < 0:
                ball.vx = -ball.vx
            if negativeY == 0:
                ball.vy = -ball.vy
    elif lastTouch == 2:
        if (ball.y) >= paddleCenter.y and (ball.y) <= (paddleCenter.y + paddleCenter.height) and (ball.x - ball.radius) > paddleCenter.x+ paddleCenter.width / 2 and (ball.x - ball.radius) <= paddleCenter.x + paddleCenter.width:
            direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
            # This variable changes the position in X
            ball.vx = ball.vel * math.cos(direction)
            # This variable changes the position in y
            ball.vy = ball.vel * math.sin(direction)
            negativeY = randint(0, 1)

            if ball.vx > 0:
                ball.vx = -ball.vx
            if negativeY == 0:
               ball.vy = -ball.vy

#* Function that makes the fill upgrade putting a "ghostBALL" in the game
def ghostBall():
    global ball2, direction, secondBallLastTouch

    pygame.draw.circle(window, (BLACK), (int(ball2.x), int(ball2.y)), ball2.radius)
    pygame.draw.circle(window, (ball2.color), (int(ball2.x), int(ball2.y)), ball2.radius)

    # Ball postion change
    ball2.x += ball2.vx * ball2.dt
    ball2.y += ball2.vy * ball2.dt

    #* When the ghost ball touches left barrier
    if ball2.x - ball2.radius >= window_width:
        secondBallLastTouch = 2
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        # This variable changes the position in X
        ball2.vx = ball2.vel * math.cos(direction)
        # This variable changes the position in y
        ball2.vy = ball2.vel * math.sin(direction)
        negativeY = randint(0, 1)

        if ball2.vx > 0:
            ball2.vx = -ball2.vx
        if negativeY == 0:
            ball2.vy = -ball2.vy

        ball2.vel = 8
        ball2.color = WHITE

    #* When the ghost ball touches right barrier
    if ball2.x - ball2.radius <= 0:  
        secondBallLastTouch = 1
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        ball2.vx = ball2.vel * math.cos(direction) # This variable changes the position in X
        ball2.vy = ball2.vel * math.sin(direction) # This variable changes the position in Y
        negativeY = randint(0, 1)

        if ball2.vx < 0:
            ball2.vx = -ball2.vx
        if negativeY == 0:
            ball2.vy = -ball2.vy

        ball2.vel = 8
        ball2.color = WHITE

    #* When the ghost ball touches top barrier
    if ball2.y + ball2.radius >= window_height:
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        ball2.vx = ball2.vel * math.cos(direction) # This variable changes the position in X
        ball2.vy = ball2.vel * math.sin(direction) # This variable changes the position in Y

        if ball2.vy > 0:
            ball2.vy = -ball2.vy
        if secondBallLastTouch == 1 and ball.vx < 0:
            ball2.vx = -ball2.vx
        if secondBallLastTouch == 2 and ball.vx > 0:
            ball2.vx = -ball2.vx
        ball2.color = WHITE

    #* When the ghost ball touches bottom barrier
    if ball2.y <= 0:
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        # !this variable changes the position in X
        ball2.vx = ball2.vel*math.cos(direction)
        # !this variable changes the position in y
        ball2.vy = ball2.vel*math.sin(direction)
        if ball2.vy < 0:
            ball2.vy = -ball2.vy
        if secondBallLastTouch == 1 and ball2.vx < 0:
            ball2.vx = -ball2.vx
        if secondBallLastTouch == 2 and ball2.vx > 0:
            ball2.vx = -ball2.vx
        ball2.color = WHITE

    #* Player 1 paddle contact
    if (ball2.y) >= paddle2.y and (ball2.y) <= (paddle2.y + 100) and (ball2.x - ball2.radius) <= (20 + 15):
        # direction = random.uniform(0, 2*math.pi)
        secondBallLastTouch = 1
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        ball2.vx = ball2.vel * math.cos(direction)
        ball2.vy = ball2.vel * math.sin(direction)
        negativeY = randint(0, 1)

        if ball2.vx < 0:
            ball2.vx = -ball2.vx
        if negativeY == 0:
            ball2.vy = -ball2.vy

        ball2.vel=8
        ball2.color=WHITE


    #* Player 2 paddle contact
    if (ball2.y ) >= paddle1.y and (ball2.y ) <= (paddle1.y + 100) and (ball2.x + ball2.radius) >= (window_width - 40):
        # direction = random.uniform(0, 2*math.pi)
        secondBallLastTouch = 2
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        ball2.vx = ball2.vel * math.cos(direction)
        ball2.vy = ball2.vel * math.sin(direction)
        negativeY = randint(0, 1)

        if ball2.vx > 0:
            ball2.vx = -ball2.vx
        if negativeY == 0:
            ball2.vy = -ball2.vy

        ball2.vel = 8
        ball2.color = WHITE

#* ------------------------ END FUNCTION -----------------------------------------

#* Function that shows the type of game that is been played
def gameTypeDisplay():
    global firstTimeDisplay, gameUpgrade
    if firstTimeDisplay == True and gameUpgrade == 1 :
        font = pygame.font.Font(None, 60)
        textReady = font.render("FOG OF WAR", True, WHITE, BLACK)
        text_rect = textReady.get_rect(center = (window_width / 2, window_height / 2-100))
        window.blit(textReady, text_rect)
        time.sleep(0.5)
        firstTimeDisplay = False
    
    if firstTimeDisplay == True and gameUpgrade == 2:
        font = pygame.font.Font(None, 60)
        textReady = font.render("FIRE BALL", True, WHITE, BLACK)
        text_rect = textReady.get_rect(center = (window_width / 2, window_height / 2-100))
        window.blit(textReady, text_rect)
        time.sleep(0.5)
        firstTimeDisplay = False

    if firstTimeDisplay == True and gameUpgrade == 3:
        font = pygame.font.Font(None, 60)
        textReady = font.render("WINDY AREA", True, WHITE, BLACK)
        text_rect = textReady.get_rect(center = (window_width / 2, window_height / 2-100))
        window.blit(textReady, text_rect)
        time.sleep(0.5)
        firstTimeDisplay = False
    
    if firstTimeDisplay == True and gameUpgrade == 4:
        font = pygame.font.Font(None, 60)
        textReady = font.render("GLITCHED BALL", True, WHITE, BLACK)
        text_rect = textReady.get_rect(center = (window_width / 2, window_height / 2-100))
        window.blit(textReady, text_rect)
        time.sleep(0.5)
        firstTimeDisplay = False

initialization()

#! GAME LOOP STARTS HERE
while True:
    myMainMenu()

    for event in pygame.event.get():
        pass

    window.fill(BLACK)

    #* Scoring board
    space = "       "
    outputText= (str(score1) + space + str(score2))  
  
    font = pygame.font.Font(None, 80)
    text = font.render(outputText, True, WHITE, BLACK)
    text_rect = text.get_rect(center = (window_width / 2, window_height / 2 - 270))
    window.blit(text, text_rect)

    key_pressed = pygame.key.get_pressed()

    #* Paddle move with arrows and keys (w and s)
    if key_pressed[K_UP] and paddle1.y > 0:
        if paddle1.y >= 0:
            paddle1.y -= 10 * paddle1.dt
    if key_pressed[K_DOWN] and paddle1.y < window_height - 100:
        if paddle1.y <= window_height:
            paddle1.y += 10 * paddle1.dt

    if key_pressed[K_s] and paddle2.y < window_height - 100:
        if paddle2.y <= window_height:
            paddle2.y += 10 * paddle2.dt

    if key_pressed[K_w] and paddle2.y > 0:
        if paddle2.y >= 0:
            paddle2.y -= 10 * paddle2.dt


    #* Pause Button
    buttonPause(10, 10, 40, 40, "pause")

    #* Draw the first paddle
    pygame.draw.rect(window, (WHITE), (20,  paddle2.y, 15, 100))
    
    #* Draw the second paddle
    pygame.draw.rect(window, (WHITE), ((window_width-40), paddle1.y, 15, 100))
 
    drawNet()

    if resuming == True:
        ball.dt = 0
        paddle1.dt = 0
        paddle2.dt = 0   
        
        drawText()
        
        ball.dt = 1
        paddle1.dt = 1
        paddle2.dt = 1
        resuming = False

    if ready == False and score1 < 6 or ready == False and score2 < 6:
        ball.dt = 0
        paddle1.dt = 0
        paddle2.dt = 0
        if fillUpgrade == True:
            gameTypeDisplay()
        
        drawTextReadySetGo()
        
        ball.dt = 1
        paddle1.dt = 1
        paddle2.dt = 1
        ready = True

    #* Calls the fog of war function
    if fillUpgrade == True and gameUpgrade == 1:
            fogOfWar()
    #* calls the fire ball function
    if fillUpgrade == True and gameUpgrade == 2:
            fireball()
    #* calls the center wall function
    if fillUpgrade == True and gameUpgrade == 3:
            directionChange()

    #* calls the ghostBall function
    if fillUpgrade == True and gameUpgrade == 4:
            ghostBall()

    #* Draw the ball
    pygame.draw.circle(window, (BLACK), (int(ball.x), int(ball.y)), ball.radius)
    pygame.draw.circle(window, (WHITE), (int(ball.x), int(ball.y)), ball.radius)

    #* Ball postion change
    ball.x += ball.vx * ball.dt
    ball.y += ball.vy * ball.dt

    #* Contact with the border

    #* Left
    if ball.x + ball.radius <= 0:
        ball.vx = -ball.vx
        score2 += 1
        ball.dt = 0
        goalScored()
        initialization()
    #* Right
    if ball.x - ball.radius >= window_width:
        score1 += 1
        ball.dt = 0
        goalScored()
        initialization()

    #* Top
    if ball.y + ball.radius >= window_height:
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        ball.vx = ball.vel * math.cos(direction)
        vy = ball.vel * math.sin(direction)

        if ball.vy > 0:
            ball.vy = -ball.vy
        if lastTouch == 1 and ball.vx < 0:
            ball.vx = -ball.vx
        if lastTouch == 2 and ball.vx > 0:
            ball.vx = -ball.vx

    #* Bottom
    if ball.y <= 0:
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)

        #* this variable changes the position in the X axis
        ball.vx = ball.vel * math.cos(direction)

        #* This variable changes the position in Y axis
        ball.vy = ball.vel * math.sin(direction)
        if ball.vy < 0:
            ball.vy = -ball.vy
        if lastTouch == 1 and ball.vx < 0:
            ball.vx = -ball.vx
        if lastTouch == 2 and ball.vx > 0:
            ball.vx = -ball.vx

    #* Player 1 paddle contact
    if (ball.y) >= paddle2.y and (ball.y) <= (paddle2.y + 100) and (ball.x - ball.radius) <= (20 + 15):
        lastTouch = 1
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        ball.vx = ball.vel * math.cos(direction)
        ball.vy = ball.vel * math.sin(direction)
        negativeY = randint(0, 1)

        if ball.vx < 0:
            ball.vx = -ball.vx
        if negativeY == 0:
            ball.vy = -ball.vy

        if gameUpgrade == 2 and fillUpgrade == True:
            if fireON == True:
                ball.vel += 1
                fireON = False
        elif gameUpgrade == 3 and fillUpgrade == True:
            if ball.vel < 10:
                ball.vel += 1
        elif gameUpgrade == 4 and fillUpgrade == True:
            if ball.vel < 10:
                ball.vel += 1
        else:
            ball.vel = randint(9, 12)

    #* player 2 paddle contact
    if (ball.y) >= paddle1.y and (ball.y) <= (paddle1.y + 100) and (ball.x + ball.radius) >= (window_width - 40):
        lastTouch = 2
        direction += random.uniform(-0.15 * math.pi, 0.15 * math.pi)
        ball.vx = ball.vel * math.cos(direction)
        ball.vy = ball.vel * math.sin(direction)
        negativeY = randint(0, 1)

        if ball.vx > 0:
            ball.vx = -ball.vx
        if negativeY == 0:
            ball.vy = -ball.vy

        if gameUpgrade == 2 and fillUpgrade == True:
            if fireON == True:
                ball.vel += 1
                fireON = False
        elif gameUpgrade == 3 and fillUpgrade == True:
            if ball.vel < 10:
                ball.vel += 1
        elif gameUpgrade == 4 and fillUpgrade == True:
            if ball.vel < 10:
                ball.vel += 1
        else:
            ball.vel=randint(9, 12)

       
    #* Score
    font = pygame.font.Font(None, 70)

    if score1 >= 7:
        pygame.draw.rect(window, BLACK, (window_width / 2 - 50, window_height / 2 - 50, 120, 100))
        
        font = pygame.font.Font(None, 60)
        winner = font.render("Player 1 Wins!", False, WHITE, BLACK)
        text_rect = winner.get_rect(center = (window_width / 2, window_height / 2))
        window.blit(winner, text_rect)
        pygame.display.update()
        time.sleep(1)
        ball.dt = 0
        paddle1.dt = 0
        paddle2.dt = 0
        
        run1 = True
        pause = False
        resuming = False
        ready = True
        score1 = 0
        score2 = 0
        
    if score2 >= 6:
        pygame.draw.rect(window, BLACK, (window_width / 2 - 50, window_height / 2 - 50, 120, 100))
        font = pygame.font.Font(None, 60)
        winner = font.render("Player 2 Wins!", True, WHITE, BLACK)
        text_rect = winner.get_rect(center = (window_width / 2, window_height / 2))
        window.blit(winner, text_rect)
        pygame.display.update()
        time.sleep(1)
        ball.dt = 0
        paddle1.dt = 0
        paddle2.dt = 0

        run1 = True
        pause = False
        resuming = False
        ready = True
        score1 = 0
        score2 = 0

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    time.sleep(0.01)
    pygame.display.update()
    
    #! --------------------------------- END GAME LOOP STARTS HERE --------------------------------------



    #! Project by Nuno Sousa & Tiago de Pina
