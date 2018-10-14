import sys
import re

def insertInto(letters,res_map,r,c,m_r,m_c):
    isInside = False
    minInside = 99999
    myL = []
##    print "Before",letters
    for l in letters:
        if res_map[m_r][m_c] in l:
            isInside = True
            myL = l
            minInside = min(l)
##            print "Inside! "+str(minInside)
            break
    
    for l in letters:
        if res_map[r][c] in l:
            myMin = min(l)
            if isInside:
                if (myMin > minInside):
                    myL.extend(l)
                    del letters[letters.index(l)]
                else:
                    l.extend(myL)
                    del letters[letters.index(myL)]
            else:
                l.append(res_map[m_r][m_c])
##            print"After: ",letters
            return
        
    if isInside:
        myL.append(res_map[r][c])
    else:
        letters.append([res_map[r][c],res_map[m_r][m_c]])
##    print letters

filename = "C:\\Amir\\programming\\CodeJam\\first\\2\\B-large.in"
f = open(filename)
lines = f.readlines()
f.close()
lines.reverse()
firstLine = lines.pop()
#print firstLine
maps = int(firstLine)
out = open("C:\\Amir\\programming\\CodeJam\\first\\2\\out.txt",'w')
for z in range(maps):
    res_map = []
    [rows,cols] = lines.pop().split(" ")
    rows = int(rows)
    cols = int(cols)
    cur_map = [[20000]*(cols+2)]
    for j in range(rows):
        cur_map.append([20000]+map(int,lines.pop().split(" "))+[20000])

    cur_map.append([20000]*(cols+2))
##    print cur_map
    cur = 1
    for p in range(rows):
        res_map.append(range(cur,cur+cols))
        cur += cols

    letters = [[1]]

    # finished building map
    
    # calculating result map
    for r in range(1,rows+1):
        for c in range(1,cols+1):
##            print r,"-",c
            min_near = min(cur_map[r-1][c],cur_map[r+1][c],cur_map[r][c+1],cur_map[r][c-1])
##            print min_near
            if (cur_map[r][c] > min_near):
                if (min_near == cur_map[r-1][c]):
                    insertInto(letters,res_map,r-1,c-1,r-2,c-1)
                elif (min_near == cur_map[r][c-1]):
                    insertInto(letters,res_map,r-1,c-1,r-1,c-2)
                elif (min_near == cur_map[r][c+1]):
                    insertInto(letters,res_map,r-1,c-1,r-1,c)
                elif (min_near == cur_map[r+1][c]):
                    insertInto(letters,res_map,r-1,c-1,r,c-1)
            else:
                # can do it with continue
##                print "not found"
                found = False
                for l in letters:
                    if res_map[r-1][c-1] in l:
                        found = True
                        break
                if not found:
                   letters.append([res_map[r-1][c-1]])

##    print "Result:"
##    print letters

    out.write("Case #"+str(z+1)+":\n")
    for i in range(1,cur):
        for l in letters:
            if i in l:
                ind = letters.index(l)
##                print ind
                out.write(chr(97+ind))
                if (i%cols == 0):
                    out.write("\n")
                else:
                    out.write(" ")
out.close()
