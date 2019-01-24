from pygame import * 
import os
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 40)
init()
size = width, height = 600, 500
screen = display.set_mode(size)


# defining colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (119, 0, 30)  #background
LIGHTPINK = (176, 86, 106) #buttons
LIGHTYELLOW = (255, 233, 157) #dots
DARKYELLOW = (246, 205, 128)
GREEN = (0, 255, 0)
GREY = (220, 219, 219)
DARKGREY = (170, 169, 169)

#font
font1 = font.SysFont("Arial Black",50) 
font2 = font.SysFont("Arial Black",30) 


# states
MENUSTATE = 0
GAMESTATE = 1
QUITSTATE = 2


#movment of the character
KEY_DOWN = False
KEY_UP = False

#put this outside the main loop
def introAnimation():
    screen.fill((BLACK))
    draw.rect(screen, GREY, (0, 50, 600, 400))
    title1 = "click up and down to jump"
    title2 = "the adventure of"
    title3 = "BIRDS"
    title4 = "ESCAPING"
    
    #animation of title 1
    type_title1 = font2.render(title1, True, WHITE)
    for x in range (0,600):
        screen.blit(type_title1, (x,180,400,100))
        time.wait(4)
        display.flip()
        draw.rect(screen, GREY,(0, 50, 600, 400))
        if x==600:
            break
        
    #animation of title 2
    type_title2 = font1.render(title2, True, WHITE)
    x=0
    for x in range (0,600):
        screen.blit(type_title2, (x,200,400,100))
        time.wait(2)
        display.flip()
        draw.rect(screen, GREY, (0, 50, 600, 400))
        if x==600:
            break
        
    #animation of title 3
    type_title3 = font1.render(title3, True, WHITE)
    x=0
    for x in range (0,600):
        screen.blit(type_title3, (x,210,400,100))
        time.wait(1)
        display.flip()
        draw.rect(screen, GREY, (0, 50, 600, 400))
        if x==600:
            break
        
    #animation of title 4
    type_title4 = font1.render(title4, True, WHITE)
    x=0
    for x in range (0,600):
        screen.blit(type_title4, (x,240,400,100))
        time.wait(1)
        display.flip()
        draw.rect(screen, GREY, (0, 50, 600, 400)) 
        if x==600:
            break
        
    #display the title    
    screen.fill((BLACK))
    draw.rect(screen, GREY, (0, 50, 600, 400))         
    type_title3 = font1.render(title3, True, WHITE)
    type_title4 = font1.render(title4, True, WHITE)
    screen.blit(type_title3, (220,180,400,100))
    screen.blit(type_title4, (160,230,400,100))
    display.flip()
    time.wait(2000)




def displayMenu(button, mouseX, mouseY):
    st = MENUSTATE
    #display menu
    screen.fill((BLACK))
    draw.rect(screen, GREY, (0, 50, 600, 400))

    # start button
    playRect = Rect(width//4, height//4, width//2, height//8)
    draw.rect(screen, DARKGREY, playRect)
    
    # Creating text
    string = "START"    
    playText = font1.render(string, 1, WHITE)
    playSize = font1.size(string)
    # centering the text in the box
    playTitleRect = Rect(width//4 + (width//2 - playSize[0])//2, height//4 + (height//8 - playSize[1])//2, playSize[0], playSize[1])
    screen.blit(playText, playTitleRect)  # will put text on screen

    # for displaying the quit game box
    quitRect = Rect(width//4, height//2, width//2, height//8)
    draw.rect(screen, DARKGREY, quitRect)
    # Creating text
    string = "QUIT"
    quitText = font1.render(string, 1, WHITE)
    quitSize = font1.size(string)
    quitTitleRect = Rect(width//4 + (width//2 - quitSize[0])//2, height//2 + (height//8 - quitSize[1])//2, quitSize[0], quitSize[1])
    screen.blit(quitText, quitTitleRect)

    # check if button 1 has been pushed
    if button == 1:
        # checking if clicked in the play box
        if playRect.collidepoint(mouseX, mouseY) == True:
            st = GAMESTATE  # change the state
        # checking if clicked in the quit box
        elif quitRect.collidepoint(mouseX, mouseY) == True:
            st = QUITSTATE # change the state
            
    display.flip()
    return st  # return the state




def drawGame(cy, button, bx, by):
    st = GAMESTATE # in drawGame, must be GAMESTATE
    screen.fill((BLACK))
    draw.rect(screen, GREY, (0, 50, 600, 400))
    
    #character
    draw.rect(screen, WHITE, (300, cy ,20 ,20))
    #barrier
    draw.rect(screen, BLACK,(bx, 50, 40, by))
    draw.rect(screen, BLACK,(bx, (by+50+150), 40, (450-50-150-by)))

 
    display.flip()    
    return st #return the state




running = True # boolean to control game loop
myClock = time.Clock()
state = MENUSTATE # start from the menu state
button = mx = my = 0 # initialize button, and mouse x and y
charactery = 415 #the position of y
barrierx = 600 #start poosition of the barrier
barriery = random.randint(0,300) #randomly generate the height of the barrier



# Game Loop
#introAnimation()
while running: # do as long as running is true
    for evnt in event.get():             # checks all events that happen
        if evnt.type == QUIT: #check if X has been clicked on screen
            running = False # set boolean to False will quit loop
        if evnt.type == MOUSEBUTTONDOWN: # check if button pressed 
            mx, my = evnt.pos    # grab the mouse x and y      
            button = evnt.button # grab the button that was pressed
        if evnt.type == KEYDOWN:
            if evnt.key == K_DOWN:
                KEY_DOWN = True
            if evnt.key == K_UP:
                KEY_UP = True
        if evnt.type ==KEYUP:
            #if evnt.key == K_DOWN:
                #KEY_DOWN = False    #comment out to create gravity
            if evnt.key == K_UP:
                KEY_UP = False
                
                
    if state == MENUSTATE: # if on the menu
        state = displayMenu(button, mx, my) # draw menu
        if state == GAMESTATE:
            charactery = 250 #reset the position of the character
            
            
    elif state == GAMESTATE: # if on the game screen
        state = drawGame(charactery, button, barrierx, barriery)
        dis1 = charactery - 50 - barriery
        dis2 = barriery + 50 + 150 - charactery - 20
        if dis1 < 0 and barrierx <=310 and barrierx >=270:
            running = False
            #print (dis1)
            #print ("1")
        if dis2 < 0 and barrierx <=310 and barrierx >=270:
            running = False
            #print (dis2)
            #print ("2")
        if barrierx <= 600:
            barrierx -= 1
        if barrierx == 0:
            barrierx = 600
        if KEY_DOWN == True:
            charactery += 2
        if KEY_UP == True:
            charactery -= 7

    else: # check for an error
        running = False
    myClock.tick(60)                     # 60 fps
    button = 0 # resetting button to 0 every time through the loop
    

    
quit()