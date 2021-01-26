import random
import pygame

SCREEN_RECT = pygame.rect.Rect(0, 0, 480, 700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')
        if is_alt == True:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -  SCREEN_RECT.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./images/enemy1.png')
        self.speed = random.randint(1,3)
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.rect.bottom = 0

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除...")
            self.kill()




class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__('./images/me1.png', speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")

        bullet = Bullet()
        bullet.rect.bottom = self.rect.top + 5
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -5)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
    def __del__(self):
        print('子弹被销毁...')








