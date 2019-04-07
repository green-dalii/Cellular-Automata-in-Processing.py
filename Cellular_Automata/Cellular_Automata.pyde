import random

SIZE=5
LIVEDPERCENT=0.55

def isLived(px,py):
    brightnum=pixels[(py+SIZE/2)*width+(px+SIZE/2)]
    if brightness(brightnum) == 255:
        return 0  # is Dead
    else:
        return 1  # is Lived
    

def mooreLived(px,py):
    liveNum = 0
    mooreList = []
    row=py/SIZE
    column=px/SIZE
    mooreList.append((column-1,row-1))   # top_left_grid
    mooreList.append((column,row-1))     # top_mid_grid
    mooreList.append((column+1,row-1))   # top_right_grid
    mooreList.append((column-1,row))     # mid_left_grid
    mooreList.append((column+1,row))     # mid_right_grid
    mooreList.append((column-1,row+1))   # bottom_left_grid
    mooreList.append((column,row+1))     # bottom_mid_grid
    mooreList.append((column+1,row+1))   # bottom_right_grid
    for each in mooreList:
        if each[0] < 0 or each[1] < 0 or each[0] >= width/SIZE or each[1] >= height/SIZE:
            liveNum += 0
        else:
            liveNum += isLived(each[0]*SIZE, each[1]*SIZE)
    return liveNum
        

def setup():
    size(1000,1000)
    background(255)
    frameRate(120)
    noStroke()
    num_x = width/SIZE
    num_y = height/SIZE
    livedNum = int(num_x*num_y*LIVEDPERCENT)
    loadPixels()
    global gridList, gridLivedList
    gridList = []
    gridLivedList = []
    for row in range(num_y):
        for column in range(num_x):
            gridList.append(
                            (column*SIZE, row*SIZE)
            )
            if num_x*column+(row+1) <= livedNum:
                gridLivedList.append(1)
            else:
                gridLivedList.append(0)
    random.shuffle(gridLivedList)
    print(gridList)
    for i, element in enumerate(gridList):
        if gridLivedList[i] == 1:
            fill(100)
        else:
            fill(255)
        rect(element[0],element[1],SIZE,SIZE)
    
    # for each in gridList:
    #     mooreLivedCount = mooreLived(each[0], each[1])
    #     print('is XXX!!!',each[0], each[1], (each[1]*SIZE+SIZE/2)*width+(each[0]*SIZE+SIZE/2))
    #     if isLived(each[0], each[1]) == 1:
    #         print('is Living!!!',each[0],each[1])
    #         # if mooreLivedCount == 2 or mooreLivedCount ==3:
    #         #     fill(100)
    #         #     rect(each[0],each[1],SIZE,SIZE)
    #         #     # print('Lived & Living',mooreLivedCount)
    #         # else:
    #         #     fill(255)
    #         #     rect(each[0],each[1],SIZE,SIZE)
    #         #     # print('Lived & Dead',mooreLivedCount)
    #     elif isLived(each[0], each[1]) == 0:
    #         # if mooreLivedCount == 3:
    #         #     fill(100)
    #         #     rect(each[0],each[1],SIZE,SIZE)
    #         #     # print('Dead & Living',mooreLivedCount)
    #         # else:
    #         #     fill(255)
    #         #     rect(each[0],each[1],SIZE,SIZE)
    #         #     # print('Dead & Dying',mooreLivedCount)
    #         None
            

        
def draw():
    loadPixels()
    # mooreLivedCount = mooreLived(mouseX/SIZE*SIZE,mouseY/SIZE*SIZE)
    # mouseAlive = isLived(mouseX/SIZE*SIZE,mouseY/SIZE*SIZE)
    # print(mooreLivedCount,mouseAlive)
    global gridList, gridLivedList
    for i, each in enumerate(gridList):
        # print('Mooring....',each[0],each[1])
        mooreLivedCount = mooreLived(each[0], each[1])
        if isLived(each[0], each[1]) == 1:
            # print('is Living!!!',each[0],each[1])
            if mooreLivedCount == 2 or mooreLivedCount == 3:
                # print('Lived & Living',mooreLivedCount)
                fill(100)
                rect(each[0],each[1],SIZE,SIZE)
                gridLivedList[i] = 1
                # print('Lived -> Living',mooreLivedCount)
            else:
                # print('Lived & Dead',mooreLivedCount)
                fill(255)
                rect(each[0],each[1],SIZE,SIZE)
                gridLivedList[i] = 0
                # print('Lived -> Dead',mooreLivedCount)
        elif isLived(each[0], each[1]) == 0:
            # print('is DEAD!!!',each[0],each[1])
            if mooreLivedCount == 3:
                # print('Dead & Living',mooreLivedCount)
                fill(100)
                rect(each[0],each[1],SIZE,SIZE)
                gridLivedList[i] = 1
                # print('Dead -> Living',mooreLivedCount)
            else:
                # print('Dead & Dying',mooreLivedCount)
                fill(255)
                rect(each[0],each[1],SIZE,SIZE)
                gridLivedList[i] = 0
                # print('Dead -> Dying',mooreLivedCount)
                
    print('Percent of alived:',float(sum(gridLivedList))/len(gridLivedList))
    # for i, element in enumerate(gridList):
    #     if gridLivedList[i] == 1:
    #         fill(100)
    #     else:
    #         fill(255)
    #     rect(element[0],element[1],SIZE,SIZE)
    
def mouseClicked():
    row = mouseX / SIZE
    column = mouseY / SIZE
    fill(100)
    rect(row*SIZE,column*SIZE,SIZE,SIZE)
    
    
    
