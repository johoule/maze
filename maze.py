# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
NEON_BLUE = (2, 1, 253)

#font
font = pygame.font.Font(None, 48)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None, 150)

#images
img = pygame.image.load('playerArrow.png')

#set stage
stage = 2


# Make a player
player =  [100, 75, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls level 1
wall1 =  [0, 415, 200, 25]
wall2 =  [25, 25, 25, 315]
wall3 =  [50, 315, 153, 25]
wall4 =  [200, 315, 25, 125]
wall5 =  [50, 25, 1125, 25]
wall6 =  [1150, 25, 25, 315]
wall7 =  [997, 315, 153, 25]
wall8 =  [997, 315, 25, 125]
wall9 =  [1000, 415, 200, 25]
wall10 = [0, 485, 200, 25]

#walls level 2


wall65 = [25, 25, 25, 25]


walls_one = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10]
walls_two = [wall65]

# doors
door1 = [600, 500, 25, 300]


# Make coins level 1
coin1 = [50, 50, 25, 25]
coin2 = [300, 0, 25, 25]
coin3 = [600, 0, 25, 25]
coin4 = [900, 0, 25, 25]
coin5 = [1175, 300, 25, 25]
coin6 = [1175, 600, 25, 25]
coin7 = [900, 875, 25, 25]
coin8 = [600, 875, 25, 25]
coin9 = [300, 875, 25, 25]
coin10 = [0, 600, 25, 25]
coin11 = [0, 300, 25, 25]

# make coins level 2
coin14 = [300, 0, 25, 25]
coin15 = [400, 0, 25, 25]
coin16 = [500, 0, 25, 25]

coins_one = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11]
coins_two = [coin14, coin15, coin16]

#levels
level2 = False
level3 = False

#doors
door_stage2 = True
 

# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if stage == 1:
                if event.key == pygame.K_SPACE:
                    stage += 1

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if up:
        player_vy = -player_speed
    elif down:
        player_vy = player_speed
    else:
        player_vy = 0
        
    if left:
        player_vx = -player_speed
    elif right:
        player_vx = player_speed
    else:
        player_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    if stage == 2:
        for w in walls_one:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    elif stage == 3:
        for w in walls_two:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    if stage == 2:
        for w in walls_one:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

    elif stage == 3:
        for w in walls_two:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''
    TOP = player[1]
    BOTTOM = player[1] + player[3]
    LEFT = player[0]
    RIGHT = player[0] + player[2]
    
    if stage == 1 or stage == 2:
        if TOP < 0:
            player[1] = 0
        elif BOTTOM > HEIGHT:
            player[1] = HEIGHT - player[3]

        if LEFT < 0:
            player[0] = 0
        elif RIGHT > WIDTH:
            player[0] = WIDTH - player[2]


    ''' collisios with doors '''
    if stage == 2:
        if door_stage2 == True:
            if intersects.rect_rect(player, door1):
                if player_vy > 0:
                    player[1] = door1[1] - player[3]
            



    ''' get the coins '''
    coins_one = [c for c in coins_one if not intersects.rect_rect(player, c)]
    coins_two = [c for c in coins_two if not intersects.rect_rect(player, c)]
    if stage == 1:
        if len(coins_one) == 0:
            level2 = True
    elif stage == 2:
        if len(coins_two) == 0:
            level3 = True

   

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)

    if stage == 1:
        pygame.draw.rect(screen, NEON_BLUE, [100, 105, 1000, 700])
        welcome = font2.render("WELCOME TO THE", 1, GREEN)
        screen.blit(welcome, [270, 200])
        maze = font3.render("MAZE", 1, GREEN)
        screen.blit(maze, [450, 350])
        space = font.render("HIT THE SPACE BAR TO START", 1, YELLOW)
        screen.blit(space, [300, 600])
        screen.blit(img, [0, 0])
        

    elif stage == 2:
        pygame.draw.rect(screen, GREEN, door1)
        for w in walls_one:
            pygame.draw.rect(screen, RED, w)

        for c in coins_one:
            pygame.draw.rect(screen, YELLOW, c)
        

    elif stage == 3:
        for w in walls_two:
            pygame.draw.rect(screen, GREEN, w)

        for c in coins_two:
            pygame.draw.rect(screen, YELLOW, c)

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
