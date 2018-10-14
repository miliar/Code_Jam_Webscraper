'''
Created on May 21, 2010

@author: hasmeet
'''

r = open('C:/users/hasmeet/desktop/A-large.in', 'r')

w = open('output.txt', 'w')

answer = ''

numCases = int(r.readline())

for i in range(numCases):
    print i
    line = r.readline().split(' ')
    N = int(line[0])
    K = int(line[1])
    rot = []
    for a in range(N): 
        line = r.readline()
        rot.append([])
        for b in range(N):
            if line[b] != '.': rot[a].append(line[b])
        while len(rot[a]) < N: rot[a] = ['.'] + rot[a]
    
    answer = 'Case #' + str(i+1) + ': '
    red = 0
    blue = 0
    for a in range(N):
        if red and blue: break
        for b in range(N):
            if red and blue: break
            if rot[a][b] == '.': continue
            if a + K <= N:
                for j in range(K):
                    if rot[a+j][b] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
            if a - K >= -1:
                for j in range(K):
                    if rot[a-j][b] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
            if b + K <= N:
                for j in range(K):
                    if rot[a][b+j] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
            if b - K >= -1:
                for j in range(K):
                    if rot[a][b-j] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
            if a + K <= N and b + K <= N:
                for j in range(K):
                    if rot[a+j][b+j] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
            if a + K <= N and b - K >= -1:
                for j in range(K):
                    if rot[a+j][b-j] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
            if a - K >= -1 and b + K <= N:
                for j in range(K):
                    if rot[a-j][b+j] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
            if a - K >= -1 and b - K >= -1:
                for j in range(K):
                    if rot[a-j][b-j] != rot[a][b]: break
                    elif j==K-1: 
                        if rot[a][b] == 'B': blue = 1
                        else: red = 1
    if red and blue: answer += 'Both\n'
    elif red: answer += 'Red\n'
    elif blue: answer += 'Blue\n'
    else: answer += 'Neither\n'
    w.write(answer)
    
    
r.close()
w.close()
print 'done'