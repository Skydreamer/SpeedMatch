# -*- coding: utf-8 -*-
import pygame
import const
import misc
import card
import random


class Game:
    def __init__(self):
        self.name = 'Speed Match - Pygame'
        self.background = None
        self.font = None
        self.is_active = True

        self.init_window()
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.load_background()
        self.load_font()

        self.game = SpeedMatch()

    def init_window(self):
        pygame.init()
        pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
        pygame.display.set_caption(self.name)

    def load_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.background = misc.load_image('background.jpg')

    def load_font(self):
        self.font = pygame.font.SysFont('monospace', const.FONT_SIZE)

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_score_cloud(self):
        out = u'ОЧКИ {0}'.format(self.game.score)
        score_label = self.font.render(out, 1, pygame.Color(const.FONT_COLOR))
        surface = pygame.Surface((const.CLOUD_WIDTH, const.CLOUD_HEIGHT))
        surface.set_alpha(const.CLOUD_APLHA)
        surface.fill(pygame.Color(const.CLOUD_COLOR))
        surface.blit(score_label, (10, 5))
        self.screen.blit(surface, (const.WINDOW_WIDTH - const.CLOUD_WIDTH - const.CLOUD_BORDER, 10))

    def draw_multiple_cloud(self):
        out = u'УРОВЕНЬ х{0}'.format(self.game.level)
        tier_label = self.font.render(out, 1, pygame.Color(const.FONT_COLOR))
        surface = pygame.Surface((const.CLOUD_WIDTH, const.CLOUD_HEIGHT))
        surface.set_alpha(const.CLOUD_APLHA)
        surface.fill(pygame.Color(const.CLOUD_COLOR))
        surface.blit(tier_label, (10, 5))
        self.screen.blit(surface, (const.WINDOW_WIDTH - 2 * const.CLOUD_WIDTH - 2 * const.CLOUD_BORDER, 10))

    def draw_time_cloud(self):
        out = u'ВРЕМЯ 0:{0:02.0f}'.format(self.game.timer / 1000)
        state_label = self.font.render(out, 1, pygame.Color(const.FONT_COLOR))
        surface = pygame.Surface((const.CLOUD_WIDTH, const.CLOUD_HEIGHT))
        surface.set_alpha(const.CLOUD_APLHA)
        surface.fill(pygame.Color(const.CLOUD_COLOR))
        surface.blit(state_label, (10, 5))
        self.screen.blit(surface, (const.WINDOW_WIDTH - 3 * const.CLOUD_WIDTH - 3 * const.CLOUD_BORDER, 10))

    def draw_answer_cloud(self):
        if self.game.total_cards > 2:
            if self.game.correct:
                out = u'Правильно!'
            else:
                out = u'Неправильно!'
            answer_label = self.font.render(out, 1, pygame.Color(const.FONT_COLOR))
            surface = pygame.Surface((const.CLOUD_WIDTH, const.CLOUD_HEIGHT))
            surface.set_alpha(const.CLOUD_APLHA)
            surface.fill(pygame.Color(const.CLOUD_COLOR))
            if self.game.correct:
                surface.blit(answer_label, (25, 5))
            else:
                surface.blit(answer_label, (15, 5))
            self.screen.blit(surface, (const.WINDOW_WIDTH / 2 - const.CLOUD_WIDTH / 2, const.WINDOW_HEIGHT / 4.5))

    def draw_info_cloud(self):
        out = u'Совпадает ли ТЕКУЩАЯ карта с ПРЕДЫДУЩЕЙ?'
        info_label = self.font.render(out, 1, pygame.Color(const.FONT_COLOR))
        surface = pygame.Surface((const.CLOUD_WIDTH * 3, const.CLOUD_HEIGHT))
        surface.set_alpha(const.CLOUD_APLHA)
        surface.fill(pygame.Color(const.CLOUD_COLOR))
        surface.blit(info_label, (30, 5))
        self.screen.blit(surface, (const.WINDOW_WIDTH / 2 - const.CLOUD_WIDTH * 1.5, const.WINDOW_HEIGHT / 6))

    def draw_help_clouds(self):
        help_label_left = self.font.render(u'НЕТ', 1, pygame.Color(const.FONT_COLOR))
        help_label_right = self.font.render(u'ДА', 1, pygame.Color(const.FONT_COLOR))

        left_arrow_image = misc.load_image('left_arrow.png', width=50, height=50)
        right_arrow_image = misc.load_image('right_arrow.png', width=50, height=50)

        surface_left = pygame.Surface((const.CLOUD_WIDTH, const.CLOUD_HEIGHT * 2))
        surface_right = pygame.Surface((const.CLOUD_WIDTH, const.CLOUD_HEIGHT * 2))

        surface_left.set_alpha(const.CLOUD_APLHA)
        surface_right.set_alpha(const.CLOUD_APLHA)

        surface_left.fill(pygame.Color(const.CLOUD_COLOR))
        surface_right.fill(pygame.Color(const.CLOUD_COLOR))

        surface_left.blit(help_label_left, (20, 20))
        surface_left.blit(left_arrow_image, (90, 5))
        surface_right.blit(help_label_right, (100, 20))
        surface_right.blit(right_arrow_image, (10, 5))

        self.screen.blit(surface_left, (const.WINDOW_WIDTH / 2 - const.CLOUD_WIDTH - 5, const.WINDOW_HEIGHT - const.CLOUD_HEIGHT * 2))
        self.screen.blit(surface_right, (const.WINDOW_WIDTH / 2 + 5, const.WINDOW_HEIGHT - const.CLOUD_HEIGHT * 2))

    def draw_final_score_cloud(self):
        out = u'РЕЗУЛЬТАТ : {0}'.format(self.game.score)
        state_label = self.font.render(out, 1, pygame.Color(const.FONT_COLOR))
        surface = pygame.Surface((const.CLOUD_WIDTH * 2, const.CLOUD_HEIGHT))
        surface.set_alpha(const.CLOUD_APLHA)
        surface.fill(pygame.Color(const.CLOUD_COLOR))
        surface.blit(state_label, (10, 5))
        screen_center_x = self.screen.get_rect().width / 2
        screen_center_y = self.screen.get_rect().height / 2
        self.screen.blit(surface, (screen_center_x - const.CLOUD_WIDTH, screen_center_y - const.CLOUD_HEIGHT / 2))

    def draw_card(self):
        self.screen.blit(self.game.current_card.surface, (const.WINDOW_WIDTH / 2 - const.CARD_WIDTH / 2,
                                                          const.WINDOW_HEIGHT / 2 - const.CARD_HEIGHT / 2))

    def run(self):
        self.game.start()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if not self.game.game_started:
                        self.game.game_started = True
                    if event.key == pygame.K_LEFT:
                        self.game.check_answer(guess=False)
                    elif event.key == pygame.K_RIGHT:
                        self.game.check_answer(guess=True)

            if self.game.timer <= 0:
                self.game.end_game = True

            if not self.game.end_game:
                self.draw_background()
                self.draw_card()
                self.draw_score_cloud()
                self.draw_multiple_cloud()
                self.draw_time_cloud()
                self.draw_help_clouds()
                self.draw_answer_cloud()
                self.draw_info_cloud()
            else:
                self.draw_final_score_cloud()

            pygame.display.update()

            if self.game.game_started and self.game.timer >= 0:
                self.game.timer -= self.clock.tick(60)
            else:
                self.clock.tick(60)


class SpeedMatch:
    def __init__(self):
        self.score = 0
        self.game_started = False
        self.end_game = False
        self.correct = False
        self.total_cards = 0
        self.correct_cards = 0
        self.correct_streak = 0
        self.timer = 0
        self.level = 1
        self.score_table = list()
        self.current_card = None
        self.previous_card = None
        self.cards = list()

        self.screen = pygame.display.get_surface()
        self.generate_score()
        self.generate_cards()
        self.setup_timer(time=const.TIME)

    def generate_cards(self):
        self.cards.append(card.Card('circle'))
        self.cards.append(card.Card('square'))
        self.cards.append(card.Card('ellipse'))
        self.cards.append(card.Card('triangle'))

    def inc_score(self):
        self.score += self.score_table[self.level - 1]

    def generate_score(self):
        previous = 0
        current = const.BASE_SCORE
        for level in range(1, const.MAX_LEVEL + 1):
            self.score_table.append(current + previous)
            current, previous = current + previous, current

    def next_card(self):
        self.previous_card = self.current_card
        rand_index = random.randrange(0, len(self.cards))
        self.current_card = self.cards[rand_index]
        self.total_cards += 1
        print self.current_card.name

    def level_up(self):
        self.level += 1
        if self.level > const.MAX_LEVEL:
            self.level = const.MAX_LEVEL

    def level_down(self):
        self.level -= 1
        if self.level < 1:
            self.level = 1

    def start(self):
        self.next_card()

    def check_answer(self, guess):
        if self.previous_card and self.current_card:
            if guess == (self.previous_card.name == self.current_card.name):
                self.correct = True
                self.correct_streak += 1
                self.inc_score()
                if self.correct_streak >= 4:
                    self.correct_streak = 0
                    self.level_up()
            else:
                self.correct = False
                if self.correct_streak > 0:
                    self.correct_streak = 0
                else:
                    self.level_down()
        self.next_card()

    def setup_timer(self, time):
        self.timer = time * 1000


if __name__ == '__main__':
    Game().run()