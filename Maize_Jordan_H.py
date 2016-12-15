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
TITLE = "Welcome To The Maize"
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
font4 = pygame.font.Font(None, 35)

#images
img = pygame.image.load('cornmaze.png')
img2 = pygame.image.load('fireworks.png')
img3 = pygame.image.load('youtried.png')

#set stage
stage = 1

#time for stage 2
seconds = 2 * 60
ticks = 0


# Make a player
player =  [600, 400, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

player2 = [575, 400, 25, 25]
player2_vx = 0
player2_vy = 0
player2_speed = 5

player3 = [700, 400, 25, 25]
player3_vx = 0
player3_vy = 0
player_speed = 5

# make walls level 1
wall1 = [0, 50, 1200, 25]  # y = 50

wall2 = [0, 75, 25, 250]  # y = 75
wall3 = [575, 75, 50, 100]
wall4 = [1175, 75, 25, 250]

wall5 = [50, 100, 225, 25]  # y = 100
wall6 = [325, 100, 225, 25]
wall7 = [650, 100, 225, 25]
wall8 = [925, 100, 225, 25]

wall9 = [50, 125, 25, 50] # y = 125
wall10 = [250, 125, 25, 50]
wall11 = [325, 125, 25, 50]
wall12 = [525, 125, 25, 50]
wall13 = [650, 125, 25, 50]
wall14 = [850, 125, 25, 50]
wall15 = [925, 125, 25, 50]
wall16 = [1125, 125, 25, 50]

wall17 = [75, 150, 175, 25] # y = 150
wall18 = [325, 150, 200, 25]
wall19 = [675, 150, 200, 25]
wall20 = [950, 150, 175, 25]

wall21 = [50, 200, 225, 25]  # y = 200
wall22 = [325, 200, 25, 175]
wall23 = [400, 200, 400, 25]
wall24 = [850, 200, 25, 175]
wall25 = [925, 200, 225, 25]

                            
wall27 = [575, 225, 50, 75]  # y = 225
wall074 = [50, 225, 25, 50]
wall075 = [250, 225, 25, 50]
wall076 = [925, 225, 25, 50]
wall077 = [1125, 225, 25, 50]

wall078 = [75, 250, 175, 25]  # y = 250
wall079 = [950, 250, 175, 25]

wall30 = [350, 275, 175, 50] # y = 275
wall31 = [675, 275, 175, 50]


wall26 = [25, 300, 250, 25]  # y = 300
wall28 = [925, 300, 250, 25]

wall29 = [250, 325, 25, 50] # y = 325
wall32 = [925, 325, 25, 50]

wall33 = [0, 350, 250, 25]  # y = 350
wall34 = [500, 425, 225, 25] #****
wall35 = [475, 375, 25, 75]# 
wall36 = [550, 375, 25, 50]#
wall37 = [625, 375, 25, 50]#
wall39 = [700, 375, 25, 50]
wall40 = [925, 350, 275, 25]

wall41 = [0, 450, 275, 25]  # y = 450
wall42 = [325, 450, 100, 25]
wall43 = [775, 450, 100, 25]
wall44 = [925, 450, 275, 25]

wall45 = [250, 475, 25, 50]  # y = 475
wall46 = [325, 475, 25, 50]
wall47 = [400, 475, 25, 50]
wall48 = [775, 475, 25, 50]
wall49 = [850, 475, 25, 50]
wall50 = [925, 475, 25, 50]

wall51 = [475, 500, 250, 25]  # y = 500

wall52 = [0, 500, 250, 25]#  # y = 550
wall53 = [350, 500, 50, 25]#
wall55 = [800, 500, 50, 25]#
wall56 = [950, 500, 250, 25]#

wall57 = [0, 525, 25, 350]#    #y = 575
wall58 = [1175, 525, 25, 350]#

wall59 = [50, 550, 225, 25]  # figure 1
wall060 = [50, 575, 25, 50]
wall061 = [250, 575, 25, 50]
wall062 = [75, 600, 175, 25]

wall063 = [25, 650, 150, 25]  # figure 2
wall064 = [150, 675, 25, 75]
wall065 = [25, 725, 125, 25]

wall066 = [225, 650, 50, 100] # figure 3

wall067 = [50, 775, 225, 25] # figure 4
wall068 = [50, 800, 25, 50]
wall069 = [250, 800, 25, 50]
wall070 = [75, 825, 175, 25]

wall071 = [325, 575, 175, 25]  # figure 5
wall072 = [325, 600, 25, 75]
wall073 = [475, 600, 25, 75]
wall54 = [350, 650, 125, 25]

wall38 = [325, 700, 100, 25]  # figure 6

wall080 = [325, 775, 175, 25]  # figure 7
wall081 = [325, 800, 25, 50]
wall082 = [475, 800, 25, 50]
wall083 = [350, 825, 125, 25]

wall084 = [550, 575, 100, 25] # figure 8
wall085 = [550, 600, 25, 75]
wall086 = [625, 600, 25, 75]
wall087 = [575, 650, 50, 25]

wall088 = [450, 725, 300, 25]


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

wall79 = [275, 200, 25, 50]    #figure 4
wall80 = [325, 75,  25, 200]
wall81 = [350, 200, 150, 25]
wall82 = [475, 75, 25, 125]
wall83 = [375, 75, 100, 25]
wall84 = [375, 100, 25, 75]
wall85 = [400, 150, 50, 25]
wall86 = [425, 125, 25, 25]

wall93 = [50, 450, 150, 25]    #figure 5
wall94 = [175, 400, 25, 50]
wall95 = [125, 400, 50, 25]

wall96 = [175, 200, 25, 125] # figure 6 .....
wall97 = [200, 300, 100, 25]
wall98 = [275, 275, 75, 25]
wall99 = [225, 225, 25, 75]

wall100 = [125, 300, 25, 75] # figure 7
wall101 = [150, 350, 175, 25]
wall102 = [325, 325, 25, 100]
wall103 = [275, 400, 50, 25]
wall104 = [225, 375, 25, 250]
wall105 = [75, 500, 150, 25]
wall106 = [125, 600, 125, 25]
wall107 = [125, 550, 25, 50]
wall108 = [150, 550, 50, 25]
wall109 = [75, 525, 25, 150]
wall110 = [100, 650, 275, 25]
wall111 = [375, 250, 25, 575]
wall112 = [275, 450, 100, 25]
wall113 = [275, 475, 25, 150]
wall114 = [300, 600, 50, 25]
wall115 = [325, 500, 25, 100]
wall116 = [225, 800, 150, 25]
wall117 = [175, 750, 25, 100]
wall118 = [200, 750, 150, 25]
wall119 = [325, 700, 25, 50]
wall120 = [75, 700, 250, 25]
wall121 = [75, 725, 25, 100]
wall122 = [125, 750, 25, 100]

wall123 = [550, 375, 25, 125] # center figure (starting and ending point)
wall124 = [625, 400, 25, 100]
wall125 = [575, 425, 50, 25]
wall126 = [575, 475, 25, 25]

wall127 = [400, 250, 300, 25] # figure 9

wall133 = [425, 300, 25, 525] # figure 10
wall134 = [450, 800, 475, 25]
wall135 = [950, 800, 25, 50]
wall136 = [975, 800, 50, 25]
wall137 = [1000, 750, 25, 50]
wall138 = [1025, 750, 100, 25]
wall139 = [1100, 775, 25, 50]
wall140 = [1050, 800, 50, 25]
wall141 = [525, 750, 25, 50]
wall142 = [550, 750, 50, 25]
wall143 = [475, 700, 25, 75]
wall144 = [500, 700, 150, 25]
wall145 = [625, 725, 25, 50]
wall146 = [650, 750, 325, 25]
wall147 = [950, 700, 25, 50]
wall148 = [975, 700, 150, 25]
wall149 = [900, 775, 25, 25]
wall150 = [1100, 450, 25, 250]
wall151 = [1050, 550, 50, 25]
wall152 = [1050, 575, 25, 100]
wall153 = [900, 450, 200, 25] #....

wall158 = [450, 600, 100, 25]  #figure 11
wall159 = [475, 625, 25, 50]
wall160 = [525, 650, 25, 50]
wall161 = [525, 550, 25, 50]
wall162 = [550, 550, 425, 25]
wall163 = [625, 500, 25, 50]
wall164 = [575, 525, 25, 25]
wall165 = [525, 525, 25, 25]
wall166 = [650, 500, 425, 25]
wall167 = [1000, 525, 25, 150]
wall168 = [725, 650, 275, 25]  
wall169 = [575, 650, 125, 25]
wall170 = [675, 675, 25, 50]
wall171 = [700, 700, 225, 25]
wall172 = [900, 675, 25, 25]
wall173 = [575, 600, 25, 50]
wall174 = [600, 600, 375, 25]

wall175 = [600, 375, 50, 25] #random figure i made up to correct for adding center figure
wall176 = [475, 475, 75, 25]
wall177 = [475, 500, 25, 75]
wall178 = [450, 425, 75, 25]
wall179 = [475, 375, 75, 25]

wall180 = [850, 400, 300, 25]
wall181 = [850, 425, 25, 50]
wall182 = [675, 450, 175, 25]
wall183 = [675, 325, 25, 125]
wall184 = [475, 325, 200, 25]
wall185 = [475, 275, 25, 25]
wall186 = [525, 300, 25, 25]
wall187 = [575, 275, 25, 25]
wall188 = [625, 300, 25, 25]
wall189 = [675, 275, 25, 25]

wall190 = [1000, 75, 125, 25]
wall191 = [1000, 100, 25, 150]
wall192 = [1050, 125, 100, 25]
wall193 = [725, 250, 300, 25]
wall194 = [725, 275, 25, 150]
wall195 = [750, 400, 75, 25]
wall196 = [800, 350, 25, 50]
wall197 = [825, 350, 300, 25]
wall198 = [1100, 175, 25, 175]
wall199 = [1050, 175, 50, 25]
wall200 = [1050, 200, 25, 125]
wall201 = [775, 300, 275, 25]
wall202 = [775, 350, 25, 25]
wall203 = [525, 50, 25, 200]
wall204 = [550, 125, 450, 25]
wall205 = [575, 50, 25, 50]
wall206 = [625, 75, 25, 150]
wall207 = [675, 50, 25, 50]
wall208 = [725, 75, 25, 150]
wall209 = [775, 50, 25, 50]
wall210 = [825, 75, 25, 150]
wall211 = [875, 50, 25, 50]
wall212 = [925, 75, 25, 150]
wall213 = [975, 75, 25, 25]
wall214 = [575, 175, 25, 75]
wall215 = [675, 175, 25, 75]
wall216 = [775, 175, 25, 75]
wall217 = [875, 175, 25, 75]
wall218 = [975, 175, 25, 25]
wall219 = [975, 225, 25, 25]





walls_one = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9,
             wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17,
             wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25,
             wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33,
             wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41,
             wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49,
             wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57,
             wall58, wall59, wall060, wall061, wall062, wall063, wall064,
             wall065, wall066, wall067, wall068, wall069, wall070, wall071,
             wall072, wall073, wall074, wall075, wall076, wall077, wall078,
             wall079, wall080, wall081, wall082, wall083, wall084, wall085,
             wall086, wall087]
walls_two = [wall60, wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68,
             wall69, wall70, wall71, wall72, wall73, wall74, wall75, wall76,
             wall77, wall78, wall79, wall80, wall81, wall82, wall83, wall84,
             wall85, wall86, wall93, wall94, wall95, wall96, wall97, wall98,
             wall99, wall100, wall101, wall102, wall103, wall104, wall105,
             wall106, wall107, wall108, wall109, wall110, wall111, wall112,
             wall113, wall114, wall115, wall116, wall117, wall118, wall119,
             wall120, wall121, wall122, wall123, wall124, wall125, wall126,
             wall127, wall133, wall134, wall135, wall136, wall137, wall138,
             wall139, wall140, wall141, wall142, wall143, wall144, wall145,
             wall146, wall147, wall148, wall149, wall150, wall151, wall152,
             wall153, wall158, wall159, wall160, wall161, wall162, wall163,
             wall164, wall165, wall166, wall167, wall168, wall169, wall170,
             wall171, wall172, wall173, wall174, wall175, wall176, wall177,
             wall178, wall179, wall180, wall181, wall182, wall183, wall184,
             wall185, wall186, wall187, wall188, wall189, wall190, wall191,
             wall192, wall193, wall194, wall195, wall196, wall197, wall198,
             wall199, wall200, wall201, wall202, wall203, wall204, wall205,
             wall206, wall207, wall208, wall209, wall210, wall211, wall212,
             wall213, wall214, wall215, wall216, wall217, wall218, wall219]

# doors
door1 = [900, 800, 25, 300]

door2 = [600, 475, 25, 25]


#teleporters

teleport2 = [575, 450, 25, 25]


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
coin70 = [75, 50 ,25, 25]   #  y = 25
coin71 = [250, 50, 25, 25]
coin72 = [375, 50, 25, 25]
coin73 = [450, 50, 25, 25]
coin74 = [550, 50, 25, 25]
coin75 = [600, 50, 25, 25]
coin76 = [700, 50, 25, 25]
coin77 = [800, 50, 25, 25]
coin78 = [900, 50, 25, 25]
coin79 = [1000, 50, 25, 25]
coin80 = [1075, 50, 25, 25]

coin81 = [125, 100, 25, 25]  # y = 100
coin82 = [225, 100, 25, 25]
coin83 = [350, 100, 25, 25]
coin84 = [425, 100, 25, 25]
coin85 = [500, 100, 25, 25]
coin86 = [575, 100, 25, 25]
coin87 = [650, 100, 25, 25]
coin88 = [750, 100, 25, 25]
coin89 = [850, 100, 25, 25]
coin90 = [975, 100, 25, 25]
coin91 = [1100, 100, 25, 25]

coin92 = [300, 125, 25, 25]  # y = 125
coin93 = [400, 125, 25, 25]

coin94 = [150, 150, 25, 25] # y = 150
coin95 = [550, 150, 25, 25]
coin96 = [700, 150, 25, 25]
coin97 = [800, 150, 25, 25]
coin98 = [900, 150, 25, 25]
coin99 = [975, 150, 25, 25]
coin100 = [1050, 150, 25, 25]

coin101 = [50, 175, 25, 25]  #y = 175
coin102 = [450, 175, 25, 25]
coin103 = [500, 175, 25, 25]
coin104 = [650, 175, 25, 25]
coin105 = [750, 175, 25, 25]

coin106 = [100, 200, 25, 25]  # y = 200
coin107 = [150, 200, 25, 25]
coin108 = [300, 200, 25, 25]
coin109 = [600, 200, 25, 25]
coin110 = [850, 200, 25, 25]
coin111 = [975, 200, 25, 25]
coin112 = [1075, 200, 25, 25]

coin113 = [400, 225, 25, 25]  # y = 225
coin114 = [475, 225, 25, 25]
coin115 = [550, 225, 25, 25]
coin116 = [650, 225, 25, 25]
coin117 = [725, 225, 25, 25]
coin118 = [800, 225, 25, 25]
coin119 = [1125, 225, 25, 25]

coin120 = [350, 250, 25, 25]  # y = 250

coin121 = [200, 275, 25, 25]  # y = 275
coin122 = [250, 275, 25, 25]
coin123 = [450, 275, 25, 25]
coin124 = [550, 275, 25, 25]
coin125 = [650, 275, 25, 25]
coin126 = [825, 275, 25, 25]
coin127 = [925, 275, 25, 25]
coin128 = [1075, 275, 25, 25]

coin129 = [50, 300, 25, 25]  # y = 300
coin130 = [500, 300, 25, 25]
coin131 = [600, 300, 25, 25]

coin132 = [100, 325, 25, 25] # y = 325
coin133 = [150, 325, 25, 25]
coin134 = [300, 325, 25, 25]
coin135 = [900, 325, 25, 25]
coin136 = [1125, 325, 25, 25]

coin137 = [350, 350, 25, 25]  # y = 350
coin138 = [400, 350, 25, 25]
coin139 = [550, 350, 25, 25]

coin140 = [50, 375, 25, 25] # y = 375
coin141 = [300, 375, 25, 25]
coin142 = [700, 375, 25, 25]
coin143 = [775, 375, 25, 25]
coin144 = [850, 375, 25, 25]
coin145 = [975, 375, 25, 25]
coin146 = [1075, 375, 25, 25]

coin147 = [450, 400, 25, 25] # y = 400

coin148 = [50, 425, 25, 25] # y = 425
coin149 = [150, 425, 25, 25]
coin150 = [350, 425, 25, 25]
coin151 = [650, 425, 25, 25]
coin152 = [750, 425, 25, 25]
coin153 = [1000, 425, 25, 25]

coin154 = [500, 450, 25, 25] # y = 450

coin155 = [700, 475, 25, 25]  # y = 475
coin156 = [825, 475, 25, 25]
coin157 = [975, 475, 25, 25]
coin158 = [1125, 475, 25, 25]

coin159 = [50, 500, 25, 25]  # y = 500
coin160 = [250, 500, 25, 25]
coin161 = [400, 500, 25, 25]

coin162 = [350, 525, 25, 25]  # y = 525
coin163 = [550, 525, 25, 25]
coin164 = [600, 525, 25, 25]
coin165 = [650, 525, 25, 25]
coin166 = [850, 525, 25, 25]
coin167 = [1050, 525, 25, 25]

coin168 = [150, 575, 25, 25] # y = 575
coin169 = [300, 575, 25, 25]
coin170 = [475, 575, 25, 25]
coin171 = [625, 575, 25, 25]
coin172 = [750, 575, 25, 25]
coin173 = [875, 575, 25, 25]
coin174 = [1075, 575, 25, 25]

coin175 = [975, 600, 25, 25]  # y = 600
coin176 = [1025, 600, 25, 25]

coin177 = [200, 625, 25, 25]  # y = 625
coin178 = [350, 625, 25, 25]
coin179 = [450, 625, 25, 25]
coin180 = [525, 625, 25, 25]
coin181 = [600, 625, 25, 25]
coin182 = [825, 625, 25, 25]
coin183 = [1125, 625, 25, 25]

coin184 = [125, 675, 25, 25]  # y = 675
coin185 = [275, 675, 25, 25]
coin186 = [500, 675, 25, 25]
coin187 = [750, 675, 25, 25]
coin188 = [875, 675, 25, 25]
coin189 = [950, 675, 25, 25]
coin190 = [1050, 675, 25, 25]

coin191 = [400, 700, 25, 25] # y = 700

coin192 = [125, 725, 25, 25]  # y = 725
coin193 = [300, 725, 25, 25]
coin194 = [500, 725, 25, 25]
coin195 = [725, 725, 25, 25]

coin196 = [450, 750, 25, 25]  # y = 750
coin197 = [600, 750, 25, 25]

coin198 = [50, 775, 25, 25]  # y = 775
coin199 = [225, 775, 25, 25]
coin200 = [550, 775, 25, 25]
coin201 = [775, 775, 25, 25]
coin202 = [875, 775, 25, 25]
coin203 = [1075, 775, 25, 25]

coin204 = [150, 825, 25, 25]  # y = 825
coin205 = [300, 825, 25, 25]
coin206 = [500, 825, 25, 25]
coin207 = [675, 825, 25, 25]
coin208 = [850, 825, 25, 25]
coin209 = [975, 825, 25, 25]
coin210 = [1125, 825, 25, 25]

# coins level 3

coins_one = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11]
coins_two = [coin70, coin71, coin72, coin73, coin74, coin75, coin76, coin77,
             coin78, coin79, coin80, coin81, coin82, coin83, coin84, coin85,
             coin86, coin87, coin88, coin89, coin90, coin91, coin92, coin93,
             coin94, coin95, coin96, coin97, coin98, coin99, coin100, coin101,
             coin102, coin103, coin104, coin105, coin106, coin107, coin108,
             coin109, coin110, coin111, coin112, coin113, coin114, coin115,
             coin116, coin117, coin118, coin119, coin120, coin121, coin122,
             coin123, coin124, coin125, coin126, coin127, coin128, coin129,
             coin130, coin131, coin132, coin133, coin134, coin135, coin136,
             coin137, coin138, coin139, coin140, coin141, coin142, coin143,
             coin144, coin145, coin146, coin147, coin148, coin149, coin150,
             coin151, coin152, coin153, coin154, coin155, coin156, coin157,
             coin158, coin159, coin160, coin161, coin162, coin163, coin164,
             coin165, coin166, coin167, coin168, coin169, coin170, coin171,
             coin172, coin173, coin174, coin175, coin176, coin177, coin178,
             coin179, coin180, coin181, coin182, coin183, coin184, coin185,
             coin186, coin187, coin188, coin189, coin190, coin191, coin192,
             coin193, coin194, coin195, coin196, coin197, coin198, coin199,
             coin200, coin201, coin202, coin203, coin204, coin205, coin206,
             coin207, coin208, coin209, coin210]

#levels
level2 = False
level3 = False

#doors
door_stage1 = True
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
            if stage == 0:
                if event.key == pygame.K_SPACE:
                    stage += 1

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    a = pressed[pygame.K_a]
    d = pressed[pygame.K_d]
    w = pressed[pygame.K_w]
    s = pressed[pygame.K_s]

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

    if a:
        player2_vx = -player2_speed
    elif d:
        player2_vx = player2_speed
    else:
        player2_vx = 0

    if w:
        player2_vy = -player2_speed
    elif s:
        player2_vy = player2_speed
    else:
        player2_vy = 0
    

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx
    player2[0] += player2_vx

    ''' resolve collisions horizontally '''
    if stage == 1:
        for w in walls_one:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]
        for w in walls_one:
            if intersects.rect_rect(player2, w):
                if player2_vx > 0:
                    player2[0] = w[0] - player2[2]
                elif player2_vx < 0:
                    player2[0] = w[0] + w[2]

    elif stage == 2 or stage == 3:
        for w in walls_two:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    

    ''' move the player in vertical direction '''
    player[1] += player_vy
    player2[1] += player2_vy
    
    ''' resolve collisions vertically '''
    if stage == 1:
        for w in walls_one:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]
        for w in walls_one:
            if intersects.rect_rect(player2, w):
                if player2_vy > 0:
                    player2[1] = w[1] - player2[3]
                elif player2_vy < 0:
                    player2[1] = w[1] + w[3]
                    

    elif stage == 2 or stage == 3:
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

    TOP2 = player2[1]
    BOTTOM2 = player2[1] + player2[3]
    LEFT2 = player2[0]
    RIGHT2 = player2[0] + player2[2]
    
    if stage == 0 or stage == 1:
        if TOP < 0:
            player[1] = 0
        elif BOTTOM > HEIGHT:
            player[1] = HEIGHT - player[3]

        if LEFT < 0:
            player[0] = WIDTH - player[2]
        elif RIGHT > WIDTH:
            player[0] = 0

        if LEFT2 < 0:
            player2[0] = WIDTH - player2[2]
        elif RIGHT2 > WIDTH:
            player2[0] = 0


    ''' collisios with doors '''
    if stage == 1:
        if door_stage1 == True:
            if intersects.rect_rect(player, door1):
                if player_vy > 0:
                    player[1] = door1[1] - player[3]
        if door_stage1 == True:
            if intersects.rect_rect(player2, door1):
                if player2_vy > 0:
                    player2[1] = door1[1] - player2[3]
    elif stage == 2:
        if door_stage2 == True:
            if intersects.rect_rect(player, door2):
                if player_vy < 0:
                    player[1] = door2[1] + player[3]


    ''' collisions with teleporters '''
    if stage == 2:
        if intersects.rect_rect(player, teleport2):
            if player_vx < 0:
                stage += 1
            



    ''' get the coins '''
    coins_one = [c for c in coins_one if not intersects.rect_rect(player, c)]
    coins_two = [c for c in coins_two if not intersects.rect_rect(player, c)]
    if stage == 1:
        if len(coins_one) == 0:
            door_stage1 = False
    elif stage == 2:
        if len(coins_two) == 0:
            door_stage2 = False

   
    ''' timer '''
    if stage == 2:
        ticks += 1
        m = seconds // 60
        s = seconds % 60
        
        if ticks == 60:
            seconds -= 1
            ticks = 0

        if m < 0:
            stage = 6


        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    level = font.render("LEVEL = " + str(stage), 1, WHITE)
    level2 = font4.render("LEVEL = " + str(stage), 1, WHITE)
    

    if stage == 0:
        
        #pygame.draw.rect(screen, NEON_BLUE, [100, 105, 1000, 700])
        screen.blit(img, [0, 0])
        welcome = font2.render("WELCOME TO THE MAIZE", 1, WHITE)
        screen.blit(welcome, [150, 800])
        level = font.render("LEVEL = " + str(stage), 1, WHITE)
        space = font.render("HIT THE SPACE BAR TO START", 1, GREEN)
        screen.blit(space, [350, 860])
        
        

    elif stage == 1:
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, NEON_BLUE, player2)
        
        screen.blit(level, [100, 5])
        #pygame.draw.rect(screen, GREEN, door1)
        for w in walls_one:
            pygame.draw.rect(screen, RED, w)

        for c in coins_one:
            pygame.draw.rect(screen, YELLOW, c)
        

    elif stage == 2:
        time = font4.render("Time: " + str(m) + ":" + str(s), 1, WHITE)
        pygame.draw.rect(screen, WHITE, player)
        screen.blit(level2, [100, 0])
        screen.blit(time, [1000, 0])
        for w in walls_two:
            pygame.draw.rect(screen, NEON_BLUE, w)

        for c in coins_two:
            pygame.draw.rect(screen, YELLOW, c)

        pygame.draw.rect(screen, GREEN, door2)
        pygame.draw.rect(screen, RED, teleport2)

    elif stage == 3:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, player)
        for w in walls_two:
            pygame.draw.rect(screen, NEON_BLUE, w)
            
    elif stage == 4:
        screen.fill(WHITE)

    elif stage == 5:
        screen.blit(img2, [0, 0])
        pygame.draw.rect(screen, BLACK, [300, 300, 600, 200])
        win = font3.render("YOU WIN!", 1, WHITE)
        screen.blit(win, [340, 350])

    elif stage == 6:
        screen.blit(img3, [0,0])
    
    '''gray = (175, 175, 175)
    for y in range(0, HEIGHT, 25):
        pygame.draw.line(screen, gray, [0, y], [WIDTH, y])
        
    for x in range(0, WIDTH, 25):
        pygame.draw.line(screen, gray, [x, 0], [x, HEIGHT])
    '''
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
