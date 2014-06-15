import os
import pygame
import const

def load_image(name, width=const.WINDOW_WIDTH, height = const.WINDOW_HEIGHT):
    fullname = os.path.join('content', name)
    try:
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (width, height))
    except pygame.error:
        print 'Cannot load image:', name
        raise SystemExit
    image = image.convert()
    return image


def rounded_rect(rect, color, radius=0.4):
    rect = pygame.Rect(rect)
    color = pygame.Color(color)
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = pygame.Surface(rect.size, pygame.SRCALPHA)

    circle = pygame.Surface([min(rect.size)*3]*2, pygame.SRCALPHA)
    pygame.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = pygame.transform.smoothscale(circle, [int(min(rect.size)*radius)]*2)

    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

    rectangle.fill(color, special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MIN)

    return rectangle