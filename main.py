import pygame # Импорт библиотеки пайнейма
import time # Импорт функции время
import threading

pygame.init()   # Запуск библиотеки пайгейм

clock = pygame.time.Clock() # Ограничение проходов по коду
coins = 0 # Счет
buff_click = 1 # Сила нажатия
rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_wood_auto/1.png'),(130,140)),
             pygame.transform.scale (pygame.image.load('materials/pickaxe_wood_auto/2.png'),(130,140))] # Массив с картинками для анимации

Screen = pygame.display.set_mode((1300, 800)) # Создание окна (Ширина и высота)
pygame.display.set_caption("Шахтерские приключения") # Название окна

class coin_spin(threading.Thread): # Создание класса
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True #Поток- демон

    def run(self) -> None:
        global Screen
        rect = pygame.Rect((85,80,178,178)) # Координаты нахожения объекта
        coin_num = 0 # Счетчик для анимации
        coin = [pygame.image.load('materials/coin/1.png'),pygame.image.load('materials/coin/1.png'),
                pygame.image.load('materials/coin/2.png'),pygame.image.load('materials/coin/2.png'),
                pygame.image.load('materials/coin/3.png'),pygame.image.load('materials/coin/3.png'),
                pygame.image.load('materials/coin/4.png'),pygame.image.load('materials/coin/4.png'),
                pygame.image.load('materials/coin/5.png'),pygame.image.load('materials/coin/5.png'),
                pygame.image.load('materials/coin/6.png'),pygame.image.load('materials/coin/6.png'),
                pygame.image.load('materials/coin/7.png'),pygame.image.load('materials/coin/7.png'),
                pygame.image.load('materials/coin/8.png'),pygame.image.load('materials/coin/8.png')] # Массив с анимацией монетки
        while True:
            Screen.blit(coin[coin_num],(85,80)) # Отображение анимации
            coin_num += 1 # Счетчик
            pygame.display.update(rect) # Обновление кадра с ограничением (для оптимизации)
            time.sleep(0.05) # Ожидание(что бы анимация была не быстрой)
            if coin_num == 15: # Если будет 16 кадр
                coin_num = 0 # обнулить

class autominer(threading.Thread): #Новый демонический поток
    def __init__(self, time_sleep, x, y, rock):
        threading.Thread.__init__(self)
        self.daemon = True #Поток- демон
        self.time_sleep = time_sleep #Интервал в виде аргумента
        self.x = x # координаты
        self.y = y
        self.rock = rock # массив с анимациями

    def run(self) -> None: #Функции
        global coins, buff_click, Screen
        background = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (130, 600)) # Задник
        rect = pygame.Rect((self.x,self.y,130,140)) # Прямоугольник для оптимизации(как выше)
        while True:
            Screen.blit(background, (self.x, 200)) # Отображение задника
            Screen.blit(self.rock[0], (self.x,self.y))
            pygame.display.update(rect) # Обновление кадра(для анимации)
            time.sleep(self.time_sleep)  # Сон
            coins += buff_click # Прибавление к счету
            Screen.blit(background, (self.x, 200)) # Обновление задника
            Screen.blit(self.rock[1], (self.x,self.y)) # Второй кадр анимации
            time.sleep(0.1) # Сон для плавности
            pygame.display.update(rect) # Обновление кадра


def DrawText(text, Textcolor, x, y, fsize): # Функция отрисовки текста
    font = pygame.font.Font('materials/extra/Fifaks.ttf', fsize) # Импорт шрифта
    text = font.render(text, True, Textcolor) # Создание шрифта
    textRect = text.get_rect() # Содание прямоугольника
    textRect.center = (x, y) # Центрование надписей
    Screen.blit(text, textRect) # Отображение текста на экране

def main_loop(): #
    global buff_click,coins,clock,rock_auto # Взятие глобальных переменных
    black = (0, 0, 0) # Черный цвет
    button_color = (13,28,67) # Цвет цифр на кнопках
    button_1 = pygame.image.load("materials/button/1.png") # Кнопка
    button_2 = pygame.image.load("materials/button/1.png")
    button_3 = pygame.image.load("materials/button/1.png")
    background_left = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (385, 800)) # Задний фон кусок
    background_right = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (675, 800))
    background_top = pygame.transform.scale(pygame.image.load('materials/extra/backgrond.png'), (440, 200))
    pygame.mixer.music.load("materials/extra/music.mp3")  # Импорт музыки
    pygame.mixer.music.set_volume(0.1)  # Контроль громкости звука
    rock = [pygame.image.load('materials/pickaxe_wood/1.png'),pygame.image.load('materials/pickaxe_wood/2.png')] # Анимация в массиве
    speed = [10, 7, 6, 5, 4, 3, 2, 1.4, 0.9, 0.6, 0.3] # Массив ускорения
    price_buff_click = 40 # Цена на улучшение клика
    price_autominer = 25 # Цена на улучшение автомайнера
    price_new_autominer = 20 # Цена покупки нового рабочего
    anim_click = 0 # Анимация нажатия
    lvl_click = 0 # Уровень силы клика
    lvl_autominer = 0 # Уровень майнера
    lvl_new_autominer = 0 # Сколько куплено копателей
    max_lvl_click = False # Максимальный уровень?
    max_lvl_autominer = False
    max_lvl_new_autominer = False
    Screen.fill((173, 216, 230)) # Залить фон
    pygame.mixer.music.play(10) # Включить музыку
    while True: # Бесконечный цикл
        for event in pygame.event.get(): # Проверка списков ивентов
            if event.type == pygame.QUIT: # Если нажат крестик
                exit() # Выход
                break # Выход из цикла

            if event.type == pygame.MOUSEBUTTONDOWN: # Если нажата мышка
                Mouse_Position = pygame.mouse.get_pos() # Запись координат мышки
                if 825 <= Mouse_Position[0] <= 1275 and 295 <= Mouse_Position[1] <= 745: # Если мышка находится между этими координатами (Основаня кнопка)
                    coins += buff_click # Прибавить значение
                    anim_click = 1 # Анимация

                if 65 <= Mouse_Position[0] <= 290 and 400 <= Mouse_Position[1] <= 480: # Если мышка находится между координатами(Прокачка клика)
                    if coins >= price_buff_click: # Если денег больше или равно цене
                        coins = coins - price_buff_click # Отнять стоймость
                        price_buff_click = price_buff_click * 2.4 # Увеличить стоймость
                        buff_click = buff_click * 1.6 # Увеличить силу клика
                        price_buff_click = round(price_buff_click) # Округление числа
                        lvl_click += 1 # Повышение уровня
                        if lvl_click == 1: # Если уровень 1
                            rock = [pygame.image.load('materials/pickaxe_stone/1.png'),pygame.image.load('materials/pickaxe_stone/2.png')]
                            rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_stone_auto/1.png'),(130,140)),
                                         pygame.transform.scale (pygame.image.load('materials/pickaxe_stone_auto/2.png'),(130,140))] # изменение массива
                            autominer_cut.rock = rock_auto # отправка обновленного массива
                            autominer_cut_2.rock = rock_auto
                            autominer_cut_3.rock = rock_auto
                        elif lvl_click == 2: # Если уровень 2
                            rock = [pygame.image.load('materials/pickaxe_iron/1.png'),pygame.image.load('materials/pickaxe_iron/2.png')]
                            rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_iron_auto/1.png'),(130,140)),
                                         pygame.transform.scale (pygame.image.load('materials/pickaxe_iron_auto/2.png'),(130,140))]
                            autominer_cut.rock = rock_auto # отправка обновленного массива
                            autominer_cut_2.rock = rock_auto
                            autominer_cut_3.rock = rock_auto
                        else:
                            rock = [pygame.image.load('materials/pickaxe_dimond/1.png'),pygame.image.load('materials/pickaxe_dimond/2.png')]
                            rock_auto = [pygame.transform.scale (pygame.image.load('materials/pickaxe_dimond_auto/1.png'),(130,140)),
                                         pygame.transform.scale (pygame.image.load('materials/pickaxe_dimond_auto/2.png'),(130,140))]
                            autominer_cut.rock = rock_auto # отправка обновленного массива
                            autominer_cut_2.rock = rock_auto
                            autominer_cut_3.rock = rock_auto
                            button_1 = pygame.image.load("materials/button/2.png") # изменение кнопки
                            max_lvl_click = True # Максимальный уровень

                if 65 <= Mouse_Position[0] <= 290 and 530 <= Mouse_Position[1] <= 610: # Если мышка находится между координатами(Прокачка майнера)
                    if coins >= price_autominer: # Если денег больше или равно цене
                        coins = coins - price_autominer # Отнять стоймость
                        price_autominer = price_autominer * 1.5 # Увеличить стоймость в полтора раза
                        lvl_autominer += 1 # Повышение уровня
                        autominer_cut.time_sleep = speed[lvl_autominer] # Изменение скорости
                        autominer_cut_2.time_sleep = speed[lvl_autominer]
                        autominer_cut_3.time_sleep = speed[lvl_autominer]
                        price_autominer = round(price_autominer) # Округление числа
                        if lvl_autominer == 10: # Если 10 уровня
                            button_2 = pygame.image.load("materials/button/2.png") # Изммение кнопки
                            max_lvl_autominer = True # Максимальный уровень

                if 65 <= Mouse_Position[0] <= 290 and 660 <= Mouse_Position[1] <= 740: # Между координатами
                    if coins >= price_new_autominer: # Проверка денег
                        coins = coins - price_new_autominer # Снятие цены
                        price_new_autominer = price_new_autominer * 5 # Повышение цен
                        lvl_new_autominer += 1 # Новый копатель
                        if lvl_new_autominer == 1: # Если 1 уровень
                            autominer_cut.start() # Создание нового потока
                        elif lvl_new_autominer == 2: # Если 2 уровень
                            autominer_cut_2.start() # Создание нового потока
                        else:
                            autominer_cut_3.start() # Создание нового потока
                            button_3 = pygame.image.load("materials/button/2.png") # Изменение кнопки
                            max_lvl_new_autominer = True # Максимальный уровень

        Screen.blit(background_left,(0,0))  # Отображение задника
        Screen.blit(background_right,(775,0))
        Screen.blit(background_top,(385,0))
        DrawText("Шахтерское приключение", black, 630, 50, 50) # Отрисовка текста
        DrawText("у вас " + str(f'{coins:.0f}') + " монет", black, 190, 300, 45) # Отрисовка текста
        DrawText("Сила нажатия ", black, 190, 380, 30) # Отрисовка текста
        DrawText("Автодобыча ", black, 190, 510, 30) # Отрисовка текста
        DrawText("Нанять рабочего ", black, 190, 640, 30) # Отрисовка текста
        Screen.blit(button_1,(65, 400)) # Отрисовка кнопок
        Screen.blit(button_2, (65, 530)) # Отрисовка кнопок
        Screen.blit(button_3, (65, 660)) # Отрисовка кнопок
        if max_lvl_click == False:
            DrawText(str(price_buff_click),button_color, 245, 440, 40) # Если не максимальный уровень то писать цену
        if max_lvl_autominer == False:
            DrawText(str(price_autominer), button_color, 245, 570, 40) # Если не максимальный уровень то писать цену
        if max_lvl_new_autominer == False:
            DrawText(str(price_new_autominer), button_color, 245, 700, 40) # Если не максимальный уровень то писать цену
        Screen.blit(rock[anim_click], (825,195)) # Отображение анимации
        time.sleep(0.05) # Сон
        anim_click = 0 # Анимация для клика
        pygame.display.update() # Обновление экрана
        clock.tick(60) # Ограничение кадров

autominer_cut = autominer(10,645,625,rock_auto) # Для быстрого вызова
autominer_cut_2 = autominer(10,515,625,rock_auto) #
autominer_cut_3 = autominer(10,385,625,rock_auto) #
coin_spin().start() # Запуск потока для анимации монетки
main_loop() # Запуск игры
pygame.quit() # Выход из библиотеки
quit() # Выход