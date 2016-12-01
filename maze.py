# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()

# here is a comment

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
    #img = pygame.image.load('playerArrow.png')

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
wall3 =  [50, 315, 150, 25]
wall4 =  [175, 315, 25, 125]
wall5 =  [50, 25, 1125, 25]
wall6 =  [1150, 25, 25, 315]
wall7 =  [997, 315, 153, 25]
wall8 =  [997, 315, 25, 125]
wall9 =  [1000, 415, 200, 25]
wall10 = [0, 500, 200, 25]
wall11 = [1000, 500, 200, 25]
wall12 = [200, 500, 25, 125]
wall13 = [50, 625, 175, 25]
wall14 = [25, 625, 25, 250]
wall15 = [50, 850, 1125, 25]
wall16 = [1150, 625, 25, 225]
wall17 = [1000, 625, 150, 25]
wall18 = [1000, 500, 25, 125]

wall19 = [100, 80, 100, 100]
wall20 = [100, 225, 100, 50]
wall21 = [250, 80, 200, 100]

wall22 = [500, 50, 25, 130]
wall23 = [250, 225, 25, 217]
wall24 = [275, 321, 175, 25]
wall25 = [350, 225, 350, 25]
wall26 = [500, 250, 25, 100]
wall27 = [575, 80, 300, 100]
wall28 = [925, 80, 175, 100]

wall29 = [925, 230, 175, 50]

wall30 = [500, 500, 200, 25]
wall31 = [500, 400, 25, 100]
wall32 = [675, 400, 25, 100]
wall33 = [593, 400, 25, 100]



#walls level 2
wall60 = [25, 25, 1150, 25]      #these lines are the borders
wall61 = [1150, 50, 25, 825]     #  
wall62 = [25, 50, 25, 825]       #
wall63 = [50, 850, 1100, 25]     #

wall64 = [50, 200, 25, 25]       #figure 2
wall65 = [75, 125, 25, 100]
wall66 = [100, 125, 75, 25]
wall67 = [150, 75, 25, 50]
wall68 = [75, 75, 75, 25]

wall69 = [50, 400, 25, 25]      #figure 3
wall70 = [75, 250, 25, 175]
wall71 = [100, 250, 25, 25]
wall72 = [125, 175, 25, 100]
wall73 = [150, 175, 50, 25]
wall74 = [200, 75, 25, 125]
wall75 = [225, 75, 75, 25]
wall76 = [275, 100, 25, 100]
wall77 = [250, 175, 25, 25]
wall78 = [225, 125, 25, 25]

wall79 = [325, 50, 25, 200]    #figure 4
wall80 = [175, 225, 150, 25]
wall81 = [175, 250, 25, 150]
wall82 = [200, 375, 75, 25]

walls_one = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33]
walls_two = [wall60, wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68,
             wall69, wall70, wall71, wall72, wall73, wall74, wall75, wall76,
             wall77, wall78, wall79, wall80, wall81, wall82]

# doors
door1 = [900, 800, 25, 300]


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
door_stage1 = True
 

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
            if stage == 0:
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
    if stage == 1:
        for w in walls_one:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    elif stage == 2:
        for w in walls_two:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    if stage == 1:
        for w in walls_one:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

    elif stage == 2:
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
    
    if stage == 0 or stage == 1:
        if TOP < 0:
            player[1] = 0
        elif BOTTOM > HEIGHT:
            player[1] = HEIGHT - player[3]

        if LEFT < 0:
            player[0] = WIDTH - player[2]
        elif RIGHT > WIDTH:
            player[0] = 0


    ''' collisios with doors '''
    if stage == 1:
        if door_stage1 == True:
            if intersects.rect_rect(player, door1):
                if player_vy > 0:
                    player[1] = door1[1] - player[3]
            



    ''' get the coins '''
    coins_one = [c for c in coins_one if not intersects.rect_rect(player, c)]
    coins_two = [c for c in coins_two if not intersects.rect_rect(player, c)]
    if stage == 1:
        if len(coins_one) == 0:
            door_stage1 = False
    elif stage == 2:
        if len(coins_two) == 0:
            level3 = True

   

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    

    if stage == 0:
        
        pygame.draw.rect(screen, NEON_BLUE, [100, 105, 1000, 700])
        welcome = font2.render("WELCOME TO THE", 1, GREEN)
        screen.blit(welcome, [270, 200])
        maze = font3.render("MAZE", 1, GREEN)
        screen.blit(maze, [450, 350])
        space = font.render("HIT THE SPACE BAR TO START", 1, YELLOW)
        screen.blit(space, [300, 600])
        
        

    elif stage == 1:
        pygame.draw.rect(screen, WHITE, player)
        #pygame.draw.rect(screen, GREEN, door1)
        for w in walls_one:
            pygame.draw.rect(screen, RED, w)

        for c in coins_one:
            pygame.draw.rect(screen, YELLOW, c)
        

    elif stage == 2:
        pygame.draw.rect(screen, WHITE, player)
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
