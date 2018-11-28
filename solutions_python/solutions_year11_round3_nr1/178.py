#!/usr/bin/python
import re

#Read input
f       = open('inp.txt', 'r')
lines   = f.readlines()
f.close()

#Output
f       = open('out.txt', 'w')
total   = lines.pop(0)
case_no = 0

def findfraction (x, gcdtoo=False, maxno=100):
    #remember x is exact
    win  = x
    deno = 100    

    if x == 0:
        return [0,maxno]
    
    if gcdtoo:
        common = gcd(win,deno)
        return [win/common,deno/common]
    else:
        return [win,deno]
    

def gcd(num1, num2):
    result = 1
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

def devable(a, b):
    return ((a%b == 0) or (b%a) == 0)
 

while(True):
    #Leave this out {
    if len(lines) == 0:
        break
    result = ""
    #}

    listn = lines.pop(0)    #x * x
    listn = listn.split(" ")
    height = int(listn[0])
    width  = int(listn[1])
    count = 0
    tiles = []
    noblue = 0

    error = False

    while (count < height):
        tile = list((lines.pop(0)).rstrip('\n'))
        bluetile = 0
        for each in tile:
            if each == '#':
                bluetile += 1 


        if (bluetile % 2) == 1:   # odd
            error = True

        noblue += bluetile
        tiles.append(tile)
        count += 1

    #cover basic case

    if (not error) and (noblue % 4 == 0):
        #not go to each line
        i=0
        error = False
        for row in tiles:
            j = 0
            error = False
            for col in row:
                if col == "#":
                    if (tiles[i+1][j] == "#" and tiles[i][j+1] == "#" and tiles[i+1][j+1] == "#"):
                        #replace it
                        tiles[i][j] = '/'
                        tiles[i][j+1] = "\\"
                        tiles[i+1][j] = "\\"
                        tiles[i+1][j+1] = '/'
                    else:
                        error = True
                        break                    
                j += 1

            if error:
                break

            i+=1 

        if error:
            result = "\nImpossible"    
        else:
            result = ""
            for each in tiles:
                result += "\n"+''.join(each)

    else:
        result = "\nImpossible"    

    case_no   += 1
    output = "Case #"+str(case_no)+": "+str(result)
    print output
    output += "\n"
    #break
    f.write(output)
f.close()
