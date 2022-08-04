import pygame, sys, math
from pygame import *
import random

def ballphf():
    global ball_speedx, ball_speedy, player_score, opponent_score
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0:
        ball_speedy = 7*random.uniform(2, 100000)%10
    if ball.bottom >= screen_length:
        ball_speedy = -(7*random.uniform(2, 100000)%10)
    if ball.left <= 0:
        ball_restart()
        player_score += 1 
    if ball.right >= screen_width:
        ball_restart()
        opponent_score += 1

#    if ball.colliderect(player) or ball.colliderect(opponent):
#        ball_speedx *= -1

    if ball.colliderect(player):
        ball_speedx *= -1
        """if ball.center > player.center:
            ball_speedy = 7*random.uniform(2, 100000)%10
            ball_speedx *= -1
        elif ball.center < player.center:
            ball_speedy = -7*random.uniform(2, 100000)%10
            ball_speedx *= -1"""
    
    if ball.colliderect(opponent):
        if ball.center > opponent.center:
            ball_speed = 7*random.uniform(2, 100000)%10
            ball_speedx *= -1
        elif ball.center < opponent.center:
            ball_speedy = -7*random.uniform(2, 100000)%10
            ball_speedx *= -1

    if ball.colliderect(obbstical1):
        if ball.colliderect(obbstical1) and ball.bottom <= obbstical1.top + 7:
            ball_speedy = -1
        elif ball.colliderect(obbstical1) and ball.top >= obbstical1.bottom -7:
            ball_speedy = 1
        else:ball_speedx *= -1
    
    if ball.colliderect(obbstical2):
        if ball.colliderect(obbstical2) and ball.bottom <= obbstical2.top + 7:
            ball_speedy = -1
        elif ball.colliderect(obbstical2) and ball.top >= obbstical2.bottom -7:
            ball_speedy = 1
        else:ball_speedx *= -1

    if ball.colliderect(obbstical3):
        if ball.colliderect(obbstical3) and ball.bottom <= obbstical3.top + 7:
            ball_speedy = -1
        elif ball.colliderect(obbstical3) and ball.top >= obbstical3.bottom -7:
            ball_speedy = 1
        else:ball_speedx *= -1
    
    if ball.colliderect(obbstical4):
        if ball.colliderect(obbstical4) and ball.bottom <= obbstical4.top + 7:
            ball_speedy = -1
        elif ball.colliderect(obbstical4) and ball.top >= obbstical4.bottom -7:
            ball_speedy = 1
        else:ball_speedx *= -1     
    
    if ball.colliderect(obbstical5):
        if ball.colliderect(obbstical5) and ball.bottom <= obbstical5.top + 7:
            ball_speedy = -1
        elif ball.colliderect(obbstical5) and ball.top >= obbstical5.bottom -7:
            ball_speedy = 1
        else:ball_speedx *= -1
    
    if ball.colliderect(obbstical6):
        if ball.colliderect(obbstical6) and ball.bottom <= obbstical6.top + 7:
            ball_speedy = -1
        elif ball.colliderect(obbstical6) and ball.top >= obbstical6.bottom -7:
            ball_speedy = 1
        else:ball_speedx *= -1    

def playerphf():
    global player_speed
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_length:
        player.bottom = screen_length

def opponent_ai():
    """if difficulty.lower() == "easy" or difficulty.lower() == "e":
        if (opponent.top) < ball.y:
            opponent.top += opponent_speed
        if (opponent.bottom) > ball.y:
            opponent.bottom -= opponent_speed
    elif difficulty.lower() == "hard" or difficulty.lower() == "h":
        if (opponent.top+46) < ball.top:
            opponent.top += opponent_speed
        if (opponent.bottom-46) > ball.bottom:
            opponent.bottom -= opponent_speed
    else:
        if (opponent.top+23) < ball.y:
            opponent.top += opponent_speed
        if (opponent.bottom-23) > ball.y:
            opponent.bottom -= opponent_speed"""
    if (opponent.top+110) < ball.top:
        opponent.top += opponent_speed
    if (opponent.bottom-110) > ball.bottom:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_length:
        opponent.bottom = screen_length

def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (screen_width/2, screen_length/2)
    ball_speedx *= random.choice((1,-1))
    ball_speedy *= random.choice((1,-1))

#difficulty = input("Hard, Normal, Easy (h/e/(anything for normal))\n")

pygame.init()
clock = pygame.time.Clock()
#game window
screen_width = 1000
screen_length = screen_width*0.562
screen = pygame.display.set_mode((screen_width,screen_length))
pygame.display.set_caption("Lord of the Pong: Return of the Pong extended edition")

#game rects
ball = pygame.Rect(screen_width/2 - 15, screen_length/2 - 15, 30,30)
player = pygame.Rect(screen_width-20, screen_length/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_length/2 - 70, 10,140)

#obsticles
obbstical1 = pygame.Rect(random.randint(30, screen_width-110), random.randint(0,screen_length), random.randint(10,80),random.randint(10,80))
obbstical2 = pygame.Rect(random.randint(30, screen_width-110), random.randint(0,screen_length), random.randint(10,80),random.randint(10,80))
obbstical3 = pygame.Rect(random.randint(30, screen_width-110), random.randint(0,screen_length), random.randint(10,80),random.randint(10,80))
obbstical4 = pygame.Rect(random.randint(30, screen_width-110), random.randint(0,screen_length), random.randint(10,80),random.randint(10,80))
obbstical5 = pygame.Rect(random.randint(30, screen_width-110), random.randint(0,screen_length), random.randint(10,80),random.randint(10,80))
obbstical6 = pygame.Rect(random.randint(30, screen_width-110), random.randint(0,screen_length), random.randint(10,80),random.randint(10,80))
random.randint(30, screen_width-30), random.randint(0,screen_length)

#game vari
ballc = (255,0,0)
playersc = (200,200,200)
bg_color = (0,0,0)
box_color = (20,230,159)
ball_speedx = 7 * random.choice((1,-1))
ball_speedy = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
# text vari
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7

    
    ballphf()
    playerphf()
    opponent_ai()
    

    screen.fill(bg_color)
    pygame.draw.rect(screen, playersc, player)
    pygame.draw.rect(screen, playersc, opponent)
    pygame.draw.aaline(screen,playersc, (screen_width/2,0), (screen_width/2,screen_length))
    pygame.draw.rect(screen, box_color, obbstical1)
    pygame.draw.rect(screen, box_color, obbstical2)
    pygame.draw.rect(screen, box_color, obbstical3)
    pygame.draw.rect(screen, box_color, obbstical4)
    pygame.draw.rect(screen, box_color, obbstical5)
    pygame.draw.rect(screen, box_color, obbstical6)
    
    player_text = game_font.render(f"{player_score}", False, playersc)
    screen.blit(player_text,((screen_width/2)+10,10))
    opponent_text = game_font.render(f"{opponent_score}", False, playersc)
    screen.blit(opponent_text,((screen_width/2)-24,10))
    
    if player_score >= 7:
        win_text = game_font.render(f"You win", False, playersc)
        screen.blit(win_text,((screen_width/2)-62.5,(screen_length/2)-45))
    if opponent_score >= 7:
        lose_text = game_font.render(f"You lose", False, playersc)
        screen.blit(lose_text,((screen_width/2)-62.5,(screen_length/2)-45))
    
    pygame.draw.ellipse(screen, ballc, ball)

    pygame.display.flip()
    clock.tick(60)
    #crash=0
    if player_score == 7 or opponent_score == 7:
        pygame.time.delay(3000)
        quit()
        "while True:crash += 1000000000000000000000000"