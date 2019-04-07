import random

THETA = 50.0
ALPHAS = 50

class Pop(object):
    
    def __init__(self, xpos, ypos, vx, vy, category, psize, hp):
        self.x = xpos
        self.y = ypos
        self.vx = vx
        self.vy = vy
        self.ctg = category
        self.psize = psize
        self.hp = hp
        
    def grow(self,food):
        # self.x += (random.random()-0.5)*1/self.psize*0.1
        # self.y += (random.random()-0.5)*1/self.psize*0.1
        None
        
    def display(self):
        # background(0)
        self.x += (random.random()-0.5)*THETA*self.psize/self.psize
        self.y += (random.random()-0.5)*THETA*self.psize/self.psize
        if self.ctg == 0:
            fill(255,0,0,ALPHAS)
        elif self.ctg == 1:
            fill(0,255,0,ALPHAS)
        elif self.ctg == 2:
            fill(0,0,255,ALPHAS)
        if self.x >= width:
            self.x = width-10
        elif self.x <= 0:
            self.x = 10
        if self.y >= height:
            self.y = height-10
        elif self.y <= 0:
            self.y = 10
        ellipse(self.x,self.y,self.psize,self.psize)
        
    def eat(self,obj):
        if self.ctg == 2 and obj.ctg == 0:
            obj.ctg = 2
        elif self.ctg == 2 and obj.ctg == 1:
            self.ctg = 1
            # print('red -> blue')
        elif self.ctg == 1 and obj.ctg == 0:
            self.ctg = 0
        elif self.ctg == 1 and obj.ctg == 2:
            obj.ctg = 1
        elif self.ctg == 0 and obj.ctg == 1:
            obj.ctg = 0
        elif self.ctg == 0 and obj.ctg == 2:
            self.ctg = 2
        else: None
