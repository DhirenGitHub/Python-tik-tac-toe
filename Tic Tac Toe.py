import pygame
import sys

WIDTH = 10 + 110 * 3
HEIGHT = 10 + 110 * 3
FPS = 120

pygame.init()

pygame.display.set_caption("Tic Tac Toe!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
places = [["", "", ""],
          ["", "", ""],
          ["", "", ""]]
turn = "X"
winner = ""


def draw_boxes():
    for o in range(3):
        for p in range(3):
            pygame.draw.rect(screen, (10, 10, 10), (10 + 110 * p, 10 + 110 * o, 100, 100))


def click():
    mouse_press = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    global turn

    if mouse_press[0] == 1:
        for o in range(3):
            for p in range(3):
                if 10 + 110 * p + 100 >= mouse_pos[0] >= 10 + 110 * p:
                    if 10 + 110 * o + 100 >= mouse_pos[1] >= 10 + 110 * o:
                        if turn == "X":
                            pygame.time.delay(200)
                            places[o][p] = "X"
                            turn = "O"

                        elif turn == "O":
                            pygame.time.delay(200)
                            places[o][p] = "O"
                            turn = "X"


font = pygame.font.SysFont("bold", 100)
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((5, 5, 5))
    draw_boxes()
    click()
    for i in range(3):
        for q in range(3):
            if places[i][q] == "O":
                txt = font.render("O", 1, (250, 250, 250))
                screen.blit(txt, (10 + 110 * q + 20, 10 + 110 * i + 20))
            elif places[i][q] == "X":
                txt = font.render("X", 1, (250, 250, 250))
                screen.blit(txt, (10 + 110 * q + 20, 10 + 110 * i + 20))

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        for i in range(3):
            for p in range(3):
                places[i][p] = ""
        turn = "X"

    pygame.display.update()
    pygame.display.flip()
