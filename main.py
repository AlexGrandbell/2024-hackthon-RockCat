import pygame
import sys
from start_screen import StartScreen


def main():

    pygame.init()

    screen_width, screen_height = 1200, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('游戏开始界面')

    # 创建开始界面实例
    start_screen = StartScreen(screen)

    # 运行开始界面
    start_screen.run()  # 修改为调用 run 方法

    # 退出pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
