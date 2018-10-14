inputF = open('A-large.in', 'r')
output = open('A-large.out', 'w')

numCases = int(inputF.readline())

def getBadCoords(arr):
    # Return (badCoords, impossibleCoords)
    badCoords = []
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                bad = True
                k = i-1
                while k >= 0:
                    if arr[k][j] != 0:
                        bad = False
                        break
                    k -= 1
                if bad == True:
                    badCoords += [(i,j)]
            elif arr[i][j] == 2:
                bad = True
                k = j+1
                while k <= len(arr[i])-1:
                    if arr[i][k] != 0:
                        bad = False
                        break
                    k += 1
                if bad == True:
                    badCoords += [(i,j)]
            elif arr[i][j] == 3:
                bad = True
                k = i+1
                while k <= len(arr)-1:
                    if arr[k][j] != 0:
                        bad = False
                        break
                    k += 1
                if bad == True:
                    badCoords += [(i,j)]
            elif arr[i][j] == 4:
                bad = True
                k = j-1
                while k >= 0:
                    if arr[i][k] != 0:
                        bad = False
                        break
                    k -= 1
                if bad == True:
                    badCoords += [(i,j)]


    for badCoord in badCoords:
        i = badCoord[0]
        j = badCoord[1]
        count = 0
        for k in range(len(arr)):
            if arr[k][j] != 0:
                count += 1
        for k in range(len(arr[0])):
            if arr[i][k] != 0:
                count += 1
        if count <= 2:
            return badCoords, [(i,j)]

    return badCoords, []
            
    

for i in range(numCases):
    dim = inputF.readline().split()
    r = int(dim[0])
    c = int(dim[1])

    arr = [[0]*c for k in range(r)]
    for j in range(r):
        line = inputF.readline()
        for k in range(len(line)):
            char = line[k]
            if char == '^':
                arr[j][k] = 1
            elif char == '>':
                arr[j][k] = 2
            elif char == 'v':
                arr[j][k] = 3
            elif char == '<':
                arr[j][k] = 4

    badCoords, impossibleCoords = getBadCoords(arr)

    output.write('Case #' + str(i+1) + ': ')    
    if len(impossibleCoords) > 0:
        output.write('IMPOSSIBLE\n')
    else:
        output.write(str(len(badCoords)) + '\n')




inputF.close()
output.close()
