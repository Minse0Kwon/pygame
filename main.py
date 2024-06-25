import asyncio
import pygame as pg
pg.init()
background_colour = (252, 252, 252)
screen = pg.display.set_mode((100, 100)) 
screen.fill(background_colour) 
pg.display.set_caption('Test') 



font = pg.font.SysFont("Times New Roman", 30)
text = font.render('GeeksForGeeks', True, (0,0,0))

async def main():
    temp = 1
    running = True

    while running: 
        label = font.render(str(temp), 1, (0,0,0))
        screen.blit(label,(0,35))

        
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                running = False
        

        pg.display.flip()
        screen.fill(background_colour) 

        await asyncio.sleep(0)
        if not running:
            pg.quit()
            return
        temp += 1

    await asyncio.sleep(0)

asyncio.run( main() )