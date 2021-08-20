import pygame
from plane_sprites import *
github
pygame.init()
class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 100)
    def __create_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.bullets = Bullet()
        # self.bullets.rect.bottom = self.hero.rect.top
        # self.bullets_group = pygame.sprite.Group


    def start_game(self):
        print("游戏开始...")
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__updata_sprites()
            pygame.display.update()

    def __event_handler(self):
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
                # print('敌机出场...')
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print('向右移动...')
            elif event.type == HERO_FIRE_EVENT and keys_pressed[pygame.K_SPACE]:
                self.hero.fire()
        # keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            # print('向右移动...')
            self.hero.speed = 4
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -4
        else:
            self.hero.speed = 0
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, False)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()
    def __updata_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
