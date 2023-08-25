from generate import Generate
from maze import Maze
import os

generator = Generate()
for i in range(5, 22, 2):
    os.mkdir(f'mazelength{i}')
    for j in range(5):
        width, height = (i, i)
        maze = generator.generate_maze(width, height)
        generator.print_maze(maze, f'mazelength{i}/maze{j + 1}.txt')




for i in range(5, 22, 2):
    os.mkdir(f"solvedmaze{i}")
    for j in range(5):
        m = Maze(f'mazelength{i}/maze{j + 1}.txt')
        print("Solving...")
        m.solve()
        print("States Explored:", m.num_explored)
        m.output_image(f"solvedmaze{i}/maze{j + 1}.png", show_explored=True)