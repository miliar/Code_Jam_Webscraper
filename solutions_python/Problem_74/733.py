#! /usr/bin/env python3.0

def dist(pos, next):
    return abs(next-pos)

def go(pos, next, sec=1):
    # curr pos, next pos, seconds --> new pos
    if ((pos == next) or (next == 0)):
        return pos
    
    d = dist(pos, next)
    
    if (sec >= d):
        return next
    
    if (next-pos > 0):
        return pos+sec
    return pos-sec

def next(letter, moves):
    for m in moves:
        if (m[0] == letter):
            return m[1]
    return 0

fic = input()

f = open(fic, "r")
lines = [li.replace("\n", "") for li in f.readlines()][1:]
f.close()

f = open("output.txt", "w")

for i in range(len(lines)):
    
    line = lines[i].split(" ")[1:]
    moves = [[i, int(j)] for i,j in zip(line[::2], line[1::2])]
    
    pos_o = 1 # current position of Orange
    pos_b = 1 # current position of Blue
    
    total = 0 # time
    
    for j in range(len(moves)):
        
        m = moves[j]
        
        if (m[0] == "B"):
            
            next_o = next("O", moves[j+1:])
            next_b = m[1]
            
            if (pos_b == m[1]): # B dont move and push
                pos_o = go(pos_o, next_o) # O move 1
            
            else:
                total += dist(pos_b, m[1])
                
                pos_o = go(pos_o, next_o, dist(pos_b, m[1])+1) # O move ...+1
                pos_b = m[1] # B move and push
                
        elif (m[0] == "O"):
            
            next_o = m[1]
            next_b = next("B", moves[j+1:]) 
            
            if (pos_o == m[1]): # O dont move and push
                pos_b = go(pos_b, next_b) # b move 1
            
            else:
                total += dist(pos_o, m[1])
            
                pos_b = go(pos_b, next_b, dist(pos_o, m[1])+1) # B move ...+1
                pos_o = m[1] # O dont move and push
        
        total += 1 # push
        
    out = "Case #"+str(i+1)+": "+str(total)
    print(out)
    f.write(out+"\n")

f.close()