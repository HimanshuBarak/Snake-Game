import pygame
import time
import random

pygame.init()                                                              #intializes all the pygame modules

black=(0,0,0)
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

dis_width=400
dis_height=300

snake_speed=17
s_block=10

dis =pygame.display.set_mode((dis_width, dis_height))                         #creates the gaming window

pygame.display.update()                                                      # updates  changes made to  window
pygame.display.set_caption("My first Snake Game")                            #sets the caption

clock =pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift",25)                          #sets the display font for your message
score_font = pygame.font.SysFont("comicsansms",35)

def player_score(score):                                                      #function to print the score
     value = score_font.render("Player Score: "+str(score), True, green)      # to dra tet on  a new surface  
     dis.blit(value,[0,0])

def make_snake(s_block,snake_List):                                            #function to print the snake 
        for x in snake_List:
             pygame.draw.rect(dis,red,[x[0],x[1],s_block,s_block])

def message(mesg,color):
      mssg=font_style.render(mesg,True,color)
      dis.blit(mssg,[dis_width/6,dis_height/3])                              #draws one image onto another

def gameloop():                                   #creating a function so that the game can be playes again nd again by  calling this func
    game_over=False
    game_close=False
    x = dis_width/2
    y = dis_height/2
    xchange = 10
    ychange = 0
    snake_List = []
    s_length=1
    foodx =round(random.randrange(0,dis_width - s_block)/10)*10   #the foodx nd foody hv to be multiples of 10 only than can they overlap with the snake
    foody =round(random.randrange(0,dis_height - s_block)/10)*10

    while not game_over:

      while game_close == True:
        dis.fill(white)
        message("Play again : R   Quit game : Q",black) 
        player_score(s_length - 1) 
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over=True
                    game_close=False
                if event.key == pygame.K_r:
                    gameloop()  
            elif event.type == pygame.QUIT:
                 game_over = True
                 game_close = False          


      for event in pygame.event.get():                                                                  #pygame.event.get is basically a queue that stores all the user inputs
           if event.type==pygame.QUIT:                                     # closes the gaming window when clicked on X button
               game_over=True
           if event.type==pygame.KEYDOWN:                         #pygame.event.get is basically a queue that stores all the user inputs/events
              if event.key == pygame.K_LEFT:
                   xchange = -s_block
                   ychange = 0
              elif event.key==pygame.K_RIGHT:
                   xchange = s_block
                   ychange = 0  
              elif event.key==pygame.K_UP:
                   xchange = 0
                   ychange = -s_block   
              elif event.key==pygame.K_DOWN:
                   xchange = 0
                   ychange = s_block 

      if x >=dis_width or x<0 or y<0 or y>=dis_height:                  # if the snakes touches the boundry the game is over   
           game_close=True 

      x = x+xchange                                                  #this is kind of the reason why the snake keeps on movin in the same dirn 
      y = y+ychange                                                  #coz once we set the direction we set values of xchange nd ychange and these keep changing values of x and y
      dis.fill(black)   
                                                 
      pygame.draw.rect(dis,blue,[foodx,foody,s_block,s_block])                            
     
      snake_head = []
      snake_head.append(x)
      snake_head.append(y)
      snake_List.append(snake_head)
      
      if len(snake_List)> s_length:                      #basically maintains the lenght of the string and deletes extra coordinates 
           del snake_List[0]
      
      for cr in snake_List[:-1]:                          #function to end game if the snake head moves into itself         
           if cr == snake_head:                           #the -1 movies the loop to access the snake head coordinates
               game_close = True
      make_snake(s_block,snake_List)   

      pygame.display.update()  
      if x == foodx and y == foody:
         foodx =round(random.randrange(0,dis_width - s_block)/10)*10   #the foodx nd foody hv to be multiples of 10 only than can they overlap with the snake
         foody =round(random.randrange(0,dis_height - s_block)/10)*10
         s_length += 1

      clock.tick(snake_speed)                                           #controls the frame rate


    pygame.quit()            #to quit the game window
    quit()                   #to quit the program

gameloop()