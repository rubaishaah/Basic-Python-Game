import pygame
import time
import random
pygame.font.init()

# create a window
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT)) # load image to pygame

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_VEL = 3

FONT = pygame.font.SysFont("arial", 30)

STAR_WIDTH = 10
STAR_HEIGHT = 20

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0)) # blit to draw an image to screen

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "White")
    WIN.blit(time_text, (10,10))

    pygame.draw.rect(WIN, "blue", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    
    pygame.display.update()



def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()

    start_time = time.time() # grabs current time
    elapsed_time = 0

    star_add_increment = 2000 
    star_count = 0

    stars = [] # store stars currently on screen

    hit = False

    # main loop to run the game
    while run:
        star_count += clock.tick(100)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get(): #tracks events
            if event.type == pygame.QUIT:
                run = False
                break

            # moving the rectangle around
            keys = pygame.key.get_pressed() #gives a list of keys user has pressed and tell if they've pressed or not
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0: # left key is pressed
                player.x -= PLAYER_VEL #subtract x coordinate
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL <= WIDTH: 
                player.x += PLAYER_VEL
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(player, elapsed_time, stars)
    pygame.quit()


# running the python file and not importing it
if __name__ == "__main__" :
    main()
