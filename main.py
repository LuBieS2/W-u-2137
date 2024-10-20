import pygame
import random
def controls(object, speed, direction):
    keys = pygame.key.get_pressed()
    if direction == "x":
        object.x += speed
    elif direction == "y":
        object.y += speed
    elif direction == "-x":
        object.x -= speed
    elif direction == "-y":
        object.y -= speed
    if keys[pygame.K_w] and (direction == "x" or direction == "-x"):
        direction = "-y"
    elif keys[pygame.K_s] and (direction == "x" or direction == "-x"):
        direction = "y"
    elif keys[pygame.K_a] and (direction == "y" or direction == "-y"):
        direction = "-x"
    elif keys[pygame.K_d] and (direction == "y" or direction == "-y"):
        direction = "x"
    return direction
def main():
    start=False
    death=False
    #screen resolution and basic commands
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Snejku 2137 pozdro")
    X=1000
    Y=1000
    screen = pygame.display.set_mode((X, Y))
    running = True
    d=20
    square = X // d
    #player and apples
    apple_pos=pygame.Vector2(random.randint(0, d-1)*square, random.randint(0, d-1)*square)
    player_pos= pygame.Vector2(0, 0)
    score=0
    pdirection = "x"
    length = [player_pos]
    temp=player_pos
    #font
    font = pygame.font.Font('slkscr.ttf', 40)
    while running:
        length.append(temp)
        screen.fill((0, 0, 0))
        clock.tick(12)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #drawing objects+
        for XY in length:
            pygame.draw.rect(screen, "white", (XY[0], XY[1], square, square), 0)
        pygame.draw.circle(screen, "white", (apple_pos.x+square/2, apple_pos.y+square/2), square/2, 0)
        #getting points
        if player_pos == apple_pos:
            while apple_pos in length:
                apple_pos = pygame.Vector2(random.randint(0, d - 1) * square, random.randint(0, d - 1) * square)
            score+=1
        else:
            length.pop(1)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            start=True
        if start:
            pdirection=controls(length[0], square, pdirection)
        temp=(length[0].x, length[0].y)
        #dying
        if player_pos.x < 0 or player_pos.x > X-1 or player_pos.y < 0 or player_pos.y > Y-1 or length[0] in length[1:]:
            scorep1display = font.render(("YOU LOSE, YOU'VE GOT " + str(score)) + " POINTS", True, (255, 255, 255))
            p1rect = scorep1display.get_rect()
            p1rect.center = (X // 2, Y // 2)
            screen.blit(scorep1display, p1rect)
            running=False
            death=True
        pygame.display.flip()
    while death:
        clock.tick(1)
        death=False
if __name__ == '__main__':
    main()
