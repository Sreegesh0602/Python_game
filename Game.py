#Libraries
import random
import pygame


# initializing pygame
pygame.init()
pygame.font.init()

# Creating the Screen/Window
bg_color=(200,200,200)        # Bgcolor
screen = pygame.display.set_mode((1000,700))         #DisplaySize
pygame.display.set_caption("Snake Game ")           #Title
bg_color=pygame.image.load(("C:\All\Programming\Python\SnakeGame\Photos\grass.jpeg"))
food = pygame.image.load("C:\\All\\Programming\\Python\\SnakeGame\Photos\\apple.jpg")
#Dimension of the object
snake_x=500
snake_y=500


# Initial Position of food
food_x=random.randint(0,900)
food_y=random.randint(0,600)

# Size of the Object
width = 20;
height = 20
# Speed
vel =5
# Initial Score
score=0

#Fill the bg
# use flip to apply all the changes
pygame.display.flip()

# Score read
# font = pygame.font.SysFont("Courier",55)
font = pygame.font.SysFont(None, 30)
def on_screen_text(text,color,x,y):
    screen_text=font.render(text,True,color)
    screen.blit(screen_text,[x,y])

# Snake
length=18
color=240
# body=[]
def body(length,color):
    pygame.draw.rect(screen, (color, 0, 0), (snake_x+length, snake_y, width + length, height+18))



def snake(length,color):
    pygame.draw.rect(screen, "black", (snake_x, snake_y, width + 18, height+18))
    pygame.draw.rect(screen, (color, 0, 0), (snake_x+38, snake_y, width + length, height+18))




# Food
def food_Pos():
    screen.blit(food,(food_x,food_y))

def RestartGame():
    screen.blit(bg_color, (0, 0))
    on_screen_text(("Score : "+str(score)),"red",0,0)
    food_Pos()
    snake(length,color)
    pygame.display.update()


# To let the window to be open
run = True
while run:
    pygame.time.delay(25)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run=False





    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_x>0:
            snake_x-=vel

    if keys[pygame.K_RIGHT] and snake_x<980:
        snake_x+=vel

    if keys[pygame.K_UP] and snake_y>0:
        snake_y-=vel

    if keys[pygame.K_DOWN] and snake_y<680:
        snake_y+=vel

    if abs(snake_x-food_x)<13 and abs(snake_y-food_y)<13:
        score+=5
        length+=18
        color-=8
        food_x = random.randint(0, 900)
        food_y = random.randint(0, 600)


    RestartGame()



pygame.quit()