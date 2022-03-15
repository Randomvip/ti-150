# https://pythonprogramming.altervista.org/buttons-in-pygame/
import pygame
import os

pygame.init()
pygame.font.init()

X = 400
Y = 400

BUTTON_DIST = 107
BUTTON_RAD = 45
BUTTON_DIA = BUTTON_RAD * 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (51, 51, 51)
LIGHT_GREY = (165, 165, 165)
ORANGE = (254, 159, 10)

FPS = 30

BUTTON_NUMBER_FONT_SIZE = 46

WIDTH, HEIGHT = 450, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Assignment 3 - TI 150")

MYFONT = pygame.font.Font("SF-Pro-Display-Regular.otf", BUTTON_NUMBER_FONT_SIZE)

# BUTTONS = [clear, negative, percent, one, two, three, four, five, six, seven, eight, nine, zero,
# period, divide, multiply, subtract, add, equal]
#    pygame.draw.circle(WINDOW, LIGHT_GREY, (64, 306), 45)  # Top left button
#    pygame.draw.circle(WINDOW, LIGHT_GREY, (64 + BUTTON_DIST, 306), 45)  # Top middle left button
#    pygame.draw.circle(WINDOW, LIGHT_GREY, (64 + BUTTON_DIST * 2, 306), 45)  # Top middle right button
#    pygame.draw.circle(WINDOW, ORANGE, (64 + BUTTON_DIST * 3, 306), 45)  # Top right button

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'calc.PNG')), (WIDTH, HEIGHT))

history = []


def button(colour, x_pos, y_pos, text):
    text_render = MYFONT.render("text", True, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    pygame.draw.circle(WINDOW, colour, (x_pos, y_pos), 45)  # Top middle right button
#   pygame.draw.circle(WINDOW, (100, 100, 100), (x, y, w, h), BUTTON_RAD)
    return WINDOW.blit(text_render, (x, y))


def draw_window():
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit("text", (1, (HEIGHT / 2) - 15))
    pygame.display.update()


def inputs():
    global history
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            while (64 - BUTTON_RAD < mouse[0] < 64 + BUTTON_RAD) and (306 - BUTTON_RAD < mouse[1] < 306 + BUTTON_RAD):
                history = []
                clear = MYFONT.render("0", True, WHITE)
                WINDOW.blit(clear, (WIDTH - 190, (HEIGHT * 2 / 10)))
                pygame.display.update()


def interpret():
    global history
    first_number = []
    second_number = []
    if history[0] == ".":
        history.insert(0, "0")
    for item in history:
        if item == "*" or "/" or "+" or "-":
            operation_pos = history.index(item)

            for obj in history[:operation_pos]:
                first_number.append(obj)
            for obj1 in history[operation_pos:]:
                second_number.append(obj1)

            if item == "+":
                add(first_number, second_number)
            if item == "-":
                subtract(first_number, second_number)


def add(number1, number2):
    total = number1 + number2
    return total


def subtract(number1, number2):
    total = number1-number2
    return total


def multiply(number1, number2):
    total = number1 * number2
    return total


def divide(number1, number2):
    total = number1/number2
    return total


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

        draw_window()
        inputs()


main()
