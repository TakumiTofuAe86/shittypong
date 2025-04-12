import pygame
import sys

pygame.init()

#screen
WIDTH, HEIGHT = 1280, 720
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Shitty Pong')

#colors
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

#paddles and ball
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE=10
ball_speed_x, ball_spedd_y=5, 5

#creating obj
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT) 
right_paddle=pygame.Rect(WIDTH-30 - PADDLE_WIDTH, HEIGHT// 2- PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

#game cycle
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      sys.exit()
  keys = pygame.key.get_pressed()

  #paddle movement
  if keys[pygame.K_w] and left_paddle.top > 0:
    left_paddle.y -= 5
  if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
    left_paddle.y += 5  
  if keys[pygame.K_UP]and right_paddle.top > 0:
    right_paddle.y -=5
  if keys[pyagme.K_DOWN] and right_paddle.bottom < HEIGHT:
    right_paddle.y += 5

  #ball movement
  ball.x += ball_speed_x
  ball.y += ball_speed_y

  if ball.top <= 0 or ball.bottom >= HEIGHT:
    ball_speed_y *= -1
  if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
    ball_speed_x *= -1

  if ball.left <= 0 orball.right >= WIDTH:
    ball_x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x *= -1

  screen.fill(BLACK)
  pygame.draw.rect(screen, WHITE, left_paddle)
  pygame.draw.rect(screen,WHITE, right_paddle)
  pygame.draw.ellipse(screen, WHITE, ball)

  pygame.display.flip()
  pygame.time.Clock().tick(60)
