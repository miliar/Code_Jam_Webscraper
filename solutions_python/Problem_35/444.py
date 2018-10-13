#coding:utf-8
'''
Created on 2009/9/3

@author: Cody
'''
def getXY(ans,H,W):
    for y in range(H):
        for x in range(W):
            if(ans[y][x]==0):
                return True,y,x
    return False,0,0
filename = "B-small-attempt2"
fin = open(filename + ".in", "r")
fout = open(filename + ".out", "w")

mark_index = 0 
baise = [(-1,0),(0,-1),(0,1),(1,0)]
arrow = ['?','^','<','>','!']
label_map  = []
label_list = []
def buttom_up(y,x,label,W,H):

    label_map[y][x] = label

    if y != 0:
        if label_map[y-1][x] =='!' :
            buttom_up(y-1, x, label, W, H)
    if x != 0:
        if label_map[y][x-1] =='>' :
            buttom_up(y, x-1, label, W, H)
    if x < W-1:
        if label_map[y][x+1] =='<' :
            buttom_up(y, x+1, label, W, H)
    if y < H-1:
        if label_map[y+1][x] =='^' :
            buttom_up(y+1, x, label, W, H)
def draw(y,x,label,W,H):
    
    temp_label = label_map[y][x]
    label_map[y][x] = label
    
    
    if y != 0:
        if label_map[y-1][x] == temp_label :
            draw(y-1, x, label, W, H)
    if x != 0:
        if label_map[y][x-1] == temp_label :
            draw(y, x-1, label, W, H)
    if x < W-1:
        if label_map[y][x+1] == temp_label :
            draw(y, x+1, label, W, H)
    if y < H-1:
        if label_map[y+1][x] == temp_label :
            draw(y+1, x, label, W, H)
    

if __name__ == '__main__':
    T = int(fin.readline()[:-1])
    print T
    for i in range(T):
        temp = fin.readline()[:-1].split(" ")
        H = int(temp[0])
        W = int(temp[1])
        print H,W
        latitude_map = []
        label_map = []
        for y in range(H):
            h = fin.readline()[:-1].split(" ")
            #print h
            h = map(lambda x:int(x), h)
            latitude_map.append(h)
            h = map(lambda x:"?", h)
            label_map.append(h) 
        #print latitude_map
        #print label_map
        
        mark_index = 0
        label_list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        label_list.reverse()
        tlabel_list = range(100)[1:]
        tlabel_list.reverse()

        for y in range(H):
            for x in range(W):
                neighbor = [] 
                if y != 0:
                    north = y - 1
                    north_latitue =  latitude_map[north][x]
                else:
                    north_latitue = 99999
                neighbor.append((north_latitue,1,(-1,0)))
                
                if x != 0:
                    west = x - 1
                    west_latitue = latitude_map[y][west]
                else: 
                    west_latitue = 99999
                neighbor.append((west_latitue,2,(0,-1)))
                
                if x < W-1:
                    east = x + 1
                    #print y,east
                    east_latitue = latitude_map[y][east]
                else:
                    east_latitue = 99999
                neighbor.append((east_latitue,3,(0,1)))
                
                if y < H-1:
                    south = y + 1 
                    south_latitue = latitude_map[south][x]
                else:
                    south_latitue = 99999
                neighbor.append((south_latitue,4,(1,0)))
                
                neighbor.sort()
                   
                y_basied = neighbor[0][2][0]
                x_basied = neighbor[0][2][1]
                
                if latitude_map[y][x] > neighbor[0][0]:
                    label_map[y][x] = arrow[neighbor[0][1]]
                else:
                    label_map[y][x] = 'o'
        #draw color     
        for y in range(H):
            for x in range(W):
                if label_map[y][x] =='o':
                    buttom_up(y,x,tlabel_list.pop(),W,H)
    
        for y in range(H):
            for x in range(W):
                try:
                    if int(label_map[y][x]):
                        draw(y,x,label_list.pop(),W,H) 
                except:
                    pass

        fout.write('Case #'+str(i+1)+":\n")
        for p in label_map:
            print p  
            row = ""
            for q in p:
                row = row + q +" "
            fout.write(row[:-1]+"\n")
    
'''

                if latitude_map[y][x] > neighbor[0][0] :  
                    # 1. 他有label , 跟它一樣 , 否則自己創一個新的。
                    if len(label_map[y+y_basied][x+x_basied]) != 0:
                        label = label_map[y+y_basied][x+x_basied][0]  #取第一個代表
                        label_map[y][x].append(label)
                    elif len(label_map[y][x])!= 0:
                        label = label_map[y][x][0]
                        label_map[y+y_basied][x+x_basied].append(label)
                    else :
                        mark_index +=1
                        label = mark_index
                        label_map[y][x].append(label)
                        label_map[y+y_basied][x+x_basied].append(label)
                else:
                    # 沒有自己的 label 
                    if label_map[y][x] == '':
                        label = label_list.pop()
                        label_map[y][x] = label
'''