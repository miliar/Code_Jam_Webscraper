#!/usr/bin/python

char = 'a'

def doPath(matrix, h, w, height, width):

    global char

    if matrix[h][w][0] != None:
        return matrix[h][w][0]

    points = [(10000, (h - 1), w),
              (10000, h, (w - 1)),
              (10000, h, (w + 1)),
              (10000, (h + 1), w)]

    maxim = None

    if h - 1 >= 0:
        points[0] = (matrix[h - 1][w][1], (h - 1), w)
    
    if w - 1 >= 0:
        points[1] = (matrix[h][w - 1][1], h, (w - 1))
    
    if w + 1 < width:
        points[2] = (matrix[h][w + 1][1], h, (w + 1))
    
    if h + 1 < height:
        points[3] = (matrix[h + 1][w][1], (h + 1), w)


    center = matrix[h][w][1]
    for p in points:
        if p[0] < center:
            if maxim == None:
                maxim = p
            else:
                if p[0] < maxim[0]:
                    maxim = p

    if maxim == None:
        tmp = char
        char = chr(ord(char) + 1)
        matrix[h][w] = [tmp, center]
        return tmp

    tmp = doPath(matrix, maxim[1], maxim[2], height, width)
    matrix[maxim[1]][maxim[2]] = [tmp, maxim[0]]
    return tmp
            
    
    
    

def processMatrix(matrix, height, width):

    for h in range(0, height):
        for w in range(0, width):
            c = doPath(matrix, h, w, height, width)
            matrix[h][w][0] = c


    newMatrix = []

    for h in range(0, height):
        row = []
        for w in range(0, width):
            c = matrix[h][w][0]
            row.append(c)
        newMatrix.append(row)

    return newMatrix


if __name__ == '__main__':
    
    maps = raw_input()
    maps = int(maps)

    global char

    for index in range(1, maps + 1):

        #height and width
        height, width = raw_input().split(' ')
        height = int(height)
        width  = int(width)

        matrix = []

        char = 'a'

        for h in range(0, height):
            row = raw_input().split(' ')
            newRow = []
            for num in row:
                tmp = (None, int(num))
                newRow.append(list(tmp))
            matrix.append(newRow)
        
        resultMatrix = processMatrix(matrix, height, width)

        print "Case #%d:"%(index,)

        for line in resultMatrix:
            print " ".join(line)
        
            
        
