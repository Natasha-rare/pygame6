import os
import random
import pygame



class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA, 32)

        self.rect = pygame.Rect(x, y, 20, 20)
        self.rect.x = x
        self.rect.y = y
        #pygame.draw.circle(self.image, pygame.Color("red"), (10, 10), 10)
        pygame.draw.rect(self.image, pygame.Color("red"), self.rect, 5)
        print(self.rect)

    def update(self, y):
        pass
       # self.rect = self.rect.move(self.rect.x, y)
        # pygame.draw.rect(self.image, pygame.Color("white"), (self.rect.x, self.rect.y, 20, 20), 5)


# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
y = 0
v = 200  # пикселей в секунду
fps = 60
all_sprites.add(Hero(50, 50))
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            all_sprites.add(Hero(event.pos[0], event.pos[1]))
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    y += v / fps
    all_sprites.update(y)

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()