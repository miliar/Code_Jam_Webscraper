#!/usr/bin/env python
import sys

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

lines = fin.readlines()
lines.append('')
index = int(lines.pop(0).rstrip())

for n in range(index):
    dimension = lines.pop(0).split()
    height = int(dimension[0])
    width = int(dimension[1])
    
    #read data
    data = []
    shortest = 100
    for i in range(height):
        data.append(lines.pop(0).rstrip().split())
        if (shortest > int(min(data[i]))):
            shortest = int(min(data[i]))
    
	#look for possible 
    possible = True
    if (width > 1 and height > 1):
        for i in range(height):
            for j in range(width):
                if (shortest == int(data[i][j])):
                    #look for exit
                    maxX = shortest
                    maxY = shortest
                    for a in range(height):
                        if (int(data[a][j]) > maxY):
                            maxY = int(data[a][j])
                    for b in range(width):
                        if (int(data[i][b]) > maxX):
                            maxX = int(data[i][b])
                    # print 'maxX : ' + maxX
                    # print 'maxY : ' + maxY
                    if (maxX > shortest and maxY > shortest):
                        possible = False
                if (possible == False):
                    break
            if (possible == False):
                break
	
	#print result
    if (possible == True):
        fout.write('Case #' + str(n+1) + ': YES')
    else:
        fout.write('Case #' + str(n+1) + ': NO')
	
    fout.write('\n')
    # lines.pop(0) #skip empty line

fout.close()