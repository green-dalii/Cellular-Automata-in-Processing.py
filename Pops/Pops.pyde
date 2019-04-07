import random
from pop import Pop

def rule(obj1,obj2):
    x1 = obj1.x
    x2 = obj2.x
    y1 = obj1.y
    y2 = obj2.y
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)

NUMBER = 400
SIZE = 20

def setup():
    size(1000,800)
    noStroke()
    frameRate(8000)
    background(0)
    global popList
    # p1= Pop(200,200,0,0,0,20,0)
    popList = []
    for i in range(NUMBER):
        popList.append(Pop(width*random.random(),height*random.random(),0,0,random.randint(0,2),SIZE,0))
        print(popList[-1].ctg,popList[-1].x,popList[-1].y)
    
def draw():
    background(0)
    for each1 in popList:
        pList=list(popList)
        pList.remove(each1)
        for each2 in pList:
            distance = rule(each1,each2)
            if distance <= SIZE*SIZE*4:
                each1.eat(each2)
                each1.display()
                each2.display()
    
    
