#coding:utf-8

filename = "B-large"
fin = open(filename + ".in", "r")
fout = open(filename + ".out", "w")





baise = [(-1,0),(0,-1),(0,1),(1,0)]
arrow = ['?','^','<','>','!']
llmap  = []
label_list = []


def buttom_up(y,x,label,W,H):

    llmap[y][x] = label

    if y != 0:
        if llmap[y-1][x] =='!' :
            buttom_up(y-1, x, label, W, H)
    if x != 0:
        if llmap[y][x-1] =='>' :
            buttom_up(y, x-1, label, W, H)
    if x < W-1:
        if llmap[y][x+1] =='<' :
            buttom_up(y, x+1, label, W, H)
    if y < H-1:
        if llmap[y+1][x] =='^' :
            buttom_up(y+1, x, label, W, H)


def draw(y,x,label,W,H):
    
    temp_label = llmap[y][x]
    llmap[y][x] = label
    
    
    if y != 0:
        if llmap[y-1][x] == temp_label :
            draw(y-1, x, label, W, H)
    if x != 0:
        if llmap[y][x-1] == temp_label :
            draw(y, x-1, label, W, H)
    if x < W-1:
        if llmap[y][x+1] == temp_label :
            draw(y, x+1, label, W, H)
    if y < H-1:
        if llmap[y+1][x] == temp_label :
            draw(y+1, x, label, W, H)
    

if __name__ == '__main__':
    T = int(fin.readline()[:-1])
    print T
    for i in range(T):
        temp = fin.readline()[:-1].split(" ")
        H = int(temp[0])
        W = int(temp[1])
        print H,W
        lamap = []
        llmap = []
        for y in range(H):
            h = fin.readline()[:-1].split(" ")
            
            h = map(lambda x:int(x), h)
            lamap.append(h)
            h = map(lambda x:"?", h)
            llmap.append(h) 
        
        label_list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        label_list.reverse()
        tlabel_list = range(100)[1:]
        tlabel_list.reverse()

        for y in range(H):
            for x in range(W):
                neighbor = [] 
                if y != 0:
                    north = y - 1
                    north_latitue =  lamap[north][x]
                else:
                    north_latitue = 99999
                neighbor.append((north_latitue,1,(-1,0)))
                
                if x != 0:
                    west = x - 1
                    west_latitue = lamap[y][west]
                else: 
                    west_latitue = 99999
                neighbor.append((west_latitue,2,(0,-1)))
                
                if x < W-1:
                    east = x + 1
                    
                    east_latitue = lamap[y][east]
                else:
                    east_latitue = 99999
                neighbor.append((east_latitue,3,(0,1)))
                
                if y < H-1:
                    south = y + 1 
                    south_latitue = lamap[south][x]
                else:
                    south_latitue = 99999
                neighbor.append((south_latitue,4,(1,0)))
                
                neighbor.sort()
                   
                y_basied = neighbor[0][2][0]
                x_basied = neighbor[0][2][1]
                
                if lamap[y][x] > neighbor[0][0]:
                    llmap[y][x] = arrow[neighbor[0][1]]
                else:
                    llmap[y][x] = 'o'
            
        for y in range(H):
            for x in range(W):
                if llmap[y][x] =='o':
                    buttom_up(y,x,tlabel_list.pop(),W,H)
    
        for y in range(H):
            for x in range(W):
                try:
                    if int(llmap[y][x]):
                        draw(y,x,label_list.pop(),W,H) 
                except:
                    pass
        
        fout.write('Case #'+str(i+1)+":\n")
        for p in llmap:
            print p  
            row = ""
            for q in p:
                row = row + q +" "
            fout.write(row[:-1]+"\n")
    

