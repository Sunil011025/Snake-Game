import random
import pygame
import sys

pygame.init()

# Screen setup
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sunil Snake Game")

# Snake position
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0

# Food position
food_x = random.randrange(0, width // 10) * 10
food_y = random.randrange(0, height // 10) * 10

clock = pygame.time.Clock()

snake_body = [(snake_x, snake_y)]


def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y

    # Move snake
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check collision with itself
    if (snake_x, snake_y) in snake_body[1:]:
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    # Add new head
    snake_body.append((snake_x, snake_y))

    # Check food collision
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, width // 10) * 10
        food_y = random.randrange(0, height // 10) * 10
    else:
        snake_body.pop(0)

    # Draw everything
    game_screen.fill((150, 150, 150))

    pygame.draw.circle(game_screen, (0, 0, 128), (food_x, food_y), 6)

    for (x, y) in snake_body:
        pygame.draw.circle(game_screen, (255, 255, 102), (x, y), 6)

    pygame.display.update()


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x, change_y = -10, 0
            elif event.key == pygame.K_RIGHT:
                change_x, change_y = 10, 0
            elif event.key == pygame.K_UP:
                change_x, change_y = 0, -10
            elif event.key == pygame.K_DOWN:
                change_x, change_y = 0, 10

    # 🔥 FIX: move this OUTSIDE event loop
    display_snake_and_food()
    clock.tick(15)