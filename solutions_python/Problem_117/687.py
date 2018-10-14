import re, itertools, math

input = open('C:\\Users\\Adam\\Downloads\\B-small-attempt0.in', 'r')
#input = open('C:\\Python27\\CodeJam\\Qualification 2013\\inputs.txt', 'r')
output = open('C:\\Python27\\CodeJam\\Qualification 2013\\outputs.out', 'w')

cases = int(input.readline())
case = 1

while case <= cases:
    rowMax = []
    columnMax = []
    lawn = []
    x = input.readline().split(' ')
    N = int(x[0])
    M = int(x[1])
    c = 1
    while c <= N:
        x = input.readline().split(' ')
        x[M-1] = x[M-1].replace('\n','')
        rowMax.append(max(x))
        lawn.append(x)
        if c == 1:
            for height in x:
                columnMax.append(height)
        else:
            for i in range(M):
                if x[i] > columnMax[i]:
                    columnMax[i] = x[i]
        c = c + 1
    result = ""
    
    for i in range(N):
        for j in range(M):
            spot = lawn[i][j]
            if spot < rowMax[i]:
                if spot < columnMax[j]:
                    result = "NO"
                    break
        if result:
            break
    if not result:
        result = "YES"
    result = "Case #" + str(case) + ": " + result
    if case != cases:
        result = result + "\n"
    output.write(result)
    case += 1
output.close()
input.close()
            
