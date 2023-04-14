import pygame
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
y_dir = 0
x_dir = 0

player_a = [10, 10, 20, 100]
player_b = [1240, 10, 20, 100]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    player_a[1] = ball_pos.y - 50
    
    pygame.draw.circle(screen, "white", ball_pos, 20)
    pygame.draw.rect(screen, "white", player_a)
    pygame.draw.rect(screen, "white", player_b)
    k = 0
    for i in range(0, 72):
        pygame.draw.rect(screen, "white", (635, k+5, 10, 10))
        k += 15
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if player_b[1] > 40:
            player_b[1] -= 300 * dt
        else:
            player_b[1] = player_b[1]
    
    if keys[pygame.K_s]:
        if player_b[1] < 575:
            player_b[1] += 300 * dt
        else:
            player_b[1] = player_b[1]

    if not y_dir:
        if ball_pos.y > 20:
            ball_pos.y -= 300 * dt
        else:
            ball_pos.y = ball_pos.y
            y_dir = 1
    if y_dir:
        if ball_pos.y < 700:
            ball_pos.y += 300 * dt
        else:
            ball_pos.y = ball_pos.y
            y_dir = 0
    if not x_dir:
        if ball_pos.x > 50:
            ball_pos.x -= 300 * dt
        else:
            ball_pos.x = ball_pos.x
            x_dir = 1            
    if x_dir:
        if ball_pos.x < 1240:
            ball_pos.x += 300 * dt
        else:
            if player_b[1] + player_b[3] > ball_pos.y > player_b[1]:
                ball_pos.x = ball_pos.x
                x_dir = 0
                continue
            else:
                running = False
    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()