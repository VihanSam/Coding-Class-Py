import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

keep_going = True
yellow = (255, 255, 0)
red = (255,0,0)
green = (0,255,0)
silver = (192,192,192)
radius = 75

#Loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.rect(screen, silver,[0,0,200,470])
    pygame.draw.circle(screen, yellow,(100,230),radius)
    pygame.draw.circle(screen, red,(100,380),radius)
    pygame.draw.circle(screen, green,(100,80),radius)
    pygame.draw.rect(screen, silver,[67,470,65,350]) 
    pygame.display.update()
pygame.quit()