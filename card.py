import pygame
import const


class Card:
    def __init__(self, name):
        self.name = name
        self.surface = pygame.Surface((const.CARD_WIDTH, const.CARD_HEIGHT))
        self.surface.fill(pygame.Color(const.CARD_COLOR))
        self.draw_image()

    def draw_image(self):
        if self.name == 'square':
            pygame.draw.rect(self.surface, pygame.Color(const.SQUARE_COLOR), (25, 50, 100, 100))
        elif self.name == 'circle':
            pygame.draw.circle(self.surface, pygame.Color(const.CIRCLE_COLOR), (75, 100), 50)
        elif self.name == 'ellipse':
            pygame.draw.ellipse(self.surface, pygame.Color(const.ELLIPSE_COLOR), (25, 65, 100, 70))
        elif self.name == 'triangle':
            point_list = [(25, 150), (125, 150), (75, 50)]
            pygame.draw.polygon(self.surface, pygame.Color(const.TRIANGLE_COLOR), point_list)
        elif self.name == 'hexagon':
            point_list = []
            pygame.draw.polygon(self.surface, pygame.Color(const.HEXAGON_COLOR), point_list)