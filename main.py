import pygame
from pygame.math import Vector2
import config
# setting screen size
screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()

running = True
begin = True

snake_rect = None
snake_parts = None
snake_direction = None
snake_length = None

while running:
    if begin:
        begin = False
        #左上角座標為 (200, 200)，寬度為 20 像素，高度為 20 像素的矩形。
        snake_rect = pygame.rect.Rect(200,200,config.SNAKE_PART_SIZE,config.SNAKE_PART_SIZE)
        snake_parts = []
        snake_direction = Vector2(0,20)
        snake_length = 1
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or 
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            running = False
    
    screen.fill(config.BG_COLOR)
    
    for i in range(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE):
        #20條直線
        pygame.draw.line(screen, config.GRID_COLOR, (i,0), (i,config.SCREEN_SIZE))
        #20條橫線
        pygame.draw.line(screen, config.GRID_COLOR, (0,i), (config.SCREEN_SIZE,i))
    
    #行走方向
    snake_rect.move_ip(snake_direction)
    
    #讓蛇慢慢變長
    snake_parts.append(snake_rect.copy())
    #表示從列表最後的元素往前取 snake_length 個元素
    snake_parts = snake_parts[-snake_length:]
    [pygame.draw.rect(screen, "red", snake_part)
        for snake_part in snake_parts]    

    
    #將緩衝區的內容顯示到實際的螢幕上
    pygame.display.flip()
    
    clock.tick(config.FPS)
        
    
    
pygame.quit()