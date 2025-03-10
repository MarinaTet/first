import time
from getkey import getkey  # Import at the top

# Create a function to make a blank grid (just dots)
def initial_grid(rows=10, cols=10):
    return [['.' for _ in range(cols)] for _ in range(rows)]

# Print the grid
def print_grid(snake, grid_size=10):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in snake:
        grid[x][y] = 'X'
    for row in grid:
        print(" ".join(row))

# Function to move the snake safely
def move_snake_safe(snake, key, grid_size=10):
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
        return False  

    if not (0 <= new_head[0] < grid_size and 0 <= new_head[1] < grid_size):
        print("Invalid move: Out of bounds!")
        return False

    if new_head in snake:
        print("Invalid move: Collision detected!")
        return False

    snake.append(new_head)
    snake.pop(0)  # Maintain length
    return True

# Main game loop
def interactive_snake_game():
    snake = [(0,0), (0,1), (0,2)]  # Initial snake position
    grid_size = 10

    while True:
        time.sleep(0.5)
        print_grid(snake, grid_size)

        print("\nWhich direction you wanna move?\n( w / a / s / d) or 'l' to leave the game: ")
        key = getkey()

        if key == "l":
            print("\nGame over! Slither Sisters thank you for playing.")
            time.sleep(1)
            print("You are awesome no matter what!\n")
            time.sleep(2)
            print(" ***  Bye!  ***")
            break  # Exit the game

        if not move_snake_safe(snake, key, grid_size):
            print("Try a different move.")

# Run the game
interactive_snake_game()
