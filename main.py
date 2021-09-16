# %%
a = "abcde"
print(a[1:3])
import pygame as pg
import time, random, selenium
import sys

# POP BALL!

"""
-- To Do --
1) Power up, pops up key to get power up "Type 'Duck' to get power up!"
- Troll -> if lose get trolled
i) Balloon
ii) Small balls
iii) -5 points, - 10 points, -20 points
iv) Decrease Prob

- Benefit
i) Double balls
ii) Bowling ball - 2 points
iii) +5 points, + 10 points, +20 points
iv) Increase prob

- Troll both
i) Floating around
ii) Reverse Screen

- Reserve
i) Swap score

3) Add characteristic/abilities to each ball
4) Small ball less scores, prob higher, big balls more scores, prob lower
5) Pop up total type 
6) Implement to zoom chat
"""

class SeeSaw(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pg.image.load("assets/see_saw.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (100, 400))
        self.image2 = pg.image.load("assets/see_saw.png").convert_alpha()
        self.rect2 = self.image2.get_rect(topleft = (100, 400))
        self.mask = pg.mask.from_surface(self.image.convert_alpha())

    def update(self):
        self.image = pg.transform.rotozoom(self.image2, angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pg.mask.from_surface(self.image.convert_alpha())

class LeftBall(pg.sprite.Sprite):

    number_of_balls = 3
    power_num = 0
    win = False
    
    def __init__(self):
        super().__init__()
        random_number = random.randint(1, LeftBall.number_of_balls)
        random_ball = "assets/ball" + str(random_number) + ".png" 
        self.image = pg.image.load(random_ball).convert_alpha()
        self.image2 = pg.image.load(random_ball).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()
        random_x = random.randint(0, 368)
        random_y = random.randint(0,100)
        self.rect.x = float(random_x)
        self.rect.y = float(random_y)
        self.gravity = 1.027
        self.angle = 1
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        global angle
        global left_score
        global right_score

        self.rect.y *= self.gravity
        self.rect.y += 1 * self.gravity
        self.angle *= 1.1
        self.image, self.rect = self.spin()
        if self.rect.bottomleft[1] >= 600:
            self.kill()
        
        # spin ball
        try:
            offset = see_saw.rect[0] - self.rect[0], see_saw.rect[1] - self.rect[1]
            if self.rect.colliderect(see_saw.rect): 
                if self.mask.overlap(see_saw.mask, offset):
                    bok.play()
                    self.kill()
                    left_score += 1
                    right_score -= 1
                    if left_score >= 200:
                        LeftBall.win = True
                    angle += 0.2
                    return True
        except:
            pass

    def spin(self):
        rotated_ball = pg.transform.rotozoom(self.image2, self.angle, 1)
        rotated_rect = rotated_ball.get_rect(center = self.rect.center)
        return rotated_ball, rotated_rect


class RightBall(pg.sprite.Sprite):

    number_of_balls = 3
    power_num = 0
    win = False
    
    def __init__(self):
        super().__init__()
        random_number = random.randint(1, RightBall.number_of_balls)
        random_ball = "assets/ball" + str(random_number) + ".png" 
        self.image = pg.image.load(random_ball).convert_alpha()
        self.image2 = pg.image.load(random_ball).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()
        random_x = random.randint(500, 868)
        random_y = random.randint(0, 100)
        self.rect.x = float(random_x)
        self.rect.y = float(random_y)
        self.gravity = 1.027
        self.angle = -1
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        global angle
        global left_score
        global right_score

        self.rect.y *= self.gravity
        self.rect.y += 1 * self.gravity
        self.angle *= 1.1
        self.image, self.rect = self.spin()
        if self.rect.bottomleft[1] >= 600:
            self.kill()
        
        # spin ball
        try:
            offset = see_saw.rect[0] - self.rect[0], see_saw.rect[1] - self.rect[1]
            if self.rect.colliderect(see_saw.rect):
                if self.mask.overlap(see_saw.mask, offset):
                    bok.play()
                    self.kill()
                    left_score -= 1
                    right_score += 1
                    if right_score >= 200:
                        RightBall.win = True
                    angle -= 0.2
                    return True
        except:
            pass

    def spin(self):
        rotated_ball = pg.transform.rotozoom(self.image2, self.angle, 1)
        rotated_rect = rotated_ball.get_rect(center = self.rect.center)
        return rotated_ball, rotated_rect
    
def setup():
    global clock
    global surface
    pg.init()
    pg.display.set_caption('Keyboard Warrior')
    surface = pg.display.set_mode((900, 600))
    clock = pg.time.Clock()

def set_assets():
    global see_saw
    global bg 
    global start_button
    global start_button_pressed
    global tiang
    global bok
    global font 
    global powerUpFont
    global font2 
    global credit_font
    global seeSaw_group
    global left_ball_group
    global right_ball_group
    global BUTTON_DRAW
    global mouse_clicked
    global white
    global black
    global khaki
    global word_list
    global start

    see_saw = SeeSaw()
    bg = pg.image.load("assets/bg3.png").convert()
    start_button = pg.image.load("assets/start.png").convert() #400 x 200
    start_button_pressed = pg.image.load("assets/pressed.png").convert()
    tiang = pg.image.load("assets/tiang.png").convert()
    bok = pg.mixer.Sound("sound/bok2.mp3")
    font = pg.font.Font("font/font1.ttf", 36)
    powerUpFont = pg.font.Font("font/font1.ttf", 72)
    font2 = pg.font.Font("font/font1.ttf", 95)
    credit_font = pg.font.Font("font/font1.ttf", 18)
    seeSaw_group = pg.sprite.Group()
    seeSaw_group.add(see_saw)
    left_ball_group = pg.sprite.Group()
    right_ball_group = pg.sprite.Group()
    BUTTON_DRAW = start_button
    mouse_clicked = False
    white = (255, 255, 255)
    black = (0, 0, 0)
    khaki = (240,230,140)
    word_list = ["Apple","Book","Cat","Duck","Elephant","Family","Giraffe"]

def set_globals():
    global left_score
    global right_score
    global angle
    global total_click
    global power_up_thres
    global power_up_random
    global start

    left_score = 0
    right_score = 0
    angle = 0
    total_click = 0
    power_up_thres = 100
    power_up_random = random.randint(0,len(word_list)-1)
    start = None
    LeftBall.power_num, RightBall.power_num = 0, 0


def get_rand_colour():
    colour_r = random.randint(0,255)
    colour_g = random.randint(0,255)
    colour_b = random.randint(0,255)
    return (colour_r,colour_g,colour_b)

def powerUpFuncLeft():
    if LeftBall.power_num == 1:
        spawn_sound.play()
        ball = LeftBall()  
        left_ball_group.add(ball)

def powerUpFuncRight():
    if RightBall.power_num == 1:
        spawn_sound.play()
        ball = RightBall()
        right_ball_group.add(ball)

def powerUpTextFunc():
    if LeftBall.power_num == 1:
        font_size = font.size("Left Power up! Double Ball!")[0]/2
        power_up_text = font.render("Left Power up! Double Ball!", True, get_rand_colour())
        surface.blit(power_up_text, (450-font_size, 20))

    elif RightBall.power_num == 1:
        font_size = font.size("Right Power up! Double Ball!")[0]/2
        power_up_text = font.render("Right Power up! Double Ball!", True, get_rand_colour())
        surface.blit(power_up_text, (450-font_size, 20))

setup()
set_assets()
set_globals()

while True:
    surface.fill((240,240,240))
    surface.blit(bg,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if  LeftBall.win == False and RightBall.win == False:
                spawn_sound = pg.mixer.Sound("sound/sound"+str(random.randint(1,3))+".mp3")
                total_click += 1
                spawn_sound.play()
                ball = LeftBall()  
                left_ball_group.add(ball)
                if event.key == pg.K_d: #represent left side
                    powerUpFuncLeft()
                elif event.key == pg.K_e: #represent right side pressed
                    powerUpFuncRight()
                if total_click >= power_up_thres:
                    if event.key == pg.K_d:
                        power_up_thres = total_click + 100
                        power_up_random = random.randint(0,len(word_list))
                        LeftBall.power_num = 1
                        start = pg.time.get_ticks()
                    elif event.key == pg.K_e:
                        power_up_thres = total_click + 100
                        power_up_random = random.randint(0,len(word_list))
                        RightBall.power_num = 1
                        start = pg.time.get_ticks() 
                    
                if event.key == pg.K_1:
                    total_click += 1
                    spawn_sound.play()
                    ball = LeftBall()  
                    left_ball_group.add(ball)
                elif event.key == pg.K_2:
                    total_click += 1
                    spawn_sound.play()
                    ball = RightBall()  
                    right_ball_group.add(ball)
        if event.type == pg.MOUSEBUTTONDOWN:
            if (250 <= pg.mouse.get_pos()[0] <= 650) and (250 <= pg.mouse.get_pos()[1] <= 450):
                mouse_clicked = True
                BUTTON_DRAW = start_button_pressed
            else:
                mouse_clicked = False
        if event.type == pg.MOUSEBUTTONUP:
            BUTTON_DRAW = start_button
            if mouse_clicked == True and (250 <= pg.mouse.get_pos()[0] <= 650) and (250 <= pg.mouse.get_pos()[1] <= 450):
                mouse_clicked = False
                LeftBall.win = False
                RightBall.win = False
                set_globals()
    
    if LeftBall.win == False and RightBall.win == False:
        # power ups
        if total_click >= power_up_thres:
            print(power_up_random)
            print(word_list[power_up_random])
            print(powerUpFont.size(word_list[power_up_random])[0])
            font_size = powerUpFont.size(word_list[power_up_random])[0]/2
            power_up_text = powerUpFont.render(word_list[power_up_random], True, get_rand_colour())
            surface.blit(power_up_text, (450-font_size, 20))
        if start:
            power_up_thres = total_click + 100#to make sure the second powerup wont pop out during first power up
            time_since_powerUp = pg.time.get_ticks() - start
            if time_since_powerUp >= 2000:
                LeftBall.power_num, RightBall.power_num = 0, 0
                font_size = powerUpFont.size("Power up ends!")[0]/2
                power_up_text = powerUpFont.render("Power up ends!", True, get_rand_colour())
                surface.blit(power_up_text, (450-font_size, 20))
            if time_since_powerUp >= 3000:
                start = None
        powerUpTextFunc()
        left_ball_group.draw(surface)
        left_ball_group.update()
        right_ball_group.draw(surface)
        right_ball_group.update()
        seeSaw_group.draw(surface)
        seeSaw_group.update()
        surface.blit(tiang, (440, 400))
        left_font = font.render(str(left_score), True, white)
        right_font = font.render(str(right_score), True, white)
        surface.blit(left_font, (5,0))
        surface.blit(right_font, (800,0))
    else:
        left_ball_group.empty()
        right_ball_group.empty()
        if LeftBall.win == True:
            win_font = font2.render("Left side Wins!", True, white)
        else:
            win_font = font2.render("Right side Wins!", True, white)
        total_click_font = font.render("Total clicks: " + str(total_click) +"!", True, khaki)
        credit = credit_font.render("Design & Code: Bernard & JX", True, (255, 99, 71))
        surface.blit(win_font, (20, 80))
        surface.blit(BUTTON_DRAW, (250,230))
        surface.blit(credit, (565, 570))
        surface.blit(total_click_font, (20, 550))

    pg.display.update()
    clock.tick(200)
# %%
