import random

class Generate():
    def generate_maze(self, width, height):
        # Initialize the maze grid
        maze = [[1] * width for _ in range(height)]
        
        def is_valid(x, y):
            return 0 <= x < width and 0 <= y < height
        
        def get_neighbours(x, y):
            neighbours = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
            valid_neighbours = [(nx, ny) for nx, ny in neighbours if is_valid(nx, ny)]
            random.shuffle(valid_neighbours)
            return valid_neighbours
        
        def carve_path(x, y):
            maze[y][x] = 0
            
            neighbours = get_neighbours(x, y)
            for nx, ny in neighbours:
                if maze[ny][nx] == 1:
                    mid_x, mid_y = (x + nx) // 2, (y + ny) // 2
                    maze[mid_y][mid_x] = 0
                    carve_path(nx, ny)
        
        start_x, start_y = 0, 0
        carve_path(start_x, start_y)
        
        # Add an end point on the bottom-right side
        maze[height - 1][width - 1] = 0
        
        return maze

    def print_maze(self, maze, filename):
        file = open(filename, 'w')
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 1:
                    file.write('#')
                elif (x, y) == (0, 0):
                    file.write('A')
                elif (x, y) == (len(row) - 1, len(maze) - 1):
                    file.write('B')
                else:
                    file.write(' ')
            file.write('\n')
