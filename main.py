import pygame
import time
import threading

pygame.init()

clock = pygame.time.Clock()
coins = 0
buff_click = 1
rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_wood_auto/1.png'),(130,140)),
             pygame.transform.scale (pygame.image.load('materials/pickaxe_wood_auto/2.png'),(130,140))]

Screen = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Шахтерские приключения")

class coin_spin(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self) -> None:
        global Screen
        rect = pygame.Rect((85,80,178,178))
        coin_num = 0
        coin = [pygame.image.load('materials/coin/1.png'),pygame.image.load('materials/coin/1.png'),
                pygame.image.load('materials/coin/2.png'),pygame.image.load('materials/coin/2.png'),
                pygame.image.load('materials/coin/3.png'),pygame.image.load('materials/coin/3.png'),
                pygame.image.load('materials/coin/4.png'),pygame.image.load('materials/coin/4.png'),
                pygame.image.load('materials/coin/5.png'),pygame.image.load('materials/coin/5.png'),
                pygame.image.load('materials/coin/6.png'),pygame.image.load('materials/coin/6.png'),
                pygame.image.load('materials/coin/7.png'),pygame.image.load('materials/coin/7.png'),
                pygame.image.load('materials/coin/8.png'),pygame.image.load('materials/coin/8.png')]
        while True:
            Screen.blit(coin[coin_num],(85,80))
            coin_num += 1
            pygame.display.update(rect)
            time.sleep(0.05)
            if coin_num == 15:
                coin_num = 0

class autominer(threading.Thread):
    def __init__(self, time_sleep, x, y, rock):
        threading.Thread.__init__(self)
        self.daemon = True
        self.time_sleep = time_sleep
        self.x = x
        self.y = y
        self.rock = rock

    def run(self) -> None:
        global coins, buff_click, Screen
        background = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (130, 600)) # Задник
        rect = pygame.Rect((self.x,self.y,130,140))
        while True:
            Screen.blit(background, (self.x, 200))
            Screen.blit(self.rock[0], (self.x,self.y))
            pygame.display.update(rect)
            time.sleep(self.time_sleep)
            coins += buff_click
            Screen.blit(background, (self.x, 200))
            Screen.blit(self.rock[1], (self.x,self.y))
            time.sleep(0.1)
            pygame.display.update(rect)


def DrawText(text, Textcolor, x, y, fsize):
    font = pygame.font.Font('materials/extra/Fifaks.ttf', fsize)
    text = font.render(text, True, Textcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    Screen.blit(text, textRect)

def main_loop(): #
    global buff_click,coins,clock,rock_auto
    black = (0, 0, 0)
    button_color = (13,28,67)
    button_1 = pygame.image.load("materials/button/1.png")
    button_2 = pygame.image.load("materials/button/1.png")
    button_3 = pygame.image.load("materials/button/1.png")
    background_left = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (385, 800))
    background_right = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (675, 800))
    background_top = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (440, 200))
    pygame.mixer.music.load("materials/extra/music.mp3")
    pygame.mixer.music.set_volume(0.1)
    rock = [pygame.image.load('materials/pickaxe_wood/1.png'),pygame.image.load('materials/pickaxe_wood/2.png')]
    speed = [10, 7, 6, 5, 4, 3, 2, 1.4, 0.9, 0.6, 0.3]
    price_buff_click = 40
    price_autominer = 25
    price_new_autominer = 20
    anim_click = 0
    lvl_click = 0
    lvl_autominer = 0
    lvl_new_autominer = 0
    max_lvl_click = False
    max_lvl_autominer = False
    max_lvl_new_autominer = False
    Screen.fill((173, 216, 230))
    pygame.mixer.music.play(10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_Position = pygame.mouse.get_pos()
                if 825 <= Mouse_Position[0] <= 1275 and 295 <= Mouse_Position[1] <= 745:
                    coins += buff_click
                    anim_click = 1

                if 65 <= Mouse_Position[0] <= 290 and 400 <= Mouse_Position[1] <= 480:
                    if coins >= price_buff_click:
                        coins = coins - price_buff_click
                        price_buff_click = price_buff_click * 2.4
                        buff_click = buff_click * 1.6
                        price_buff_click = round(price_buff_click)
                        lvl_click += 1
                        if lvl_click == 1:
                            rock = [pygame.image.load('materials/pickaxe_stone/1.png'),pygame.image.load('materials/pickaxe_stone/2.png')]
                            rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_stone_auto/1.png'),(130,140)),
                                         pygame.transform.scale (pygame.image.load('materials/pickaxe_stone_auto/2.png'),(130,140))] # изменение массива
                            autominer_cut.rock = rock_auto
                            autominer_cut_2.rock = rock_auto
                            autominer_cut_3.rock = rock_auto
                        elif lvl_click == 2:
                            rock = [pygame.image.load('materials/pickaxe_iron/1.png'),pygame.image.load('materials/pickaxe_iron/2.png')]
                            rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_iron_auto/1.png'),(130,140)),
                                         pygame.transform.scale (pygame.image.load('materials/pickaxe_iron_auto/2.png'),(130,140))]
                            autominer_cut.rock = rock_auto
                            autominer_cut_2.rock = rock_auto
                            autominer_cut_3.rock = rock_auto
                        else:
                            rock = [pygame.image.load('materials/pickaxe_dimond/1.png'),pygame.image.load('materials/pickaxe_dimond/2.png')]
                            rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_dimond_auto/1.png'),(130,140)),
                                         pygame.transform.scale (pygame.image.load('materials/pickaxe_dimond_auto/2.png'),(130,140))]
                            autominer_cut.rock = rock_auto
                            autominer_cut_2.rock = rock_auto
                            autominer_cut_3.rock = rock_auto
                            button_1 = pygame.image.load("materials/button/2.png")
                            max_lvl_click = True

                if 65 <= Mouse_Position[0] <= 290 and 530 <= Mouse_Position[1] <= 610:
                    if coins >= price_autominer:
                        coins = coins - price_autominer
                        price_autominer = price_autominer * 1.5
                        lvl_autominer += 1
                        autominer_cut.time_sleep = speed[lvl_autominer]
                        autominer_cut_2.time_sleep = speed[lvl_autominer]
                        autominer_cut_3.time_sleep = speed[lvl_autominer]
                        price_autominer = round(price_autominer)
                        if lvl_autominer == 10:
                            button_2 = pygame.image.load("materials/button/2.png")
                            max_lvl_autominer = True

                if 65 <= Mouse_Position[0] <= 290 and 660 <= Mouse_Position[1] <= 740:
                    if coins >= price_new_autominer:
                        coins = coins - price_new_autominer
                        price_new_autominer = price_new_autominer * 5
                        lvl_new_autominer += 1
                        if lvl_new_autominer == 1:
                            autominer_cut.start()
                        elif lvl_new_autominer == 2:
                            autominer_cut_2.start()
                        else:
                            autominer_cut_3.start()
                            button_3 = pygame.image.load("materials/button/2.png")
                            max_lvl_new_autominer = True

        Screen.blit(background_left,(0,0))
        Screen.blit(background_right,(775,0))
        Screen.blit(background_top,(385,0))
        DrawText("Шахтерское приключение", black, 630, 50, 50)
        DrawText("у вас " + str(f'{coins:.0f}') + " монет", black, 190, 300, 45)
        DrawText("Сила нажатия ", black, 190, 380, 30)
        DrawText("Автодобыча ", black, 190, 510, 30)
        DrawText("Нанять рабочего ", black, 190, 640, 30)
        Screen.blit(button_1,(65, 400))
        Screen.blit(button_2, (65, 530))
        Screen.blit(button_3, (65, 660))
        if max_lvl_click == False:
            DrawText(str(price_buff_click),button_color, 245, 440, 40)
        if max_lvl_autominer == False:
            DrawText(str(price_autominer), button_color, 245, 570, 40)
        if max_lvl_new_autominer == False:
            DrawText(str(price_new_autominer), button_color, 245, 700, 40)
        Screen.blit(rock[anim_click], (825,195))
        time.sleep(0.05)
        anim_click = 0
        pygame.display.update()
        clock.tick(60)

autominer_cut = autominer(10,645,625,rock_auto)
autominer_cut_2 = autominer(10,515,625,rock_auto)
autominer_cut_3 = autominer(10,385,625,rock_auto)
coin_spin().start()
main_loop()
pygame.quit()
quit()