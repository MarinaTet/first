import time
import random
from getkey import getkey  # Import at the top

def initial_grid(rows=10, cols=10):
    return [['.' for _ in range(cols)] for _ in range(rows)]

def print_grid(snake, food, grid_size=10):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in snake:
        grid[x][y] = 'X'
    fx, fy = food
    grid[fx][fy] = 'F'  # Represent food with 'F'
    for row in grid:
        print(" ".join(row))

def spawn_food(snake, grid_size=10):
    while True:
        food = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        if food not in snake:
            return food

def move_snake_safe(snake, key, food, grid_size=10):
    head_x, head_y = snake[-1]
    
    if key == 'w':  # Up
        new_head = (head_x - 1, head_y)
    elif key == 's':  # Down
        new_head = (head_x + 1, head_y)
    elif key == 'd':  # Right
        new_head = (head_x, head_y + 1)
    elif key == 'a':  # Left
        new_head = (head_x, head_y - 1)
    else:
        print("Invalid key! Use 'w', 's', 'a', or 'd' to move.")
        return False, food  

    if not (0 <= new_head[0] < grid_size and 0 <= new_head[1] < grid_size):
        print("Invalid move: Out of bounds!")
        return False, food

    if new_head in snake:
        print("Invalid move: Collision detected!")
        return False, food

    snake.append(new_head)
    
    if new_head == food:  # Snake eats food
        print("Yum! The snake ate the food!")
        food = spawn_food(snake, grid_size)  # Spawn new food
    else:
        snake.pop(0)  # Maintain length
    
    return True, food

def interactive_snake_game():
    snake = [(0, 0), (0, 1), (0, 2)]  # Initial snake position
    grid_size = 10
    food = spawn_food(snake, grid_size)

    while True:
        time.sleep(0.5)
        print_grid(snake, food, grid_size)

        print("\nWhich direction you wanna move?\n( w / a / s / d) or 'l' to leave the game: ")
        key = getkey()

        if key == "l":
            print("\nGame over! Slither Sisters thank you for playing.")
            time.sleep(1)
            print("You are awesome no matter what!\n")
            time.sleep(2)
            print(" ***  Bye!  ***")
            return  # Exit the function

        valid_move, food = move_snake_safe(snake, key, food, grid_size)
        if not valid_move:
            print("Try a different move.")

interactive_snake_game()
