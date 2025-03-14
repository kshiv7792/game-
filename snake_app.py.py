import streamlit as st
import random
import time

# Set up the game
st.title("🐍 Snake Game in Streamlit")
st.write("Use the buttons to move the snake!")

# Initialize game variables
GRID_SIZE = 10
WIDTH, HEIGHT = 20, 20
snake = [[10, 10]]
direction = "RIGHT"
food = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
score = 0

# Create buttons for movement
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬆️ Up"):
        if direction != "DOWN":
            direction = "UP"
with col3:
    if st.button("⬇️ Down"):
        if direction != "UP":
            direction = "DOWN"
if st.button("⬅️ Left"):
    if direction != "RIGHT":
        direction = "LEFT"
if st.button("➡️ Right"):
    if direction != "LEFT":
        direction = "RIGHT"

# Move the snake
head = snake[-1].copy()
if direction == "UP":
    head[1] -= 1
elif direction == "DOWN":
    head[1] += 1
elif direction == "LEFT":
    head[0] -= 1
elif direction == "RIGHT":
    head[0] += 1

# Wrap around the grid (no walls)
head[0] %= WIDTH
head[1] %= HEIGHT

# Check for collision with food
if head == food:
    snake.append(food)
    food = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
    score += 1
else:
    snake.append(head)
    snake.pop(0)

# Display game board
st.write(f"Score: {score}")
grid = [["⬛" for _ in range(WIDTH)] for _ in range(HEIGHT)]
grid[food[1]][food[0]] = "🍎"
for x, y in snake:
    grid[y][x] = "🟩"
st.write("\n".join(["".join(row) for row in grid]))

time.sleep(0.2)
st.rerun()
