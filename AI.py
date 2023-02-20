from queue import PriorityQueue

from const import *

class AI:
    def __init__(self, pos):
        self.body = pos[1:]
        self.head = pos[0]

        self.grid = []

        self.path = []

        for r in range(int(WIDTH / CELL_SIZE)):
            self.grid.append([])
            for c in range(int(WIDTH / CELL_SIZE)):
                self.grid[r].append((r, c))

    def h(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, came_from, current):

        while current in came_from:
            current = came_from[current]
            self.path.append(current)


    def update_neighbors(self, grid, pos):
        neighbors = []
        row, col = pos
        if row < (WIDTH / CELL_SIZE) - 1 and not grid[row + 1][col] in self.body: # DOWN
            neighbors.append(grid[row + 1][col])

        if row > 0 and not grid[row - 1][col] in self.body: # UP
            neighbors.append(grid[row - 1][col])

        if col < (WIDTH / CELL_SIZE) - 1 and not grid[row][col + 1] in self.body: # RIGHT
            neighbors.append(grid[row][col + 1])

        if col > 0 and not grid[row][col - 1] in self.body: # LEFT
            neighbors.append(grid[row][col - 1])

        return neighbors


    def algorithm(self, grid, start, end):
        self.path = []
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}
        g_score = {spot: float("inf") for row in grid for spot in row}
        g_score[start] = 0
        f_score = {spot: float("inf") for row in grid for spot in row}
        f_score[start] = self.h(start, end)

        open_set_hash = {start}

        while not open_set.empty():

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                self.reconstruct_path(came_from, end)
                return True

            neighbors = self.update_neighbors(self.grid, current)

            for neighbor in neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.h(neighbor, end)
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)


        return False

    def get_path(self):
        return self.path

