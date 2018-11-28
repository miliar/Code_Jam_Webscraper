import sys

x = 0;
n = sys.stdin.readline()
n = int(n)

#print("Case #",i,": ",w + 1," ", f + 1, sep='')
while (x < n):
    x = x + 1
    l = [
    sys.stdin.readline(),
    sys.stdin.readline(),
    sys.stdin.readline(),
    sys.stdin.readline()]
    
    sys.stdin.readline()
    
    u = 0
    d = 0
    
    for i in range(4):
        for j in range(4):
            q = w = e = r = 0
            qo = wo = eo = ro = 0
            if l[i][j] == '.':
                d = 1
            if u == 0:    
                if l[i][j] == 'X' or l[i][j] == 'T':
                    for k in range(3):
                        o = k + 1
                        if j + o <= 3: 
                            if l[i][j + o] == 'X' or l[i][j + o] == 'T':
                                q = q + 1
                        if i + o <= 3: 
                            if l[i + o][j] == 'X' or l[i + o][j] == 'T':
                                w = w + 1
                        if i + o <= 3 and j + o <= 3:
                            if l[i + o][j + o] == 'X' or l[i + o][j + o] == 'T':
                                e = e + 1
                        if i - o >= 0 and j + o <= 3:
                            if l[i - o][j + o] == 'X' or l[i - o][j + o] == 'T':
                                r = r + 1
                    
                    if q == 3 or w == 3 or e == 3 or r == 3:
                        print("Case #",x,": X won", sep='')
                        u = 1
                        
            if u == 0:
                q = w = e = 0
                if l[i][j] == 'O' or l[i][j] == 'T':
                    for k in range(3):
                        o = k + 1
                        if j + o <= 3: 
                            if l[i][j + o] == 'O' or l[i][j + o] == 'T':
                                qo = qo + 1
                        if i + o <= 3: 
                            if l[i + o][j] == 'O' or l[i + o][j] == 'T':
                                wo = wo + 1
                        if i + o <= 3 and j + o <= 3:
                            if l[i + o][j + o] == 'O' or l[i + o][j + o] == 'T':
                                eo = eo + 1
                        if i - o >= 0 and j + o <= 3:
                            if l[i - o][j + o] == 'O' or l[i - o][j + o] == 'T':
                                ro = ro + 1
                                
                    
                    if qo == 3 or wo == 3 or eo == 3 or ro == 3:
                        print("Case #",x,": O won", sep='')
                        u = 1
            
    if u == 0:
        if d == 0:
            print("Case #",x,": Draw", sep='')
        else:
             print("Case #",x,": Game has not completed", sep='')
        
    
    