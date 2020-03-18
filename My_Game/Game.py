#Task 15 (Capstone Project II)
#Programmer:Berto Swanepoel
#This program is to show my mentor what I have read and learned for the reading

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
# This creates the screen and gives it the width and height specified as a 2 item sequence.
screen = pygame.display.set_mode((screen_width,screen_height)) 

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("player.png")
enemy1 = pygame.image.load("enemy1.png")
enemy2 = pygame.image.load("enemy2.png")
enemy3 = pygame.image.load("enemy3.png")
trophy = pygame.image.load("trophy.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
trophy_height = trophy.get_height()
trophy_width = trophy.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 50
playerYPosition = 50
width = 40
height = 60
vel = 1

# Make the enemy start off screen and at a random y position.

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
trophyXPosition =  screen_width
trophyYPosition =  random.randint(0, screen_height - trophy_height)

#Assign keys and give them a boolean value. 

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game's main loop. 
while 1:

# This is a looping structure that will loop the indented code until you tell it to stop.

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. 
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))# This draws the enemy image to the screen at the postion specfied.
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))# This draws the enemy image to the screen at the postion specfied.
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))# This draws the enemy image to the screen at the postion specfied.
    screen.blit(trophy, (trophyXPosition, trophyYPosition))# This draws the trophy image to the screen at the postion specfied.
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

#Now we assign the key functions and change boolean value upon pressing the correct button.

    keys = pygame.key.get_pressed()
    
#When pressing the LEFT button boolean sill be changed to True while others stay False. Player will move LEFT.
    
    if keys[pygame.K_LEFT] and playerXPosition > vel: 
        playerXPosition -= vel
        left = True
        right = False
        up = False
        down = False

#When pressing the RIGHT button boolean sill be changed to True while others stay False. Player will move RIGHT.
        
    elif keys[pygame.K_RIGHT] and playerXPosition < 1030 - vel - width:  
        playerXPosition += vel
        left = False
        right = True
        up = False
        down = False

#When pressing the UP button boolean sill be changed to True while others stay False. Player will move UP.

    elif keys[pygame.K_UP] and playerYPosition > vel:  
        playerYPosition -= vel
        left = False
        right = False
        up = True
        down = False

#When pressing the DOWN button boolean sill be changed to True while others stay False. Player will move DOWN.

    elif keys[pygame.K_DOWN] and playerYPosition < 650 - vel - width:  
        playerYPosition += vel
        left = False
        right = False
        up = False
        down = True
            
# After events are checked for in the for loop above and values are set,
# check key pressed values and move player accordingly.
    
# The coordinate system of the game window(screen) is that the top left corner is (0, 0).
# This means that if you want the player to move down you will have to increase the y or x position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerXPosition += 1
    
# Check for collision of the enemy with the player.
# To do this we need bounding boxes around the images of the player and enemy.
# We then need to test if these boxes intersect. If they do then there is a collision.
    
# Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
# The following updates the playerBox position to the player's position,
# in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
# Bounding box for the enemy:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    trophyBox = pygame.Rect(trophy.get_rect())
    trophyBox.top = trophyYPosition
    trophyBox.left = trophyXPosition
    
# Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
    
# Display losing status to the user: 
        
        print("You lose!")
       
# Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
# If the enemy is off the screen the user wins the game:
    
    if playerBox.colliderect(trophyBox):
    
# Display wining status to the user: 

        
        print("You win!")
        
        
# Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
# Make enemy approach the player.
    
    enemy1XPosition -= 0.18
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.12
    trophyXPosition -= 0.10
    
# ================The game loop logic ends here. =============
  
