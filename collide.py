import pygame
import random

pygame.init()

width = 1500
height = 750

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("collide shapes")

black = (0,0,0)
white = (255,255,255)

font = pygame.font.Font(None, 36)  

text = "Press Enter to Play"  # The text you want to display
text_surface = font.render(text, True, white)
text_x = (width/2) - 100
text_y = (height/2)/2

# pygame.Rect() helps to interact with the attributes of rectangle like x,y,width,height.
# it itself is a class thus no need for us to create class.

player1_paddle = pygame.Rect(width - (width - 30),height - (height - 30),30,90) 
player2_paddle = pygame.Rect(width - 60,height - 120,30,90)
paddle_speed = 7
speed_factor = 1
ball_x = (width/2) - 20
ball_y = (height/2) - 20

ball = pygame.Rect(ball_x,ball_y,25,25)

ball_speed_x = random.choice([-1, 1])*random.uniform(3, 5)
ball_speed_y = random.choice([-1, 1])*random.uniform(3, 5)
 # give DIRECTION & SPEED ---
 # choice = left or right & up or down    # uniform = random selection from 3,5 pixels movement in chosed direction
        
 # once direction & speed is chosen, UPDATE ball co-ords.
# ball.x += ball_speed_x
#ball.y += ball_speed_y

clock = pygame.time.Clock()

running = True
wait_for_enter = True
show_text = True


while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
            
    # DISPLAY instruction
    screen.fill(black)
    if show_text:
        screen.blit(text_surface, (text_x, text_y))
    
    keys = pygame.key.get_pressed()

# FOR PADDLES ---------------------------------
    if keys[pygame.K_w]:
        player1_paddle.y -= paddle_speed
    if keys[pygame.K_s]:
        player1_paddle.y += paddle_speed
    if keys[pygame.K_UP]:
        player2_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        player2_paddle.y += paddle_speed

    # max - gives max, but when LHS = RHS i.e. 0 it would return 0, thus no movement , thus paddle stops
    # min - gives min, -||- here is (height - paddle.height) 750-90 = 640
    player1_paddle.y = max(player1_paddle.y,0)
    player1_paddle.y = min(player1_paddle.y, height - player1_paddle.height)
    
    player2_paddle.y = max(player2_paddle.y,0)
    player2_paddle.y = min(player2_paddle.y, height - player2_paddle.height)

# FOR BALL------------------------------------------------------------------------
    if wait_for_enter:
        if keys[pygame.K_RETURN]:
            wait_for_enter = False
            show_text = False
    else:
        ball.x += ball_speed_x
        ball.y += ball_speed_y 
        
    # RESET ball if went PAST PADDLE
    if ball.x <= 0 or ball.x + ball.width >= width:
        ball.x = (width/2) - 20
        ball.y = (height/2) - 20
        speed_factor = 1
        ball_speed_x = random.choice([-1, 1]) * random.uniform(3, 5)
        ball_speed_y = random.choice([-1, 1]) * random.uniform(3, 5)
        wait_for_enter = True
        show_text = True
    # COLLISION with upper nd lower WALL
    if ball.y +ball.height<= 0 or ball.y+ ball.height >= height:
        ball_speed_y *= -1
    
    # COLLISION DETECTION between paddles nd ball------------

    def checkCollision(rect1,rect2):
        return(rect1.x < rect2.x + rect2.width and
                rect1.x + rect1.width > rect2.x and
                rect1.y < rect2.y + rect2.height and
                rect1.y + rect1.height > rect2.y)

    if checkCollision(player1_paddle,ball) or checkCollision(player2_paddle,ball):
        ball_speed_x = (ball_speed_x * -1)
    

# DISPLAY ------------------------------------------------------------------------
    #screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, player1_paddle)
    pygame.draw.rect(screen, white, player2_paddle)

    pygame.draw.rect(screen, white, ball,20,20,20,20,20,20)

    # pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_radius)
    

    # Update the display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
