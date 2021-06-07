import pygame
import random

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

def end_message(msg, disp, dis_wid, dis_len, font):
    mesg = font.render(msg, True, red)
    disp.blit(mesg, [dis_wid/2, dis_len/2])
    pygame.display.update()

def update_score(score, disp, dis_wid, dis_len, font):
    mesg = font.render(str(score), True, black)
    disp.blit(mesg, [0, 0])
    
def create_snake(display, x, y, snake_size):
    pygame.draw.rect(display, blue, [x, y, snake_size, snake_size])

def create_esnake(display, coords, counter, esnake_size):
    for index in range(counter + 1):
        pygame.draw.rect(display, green, [coords[index][0], coords[index][1], 10, esnake_size[index]])
        #print(coords[index][0], coords[index][1])
        #print(counter)
        
def grow_snake(display, snake_body, snake_size):
    for x in snake_body:
        pygame.draw.rect(display, blue, [x[0], x[1], snake_size, snake_size])

def create_food(display, x, y, snake_size):
    pygame.draw.rect(display, red, [x, y, snake_size, snake_size])

def move(display, dis_len, dis_wid, snake_size, event):
    
    if event.key == pygame.K_w:
        dx = 0
        dy = -snake_size
    if event.key == pygame.K_a:
        dx = -snake_size
        dy = 0
    if event.key == pygame.K_s:
        dx = 0
        dy = snake_size
    if event.key == pygame.K_d:
        dx = snake_size
        dy = 0
    
    return dx, dy

def game_loop(display, display_width, display_length, clock, snake_size, snake_speed, font):
    
    x = display_width/2
    y = display_length/2

    snake_len = 1
    snake_body = []
    
    foodx = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, display_length - snake_size) / 10.0) * 10.0

    esnake_c = 0
    esnake_coords = []
    esnake_singCoords = []
    esnake_sizeL = []
            
    ex = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    ey = round(random.randrange(0, display_length - snake_size) / 10.0) * 10.0
    esnake_size = round(random.randrange(20, 70) / 10.0) * 10.0

    esnake_singCoords.append(ex)
    esnake_singCoords.append(ey)
    esnake_sizeL.append(esnake_size)
    esnake_coords.append(esnake_singCoords)
    
    x_change = 0
    y_change = 0

    score = 0
    update_score(str(score), display, display_width, display_length, font)
    
    game_over = False
    game_close = False
    while not game_over:
        
        while game_close == True:
            display.fill(white)
            end_message("You loser. Press Q to quit or C to play again.", display, display_width, display_length, font)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop(display, display_width, display_length, clock, snake_size, snake_speed, font)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                x_change, y_change = move(display, display_length, display_width, snake_size, event)
        
        if x >= display_width or x <= 0 or y >= display_length or y <= 0:
            game_close = True

        x += x_change    
        y += y_change

        display.fill(white)
        create_food(display, foodx, foody, snake_size)
        create_snake(display, x, y, snake_size)
        create_esnake(display, esnake_coords, esnake_c, esnake_sizeL)

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_len:
            del snake_body[0]

        for index in snake_body[:-1]:
            if index == snake_head:
                game_close = True

        grow_snake(display, snake_body, snake_size)
        update_score(score, display, display_width, display_length, font)
        pygame.display.update()
        
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, display_length - snake_size) / 10.0) * 10.0
            score += 1
            snake_len += 1

        if score % 5 == 0 and score != 0 and score // 5 > esnake_c:
            ex = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            ey = round(random.randrange(0, display_length - snake_size) / 10.0) * 10.0
            esnake_singCoords = []
            esnake_singCoords.append(ex)
            esnake_singCoords.append(ey)
            esnake_coords.append(esnake_singCoords)
            esnake_size = round(random.randrange(20, 70) / 10.0) * 10.0
            esnake_sizeL.append(esnake_size)
            esnake_c += 1
            
        for i in range(len(esnake_coords)):
            if x == esnake_coords[i][0] and y in range(int(esnake_coords[i][1]), int(esnake_coords[i][1]) + int(esnake_size)):
                game_close = True
                
        clock.tick(snake_speed) #snake speed

    pygame.quit()
    quit()


def init_game():
    clock = pygame.time.Clock()

    display_width = 1200
    display_length = 600

    snake_size = 10
    snake_speed = 20
    
    pygame.init()
    font = pygame.font.SysFont(None, 50)
    display = pygame.display.set_mode((display_width, display_length))
    pygame.display.update()

    game_loop(display, display_width, display_length, clock, snake_size, snake_speed, font)

def main():
    init_game()
    
main()
