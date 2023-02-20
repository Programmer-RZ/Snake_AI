import pygame

class Player:
    def __init__(self, screen, cell_size):
        self.screen = screen
        self.cell_size = cell_size

        self.pos = [(2, 2), (1, 2), (0, 2)]
        self.dir_x = 1
        self.dir_y = 0
    
    def draw(self):
        for p in self.pos:
            x, y = p
            pygame.draw.rect(self.screen, 'red4', (x * self.cell_size, y * self.cell_size,
            self.cell_size, self.cell_size))

        xx, yy = self.pos[0]
        pygame.draw.rect(self.screen, 'red', (xx * self.cell_size, yy * self.cell_size, self.cell_size, self.cell_size))
    
    def move(self):
        pos_copy = self.pos[:-1]
        cx, cy = pos_copy[0]
        pos_copy.insert(0, (cx + self.dir_x, cy + self.dir_y))

        self.pos = pos_copy

    def add(self, food):
        fx, fy = food
        hx, hy = self.pos[0]

        if hx == fx and hy == fy:
            self.pos.append(self.pos[-1])
            return True
        else:
            return False

    def get_dir(self, aim):
        ax, ay = aim
        hx, hy = self.pos[0]

        self.dir_x = ax - hx
        self.dir_y = ay - hy

