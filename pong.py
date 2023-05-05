import pygame as pg
import random
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)
#Liten feil i koden som var veldig vanskelig å fikse, jeg prøvde alt, men jeg vet ikke om den er fikset nå (ballen henger seg på rektanglene
# noen ganger, som igjen ødelegger poengene)


VINDU_BREDDE = 600
VINDU_HOYDE = 400
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()
pg.font.init()

class Ball:
    spiller1 = 0
    spiller2 = 0
    def __init__(self, x, y, radius, farge, fart):
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.fart = fart
        self.xfart = random.randint(4,5)
        self.yfart = random.randint(4,5)
      
       

    def tegn(self):
        pg.draw.circle(vindu, self.farge, (self.x, self.y), self.radius)
    


    def flytt(self, rektangel, rektangel2):
        if (self.x - self.radius <= 0):
            self.xfart = -self.xfart
            self.x = self.radius
        elif (self.x + self.radius >= VINDU_BREDDE):
            self.xfart = -self.xfart
            self.x = VINDU_BREDDE - self.radius
        if (self.y - self.radius <= 0):
            self.yfart = -self.yfart
            self.y = self.radius
        elif (self.y + self.radius >= VINDU_HOYDE):
            self.yfart = -self.yfart
            self.y = VINDU_HOYDE - self.radius

        
        # Sjekker kollisjon med rektangler
        if self.x - self.radius <= rektangel.x + rektangel.bredde and self.y < rektangel.y + rektangel.hoyde and self.y > rektangel.y:
            self.xfart = -self.xfart
            Ball.spiller1 += 1
        elif self.x - self.radius >= rektangel2.x - rektangel2.bredde and self.y < rektangel2.y + rektangel2.hoyde and self.y > rektangel2.y:
            self.xfart = -self.xfart
            Ball.spiller2 += 1

        self.x += self.xfart
        self.y += self.yfart

      
        

class Rektangel:
    def __init__(self, farge, x, y, bredde, hoyde):
        self.farge = farge
        self.x = x
        self.y = y
        self.bredde = bredde
        self.hoyde = hoyde
        self.xfart = 0
        self.yfart = 0

    def tegn(self):
        pg.draw.rect(vindu, self.farge, (self.x, self.y, self.bredde, self.hoyde))
    
    def sjekk_vegg(self):
        if (self.x - self.bredde <= 0):
            self.x = self.bredde
        elif (self.x + self.bredde >= VINDU_BREDDE):
            self.x = VINDU_BREDDE - self.bredde
        if (self.y <= 0):
            self.y = 1
        elif (self.y + self.hoyde >= VINDU_HOYDE):
            self.y = VINDU_HOYDE - self.hoyde



        
fortsett = True
ball = Ball(300, 200, 10, (250, 250, 250), 5)
rektangel = Rektangel((250, 250, 250), 10, 150, 10, 100)
rektangel2 = Rektangel((250, 250, 250), 580, 150, 10, 100)



while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False 

            
    vindu.fill((0, 0, 0))
    skrift = pg.font.Font(None, 50)
    pg.draw.line(vindu, (250, 250, 250), [300, 0], [300, 400], 5)
    ball.tegn()
    ball.flytt(rektangel, rektangel2)
    rektangel.tegn()
    rektangel2.tegn()
    rektangel.sjekk_vegg()
    rektangel2.sjekk_vegg()
    
    

    #Sjekker kollisjon med vegg
    if ball.x - ball.radius <= 0 or ball.x + ball.radius >= VINDU_BREDDE:
            fortsett = False
            print("Spiller 1 poeng: ", Ball.spiller1)
            print("Spiller 2 poeng: ", Ball.spiller2)
    
           
    #Skriver poeng på skjermen
    spiller_skrift = skrift.render(f"{Ball.spiller1}", False, (250, 250, 250))
    vindu.blit(spiller_skrift,(130, 10))
    spiller2_skrift = skrift.render(f"{Ball.spiller2}", False, (250, 250, 250))
    vindu.blit(spiller2_skrift, (450, 10))


    
    trykkede_taster = pg.key.get_pressed()
    if trykkede_taster[K_UP]:
        rektangel2.y -= 10
    elif trykkede_taster[K_DOWN]:
        rektangel2.y += 10
    
    if trykkede_taster[K_w]:
        rektangel.y -= 10
    elif trykkede_taster[K_s]:
        rektangel.y += 10
    

    

    clock.tick(60)
    pg.display.flip()

pg.quit()  
        
