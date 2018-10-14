#!/usr/bin/env python

#read input put in 4x4 matrix
lines = [line.strip() for line in open('input.in')]
n = int(lines[0])

stopped = dotFound = won = False #stopped: didn't run to the end of the line
sign = ""
of = open("output.out",'w')

for i in range(n):
    #waagerecht
    for j in range(4):
        for k in range(4):
            actual = lines[1+i*5 + j][k]
            if (actual == '.'):
                dotFound = True
                stopped = True
                break
            elif (actual == 'T'):
                continue
            else:   #sign == X or O
                if (sign == ""):
                    sign = actual
                    continue
                elif (sign != actual):
                    stopped = True
                    break
                else:
                    continue
        
        if ((not stopped) and (sign != "")):
            of.write("Case #"+str(i+1)+": "+sign+" won\n")
            won = True
        stopped = False
        sign = ""
    #senkrecht
    if not won:
        for j in range(4):
            for k in range(4):
                actual = lines[1+i*5 + k][j]
                if (actual == '.'):
                    dotFound = True
                    stopped = True
                    break
                elif (actual == 'T'):
                    continue
                else:   #sign == X or O
                    if (sign == ""):
                        sign = actual
                        continue
                    elif (sign != actual):
                        stopped = True
                        break
                    else:
                        continue
           
            if ((not stopped) and (sign != "")):
                of.write("Case #"+str(i+1)+": "+sign+" won\n")
                won = True
            stopped = False
            sign = ""
    
    #diagonal links nach rechts
    if not won:
        for k in range(4):
            actual = lines[1+i*5 + k][k]
            if (actual == '.'):
                dotFound = True
                stopped = True
                break
            elif (actual == 'T'):
                continue
            else:   #sign == X or O
                if (sign == ""):
                    sign = actual
                    continue
                elif (sign != actual):
                    stopped = True
                    break
                else:
                    continue
        
        if ((not stopped) and (sign != "")):
            of.write("Case #"+str(i+1)+": "+sign+" won\n")
            won = True
        stopped = False
        sign = ""
    #diagonal rechts nach links
    if not won:
        for k in range(4):
            actual = lines[1+i*5+k][3-k]
            if (actual == '.'):
                dotFound = True
                stopped = True
                break
            elif (actual == 'T'):
                continue
            else:   #sign == X or O
                if (sign == ""):
                    sign = actual
                    continue
                elif (sign != actual):
                    stopped = True
                    break
                else:
                    continue
        
        if ((not stopped) and (sign != "")):
            of.write("Case #"+str(i+1)+": "+sign+" won\n")
            won = True
        stopped = False
        sign = ""
    
    
    if (not won):
        if (not dotFound):
            of.write("Case #"+str(i+1)+": Draw\n")
        elif (dotFound):
            of.write("Case #"+str(i+1)+": Game has not completed\n")
    stopped = dotFound = won = False


of.close()