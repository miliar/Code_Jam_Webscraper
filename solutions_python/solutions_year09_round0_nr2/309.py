#!/usr/bin/env python

import sys

def travel(map,x,y,map_name,next_letter, h, w,xo,yo):
    #print "%s X %s" % (x,y)
    if map_name[y][x] != '.':
        return map_name[y][x]
    else:
        neighbors = [0,0,0,0]
        lowest = sys.maxint
        
        map_min = sys.maxint
        
        #left
        if x > 0:
            neighbors[1] = map[y][x-1]
        else:
            neighbors[1] = sys.maxint
        
        #right
        if x < w-1:
            neighbors[2] = map[y][x+1]
        else:
            neighbors[2] = sys.maxint

        #top
        if y > 0:
            neighbors[0] = map[y-1][x]
        else:
            neighbors[0] = sys.maxint
        
        #bottom
        if y < h-1:
            neighbors[3] = map[y+1][x]
        else:
            neighbors[3] = sys.maxint
        
        lowest = min(neighbors)
        
       # print "Letter: %s Lowest: %s" % (next_letter, lowest)
        
        #check to see if this is a sink
        if lowest >= map[y][x]:
            map_name[y][x] = next_letter
            return next_letter
        
        map_name[y][x] = '?'
        
        #check to see if there's only 1 level lower
        if neighbors.count(lowest) == 1:
            #find out where
            if neighbors.index(lowest) == 0:
                map_name[y][x] = travel(map,x,y-1,map_name,next_letter,h,w,x,y)
            elif neighbors.index(lowest) == 1:
                map_name[y][x] = travel(map,x-1,y,map_name,next_letter,h,w,x,y)
            elif neighbors.index(lowest) == 2:
                map_name[y][x] = travel(map,x+1,y,map_name,next_letter,h,w,x,y)
            elif neighbors.index(lowest) == 3:
                map_name[y][x] = travel(map,x,y+1,map_name,next_letter,h,w,x,y)
            else:
                map_name[y][x] = next_letter
            return map_name[y][x]
        
        #check for lowest ties
        else:
            #checking for ties
            if neighbors[0] == lowest and map_name[y-1][x] != '?':
                map_name[y][x] = travel(map,x,y-1,map_name,next_letter,h,w,x,y)
            elif neighbors[1] == lowest and map_name[y][x-1] != '?':
                map_name[y][x] = travel(map,x-1,y,map_name,next_letter,h,w,x,y)
            elif neighbors[2] == lowest and map_name[y][x+1] != '?':
                map_name[y][x] = travel(map,x+1,y,map_name,next_letter,h,w,x,y)
            elif neighbors[3] == lowest and map_name[y+1][x] != '?':
                map_name[y][x] = travel(map,x,y+1,map_name,next_letter,h,w,x,y)
            else:
                map_name[y][x] = next_letter
            return map_name[y][x]
        
    

def printMatrix(m):
    
    for i in range(0,len(m)):
        line = ""
        for j in range(0,len(m[i])):
            line = line + m[i][j] +" "
        print line
    

f = open("Watersheds/sample.in",'r')

try:
    
    num_of_maps = int(f.next().rstrip("\n"))
    
    for t in range(0,num_of_maps):
        
        hw = f.next().rstrip("\n").rsplit(" ")
        h = int(hw[0])
        w = int(hw[1])
        
        map = []
        map_name = []
        for i in range(0,h):
            map_line = []
            map_name_line = []
            for v in (f.next().rstrip("\n")).rsplit(" "):
                map_line.append(int(v))
                map_name_line.append(".")
            map.append(map_line)
            map_name.append(map_name_line)
        
        #print map_name
        
        letter = ord('a')
        
        for i in range(0,h):
            for j in range(0,w):
                letter_n = travel(map,j,i,map_name,chr(letter),h,w,-1,-1)
                #print letter_n
                if letter == ord(letter_n):
                    letter = letter+1
        
        print "Case #%s:" % (t+1)
        
        printMatrix(map_name)
        
        
        
                
    
        
except Exception, e:
    #pass
    print e
finally:
    f.close()