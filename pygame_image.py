import sys
import pygame as pg
from math import sin

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") # 背景surface
    kokaton = pg.image.load("ex01/fig/3.png") # こーかとんsurface
    kokaton = pg.transform.flip(kokaton, True, False) #こーかとんflip
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]
    # kokatons = [kokaton, pg.transform.rotozoom(kokaton, 10, 1.0), kokaton, pg.transform.rotozoom(kokaton, 10, 1.0)] #こーかとん回転    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        t = tmr%1600
        r = sin(tmr/10)
        screen.blit(bg_imgs[(tmr//1600)%2], [-t, 0])
        screen.blit(bg_imgs[(tmr//1600+1)%2], [1600-t, 0]) # 背景表示
        screen.blit(pg.transform.rotozoom(kokaton, 10*r, 1.0), [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()