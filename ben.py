import pygame
import random
import time

pygame.init()
pygame.display.set_caption('Raumschiff Rogue Like')
clock = pygame.time.Clock()
h=1000
b=800
f=pygame.display.set_mode((h, b))
spieler = pygame.image.load('raumschiff.png')
spieler = pygame.transform.scale(spieler, (200,200))

gegner = pygame.image.load('gegner.png')
gegner = pygame.transform.scale(gegner, (50,50))


schussausssehen2 = pygame.image.load('schuss2.png')
schussausssehen2 = pygame.transform.scale(schussausssehen2, (20,20))

schussausssehen1 = pygame.image.load('schuss.png')
schussausssehen1 = pygame.transform.scale(schussausssehen1, (20,20))

schusssybmol1 = pygame.image.load('schusssymbol1.png')
schusssybmol1 = pygame.transform.scale(schusssybmol1, (50,50))

schusssybmol1_on= pygame.image.load('schusssymbol1on.png')
schusssybmol1_on = pygame.transform.scale(schusssybmol1_on, (50,50))

schusssybmol2 = pygame.image.load('schusssymbol2.png')
schusssybmol2 = pygame.transform.scale(schusssybmol2, (50,50))

schusssybmol2_on= pygame.image.load('schusssymbol2 on.png')
schusssybmol2_on = pygame.transform.scale(schusssybmol2_on, (50,50))

kabumm1 = pygame.image.load('Kabumm1.png')
kabumm1 = pygame.transform.scale(kabumm1, (75,75))

kabumm2= pygame.image.load('Kabumm2.png')
kabumm2 = pygame.transform.scale(kabumm2, (50,50))

kabumm3 = pygame.image.load('Kabumm3.png')
kabumm3 = pygame.transform.scale(kabumm3, (50,50))

kabumm4= pygame.image.load('Kabumm4.png')
kabumm4 = pygame.transform.scale(kabumm4, (50,50))

kabumm = [kabumm1, kabumm2, kabumm3, kabumm4]
schusssybmol1variable=False
schusssybmol1_onvariable=True
schusssybmol2variable=True
schusssybmol2_onvariable=False

schusssybmol1_x=50
schusssybmol1_y=700
schusssybmol2_x=125
schusssybmol2_y=700





schussausssehen=schussausssehen1



Kabumm1visible=False
Kabumm2visible=False
Kabumm3visible=False
Kabumm4visible=False
gegnerleben=3
schiessen=True
schiessen1=True
schuss_visible1=False
das=True
x=500
y=550
gegnerx= 500
gegnery= 5
w=True
y_bewegung= 0
x_bewegung = 0
x_pos_array = []
y_pos_array = []
weg_array = []
for i in range(1,1000):
    x_pos = random.randint(0,1000)
    y_pos = random.randint(0,800)
    x_pos_array.append(x_pos)
    y_pos_array.append(y_pos)
    weg_array.append(0)
    
sternen_speed = 2
schuss_visible = False
schuss_speed = 0 
schuss_speed12 = 0 
schuss_x = 0
schuss_y = 0
schuss_x1 = 0
schuss_y1 = 0
schussspeed1=0
schussspeed2=0
if das:
    schuss1 = True
    schuss2= False
kabummcount=0
fps = 240
gegner_visible = True
while w:
    clock.tick(fps)
    if schuss2:
        schussausssehen=schussausssehen2

    if schuss1:
        schussausssehen=schussausssehen1


     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            w=False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x_bewegung = -1

        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            x_bewegung = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
           x_bewegung = 1
        
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
           x_bewegung = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
           y_bewegung = -1
           sternen_speed = 3

        if event.type == pygame.KEYUP and event.key == pygame.K_w:
           y_bewegung = 0
           sternen_speed = 2

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
           y_bewegung = 1
           sternen_speed = 0

        if event.type == pygame.KEYUP and event.key == pygame.K_s:
           y_bewegung = 0
           sternen_speed = 2

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if schiessen:
                schuss_visible = True
                schiessen=False
                schuss_x = x + 103
                schuss_y = y + 30
                if schuss2:
                    schuss_speed = 1

                if schuss1:
                    schuss_speed=4
               

        if schuss2:
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                schuss_visible = False
                schuss_speed = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            schussspeed1=schussspeed1 + 1

        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT: 
            schussspeed1=0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            schussspeed2=schussspeed2 + 1

        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT: 
            schussspeed2=0
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            schuss2=True 
            schuss1=False
            schuss_visible=False
            schusssybmol1_onvariable=False
            schusssybmol1variable=True
            schusssybmol2variable=False
            schusssybmol2_onvariable=True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            schuss2=False
            schuss1=True
            schuss_visible=False
            schusssybmol1_onvariable=True
            schusssybmol1variable=False
            schusssybmol2variable=True
            schusssybmol2_onvariable=False


    
    f.fill((25,0,15))

    #Spieler
    x = x + x_bewegung
    y = y + y_bewegung
    f.blit(spieler, (x,y))

    #gegner
    if gegner_visible:
        f.blit(gegner, (gegnerx,gegnery))
    # schusssymbole
    if schusssybmol1_onvariable:
        f.blit(schusssybmol1_on, (schusssybmol1_x,schusssybmol1_y))

    if schusssybmol1variable:
        f.blit(schusssybmol1, (schusssybmol1_x,schusssybmol1_y))

    if schusssybmol2_onvariable:
        f.blit(schusssybmol2_on, (schusssybmol2_x,schusssybmol2_y))

    if schusssybmol2variable:
        f.blit(schusssybmol2, (schusssybmol2_x,schusssybmol2_y))
        

    #collision 
    if gegner_visible: 

        if schuss_y > gegnery-10 and schuss_y < gegnery + 40  and schuss_x > gegnerx-10 and schuss_x < gegnerx + 40:
            gegnerleben = gegnerleben - 1
            schuss_visible1=False
            schuss_visible=False
            schuss_x=-50
            schuss_y=-50 

        
    
    if gegnerleben == 0:
        gegner_visible=False
        Kabumm1visible=True
        gegnerleben=1
    
     
    #Kabumm1visible=False
        
    if Kabumm1visible:   
        #for k in kabumm:
        if kabummcount + 1 == fps:
            kabummcount = 0
            Kabumm1visible = False
        kabummcount = kabummcount + 1

        j = kabummcount // 60
        f.blit(kabumm[j],(gegnerx,gegnery))
        

        
            
            

    #Schuss
    if schuss2:
        schuss_y = schuss_y - schuss_speed
        schuss_x=schuss_x - schussspeed1
        schuss_x=schuss_x +schussspeed2
        
        if schuss_visible:
            f.blit(schussausssehen, (schuss_x,schuss_y))

        if schuss_x< -50:
            schuss_x = 999

    #Kollision rechts
    if schuss_x > 1000:
        schuss_x = 0
           
            

    i = 0
    #Sterne
    for weg in weg_array:
        weg_array[i] = weg_array[i] + sternen_speed
        i = i + 1

    i = 0 

    for x2 in x_pos_array:
        f.set_at((x2,y_pos_array[i] + weg_array[i]), (255,255,255))
        
        if y_pos_array[i] + weg_array[i] > 800:
            weg_array[i] =  0
            y_pos_array[i] = 0 
            x_pos_array[i] = random.randint(0,1000)
        
        i = i + 1

    #Kollision links
    if x < -200:
        x = 999

    #Kollision rechts
    if x > 1000:
        x = -199

    #Kollision oben
    if  y< -50:
        y=-50
        sternen_speed=2
    
    #Kollision unten
    if  y> 600:
        y=600
        sternen_speed  =2 

    #schuss wechsel
    if schuss1:
        schuss2=False
        if schuss_visible:
            schuss_y = schuss_y- schuss_speed
        
            f.blit(schussausssehen, (schuss_x,schuss_y))

    if schuss_y<-50:
        schuss_visible=False
        schiessen=True

    if schuss_y<-50:
        schuss_visible=False
    
    if schuss_visible==False: 
        schiessen=True

    if schuss_y1<-50:
        schuss_visible1=False   
    
    if schuss_visible1==False: 
        schiessen1=True

    
    pygame.display.update()

pygame.quit()
    
    
    
