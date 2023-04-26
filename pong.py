import pygame as pg
import random
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)


VINDU_BREDDE = 600
VINDU_HOYDE = 400
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

poeng1 = 0
poeng2 = 0

class Ball:
    def __init__(self, x, y, radius, farge, fart):
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.fart = fart
        self.xfart = random.randint(4, 8)
        self.yfart = random.randint(4, 8)

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
        if self.x - self.radius <= rektangel.x + rektangel.bredde:
            self.xfart = -self.xfart
        elif self.x + self.radius >= rektangel2.x + rektangel2.bredde:
            self.xfart = -self.xfart
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
ball = Ball(150, 150, 10, (250, 250, 250), 5)
rektangel = Rektangel((250, 250, 250), 15, 150, 15, 100)
rektangel2 = Rektangel((250, 250, 250), 570, 150, 15, 100)



while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    vindu.fill((0, 0, 0))
    pg.draw.line(vindu, (250, 250, 250), [300, 0], [300, 400], 5)
    ball.tegn()
    ball.flytt(rektangel, rektangel2)
    rektangel.tegn()
    rektangel2.tegn()
    rektangel.sjekk_vegg()
    rektangel2.sjekk_vegg()

    
    

    trykkede_taster = pg.key.get_pressed()
    if trykkede_taster[K_UP]:
        rektangel2.y -= 5
    elif trykkede_taster[K_DOWN]:
        rektangel2.y += 5
    
    if trykkede_taster[K_w]:
        rektangel.y -=5
    elif trykkede_taster[K_s]:
        rektangel.y += 5
    

        
        
    

    

    clock.tick(60)
    pg.display.flip()

pg.quit()  
        