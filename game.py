import pygame
import sys

# Sprite
# Mask

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/ball3.png")
        self.rect = self.image.get_rect(center = (500, 400))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.rect.y -= 10
                elif event.key == pygame.K_s:
                    self.rect.y += 10
                if event.key == pygame.K_a:
                    self.rect.x -= 10
                elif event.key == pygame.K_d:
                    self.rect.x += 10

pygame.init()

ball1 = Ball()
ball_group = pygame.sprite.Group()
ball_group.add(ball1)

# surfaces
screen = pygame.display.set_mode((900, 600))
khaki = (240,230,140)
enemy_ball = pygame.image.load("assets/ball0.png")
enemy_ball_rect = enemy_ball.get_rect(center = (100,100))
bg = pygame.image.load("assets/bg1.png")
font_1 = pygame.font.Font("font/font1.ttf", 46)
sound_1 = pygame.mixer.Sound("sound/bok.mp3")
sound_1.set_volume(1)
clock = pygame.time.Clock()
# Rectangle 

text = "You win!"
text_rendered = font_1.render(text, True, (0,0,0))
while True: #0.004
    # events 
    screen.fill(khaki)
    
    enemy_ball_rect.x += 1
    # screen.blit(bg, (0,0))
    screen.blit(text_rendered, (300, 100))
    ball_group.update()
    ball_group.draw(screen)
    screen.blit(enemy_ball, enemy_ball_rect)
    pygame.display.update()
    clock.tick(120)