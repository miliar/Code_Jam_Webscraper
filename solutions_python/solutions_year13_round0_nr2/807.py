def solve(matrix):
    width = len(matrix)
    height = len(matrix[0])
    
    for x in range(0, width):
        for y in range(0, height):
            element = matrix[x][y]
            xwin=0
            ywin=0
            for j in range(0, height):
                if (matrix[x][j] <= element):
                    xwin+=1
            for j in range(0, width):
                if (matrix[j][y] <= element):
                    ywin+=1
        
            if (ywin!=width and xwin!=height):
                return "NO"

    return "YES"

tries = raw_input()

for i in range(0, int(tries)):
    words = raw_input().split()
    
    updown = []
    
    for x in range(0, int(words[0])):
        updown.append(map(int, raw_input().split()))
        

    print "Case #"+ str(i+1)+": "+str(solve(updown))