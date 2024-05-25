import pygame
import sys
from utils import scale_background

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("./audios/Uchiagehanabi.wav")

class PassScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = scale_background('img/pass.png', screen.get_width(), screen.get_height())
        self.font = pygame.font.Font(None, 36)  # None indicates using the default font
        self.is_running = True
        pygame.mixer.music.play(-1)

    def draw(self):
        # Draw background
        self.screen.blit(self.background_image, (0, 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def run(self):
        while self.is_running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(60)