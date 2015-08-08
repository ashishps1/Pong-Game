#ashish_singh
# P.S. run it on www.code-skulptor.org

import simplegui
import random
WIDTH=900
HEIGHT=500
RADIUS=20
PAD_WIDTH=10
PAD_HEIGHT=80
HPW=PAD_WIDTH/2
HPH=PAD_HEIGHT/2
LEFT=True
RIGHT=False
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[4,4]
paddle1_pos=[HPW,HPH]
paddle2_pos=[WIDTH-HPW,HPH]
paddle1_vel=[0,0]
paddle2_vel=[0,0]
score1=0
score2=0
def play():
    music.play()
    
def new_game():
    global paddle1_pos,paddle2_pos,paddle_vel,paddle2_vel
    global score1,score2,ball_vel,ball_pos,score1,score2
    music.play()
    r=1+random.randrange(0,4)
    ball_pos=[WIDTH/2,HEIGHT/2]
    paddle1_pos[1]=HPH
    paddle2_pos[1]=HPH
    ball_vel=[4,4]
    rand(r)
    paddle1_vel[1]=0
    paddle2_vel[1]=0
    score1=0
    score2=0
    
def nohit(r):
    global paddle1_pos,paddle2_pos,paddle_vel,paddle2_vel
    global score1,score2,ball_vel,ball_pos
    ball_pos=[WIDTH/2,HEIGHT/2]
    rand(r)
    

    
def draw(c):
    global paddle1_pos,paddle2_pos,paddle_vel,paddle2_vel
    global score1,score2,pos1,pos2,ball_pos,ball_vel
    
    music.play()
    c.draw_line([WIDTH/2,0],[WIDTH/2,HEIGHT],1,"White")
    c.draw_line([PAD_WIDTH,0],[PAD_WIDTH,HEIGHT],1,"White")
    c.draw_line([WIDTH-PAD_WIDTH,0],[WIDTH-PAD_WIDTH,HEIGHT],1,"White")
    
   
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    if (((ball_pos[1]-paddle2_pos[1]<=HPH and ball_pos[1]-paddle2_pos[1]>=-HPH) and ball_pos[0]>WIDTH-PAD_WIDTH-RADIUS) or (ball_pos[1]-paddle1_pos[1]<=HPH and ball_pos[1]-paddle1_pos[1]>=-HPH and ball_pos[0]<RADIUS+PAD_WIDTH) or ball_pos[1]<RADIUS  or ball_pos[1]>HEIGHT-RADIUS-1):
        if ball_pos[0]<RADIUS+PAD_WIDTH:
            ball_vel[0]=-(ball_vel[0])
            if ball_vel[1]>0:
                ball_vel[1]+=0.3
            else:
                ball_vel[1]-=0.3
                
            
        elif ball_pos[1]<RADIUS:
            ball_vel[1]=-(ball_vel[1])
            if ball_vel[0]>0:
                ball_vel[0]+=0.3
            else:
                ball_vel[0]-=0.3
            
        elif ball_pos[0]>(WIDTH-1)-RADIUS-PAD_WIDTH:
            ball_vel[0]=-(ball_vel[0])
            if ball_vel[1]>0:
                ball_vel[1]+=0.3
            else:
                ball_vel[1]-=0.3
        elif ball_pos[1]>(HEIGHT-1)-RADIUS:
            ball_vel[1]=-(ball_vel[1])
            if ball_vel[0]>0:
                ball_vel[0]+=0.3
            else:
                ball_vel[0]-=0.3
           
    

    elif (ball_pos[0]>WIDTH-RADIUS or ball_pos[0]<RADIUS):
        laugh.play()
        if ball_pos[0]<WIDTH/2:
            score2=score2+1
        else :
            score1=score1+1
        ball_vel=[4,4]
        ball_pos=[WIDTH/2,HEIGHT/2]
       
        
        r=1+random.randrange(0,4)
        nohit(r)
        
    
    c.draw_circle(ball_pos,RADIUS,4,"Black","White")
    
    paddle1_pos[1]+=1.5*paddle1_vel[1]
    paddle2_pos[1]+=1.5*paddle2_vel[1]
    if paddle1_pos[1]>=HEIGHT-HPH:
        paddle1_vel[1]=-paddle1_vel[1]
    elif paddle1_pos[1]<=HPH:
        paddle1_vel[1]=-paddle1_vel[1]
        
    if paddle2_pos[1]>=HEIGHT-HPH:
        paddle2_vel[1]=-paddle2_vel[1]
    elif paddle2_pos[1]<=HPH:
        paddle2_vel[1]=-paddle2_vel[1]
        
    c.draw_line([0,paddle1_pos[1]-HPH],[0,paddle1_pos[1]+HPH],PAD_WIDTH,"Green")
    c.draw_line([WIDTH-PAD_WIDTH,paddle2_pos[1]-HPH],[WIDTH-PAD_WIDTH,paddle2_pos[1]+HPH],PAD_WIDTH,"Green")
    c.draw_text('A',[225,40],20,'Blue')
    c.draw_text('B',[650,40],20,'Blue')
    c.draw_text(str(score1),[225,65],20,'Blue')
    c.draw_text(str(score2),[650,65],20,'Blue')
    
def ball_small():
    global RADIUS
    RADIUS=10
def ball_big():
    global RADIUS
    RADIUS=30
def ball_medium():
    global RADIUS
    RADIUS=20    


def keydown(key):
    acc=5
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1]-=acc
        
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1]+=acc
        
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1]-=acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1]+=acc
        

def keyup(key):
    acc=0
    paddle2_vel[1]=acc
    paddle1_vel[1]=acc

def rand(r):
    global ball_vel
    if r==1:
        ball_vel[0]=ball_vel[0]
    elif r==2:
        ball_vel[0]=-ball_vel[0]
    elif r==3:
        ball_vel[1]=-ball_vel[1]
    elif r==4:
        ball_vel[1]=ball_vel[1]    

    
    
    
    
f=simplegui.create_frame("pong",WIDTH,HEIGHT)
f.set_canvas_background("Red")
f.set_draw_handler(draw)
f.add_button("PLAY",play)
f.add_button("NEW GAME",new_game)
f.add_button("small ball",ball_small)
f.add_button("big ball",ball_big)
f.add_button("medium ball",ball_medium)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
laugh = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg")

f.start()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
