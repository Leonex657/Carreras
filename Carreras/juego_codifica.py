import pygame
import sys

pygame.init()


SCREEN = pygame.display.set_mode((800,600))
pygame.display.set_caption("Menu")

WIDTH, HEIGTH = 610, 730
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("CARRO INSANO")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

fondo = pygame.image.load("carretera1.png").convert()
fondo_y = 0
carro_img = pygame.image.load("carro.png")
carro_img = pygame.transform.scale(carro_img, (78,78))

car = carro_img.get_rect(topleft=(WIDTH//2, HEIGTH - 60))
car_speed = 7

def draw_text(text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

obstaculo = pygame.sprite.Sprite()


while True:
    screen.blit(fondo, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el fondo hacia abajo
    fondo_y += 2
    if fondo_y >= HEIGTH:
        fondo_y = 0


    keys = pygame.key.get_pressed()
    if keys[pygame. K_LEFT] and car.left > 84:
        car.x -= car_speed
    if keys[pygame. K_RIGHT] and car.right < 495:
        car.x += car_speed
    if keys[pygame. K_UP]: car.y -= car_speed
    if keys[pygame. K_DOWN]: car.y += car_speed


    screen.blit(fondo, (0, fondo_y))
    screen.blit(fondo, (0, fondo_y - HEIGTH))



    car.clamp_ip(screen.get_rect())
    screen.blit(carro_img, car.topleft)
    
    pygame.display.flip()
    clock.tick(60)
    