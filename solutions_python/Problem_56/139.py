'''
Created on 22/05/2010

Rotate

@author: Soloman
'''

def solve(N, K, C):
    for i in range(N):
        C[i] = moveRight(C[i])
        print(C[i])
        
    return check(K, C, len(C[0]), N)

def check(K, C, w, h):
    if C[h-1][w-1]!='.':
        Y = [y for y in range(h)]
        X = [x for x in range(w)]
        Y.reverse()
        X.reverse()
        
        found = []
        for y in Y:
            for x in X:
                c = C[y][x]
                if c!='.' and c not in found:
                    if _check(K, C, x, y):
                        found.append(c)
        
        if len(found)==2:
            return 'Both'
        elif len(found)==1:
            return _print(found[0])
        else:
            return 'Neither'  
    else:
        return 'Neither'

def _print(c):
    if c=='R':
        return 'Red'
    else:
        return 'Blue' 

def _check(K, C, x, y):
    W = len(C[0])
    t = C[y][x]    
    found = True
    for i in range(1, K): #check row
        _x = x-i
        if _x>=0:
            if t!=C[y][_x]:
                found=False
                break 
        else:
            found=False
            break
    if found:
        return True
    
    found = True
    for i in range(1, K): #check col
        _y = y-i
        if _y>=0:
            if t!=C[_y][x]:
                found=False
                break 
        else:
            found=False
            break
    if found:
        return True
    
    found = True
    for i in range(1, K): #check dia
        _y = y-i
        _x = x-i
        if _y>=0 and _x>=0:
            if t!=C[_y][_x]:
                found=False
                break 
        else:
            found=False
            break
    if found:
        return True
    
    found = True
    for i in range(1, K): #check dia 2
        _y = y-i
        _x = x+i
        if _y>=0 and _x<W:
            if t!=C[_y][_x]:
                found=False
                break 
        else:
            found=False
            break
    if found:
        return True
    
    return False
    
        
        

    

def moveRight(line):
    old = len(line)
    line = [l for l in line if l!='.']
    k = old-len(line)
    if k>0:
        return ''.join('.'*k)+''.join(line)
    else:
        return line

file_dir=''
input_file = file_dir + 'A-large.in'
output_file = file_dir + 'out.txt'

fin=open(input_file, 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    N, K = [int(x) for x in fin.readline().split()]
    C = []
    for i in range(N):
        C.append(fin.readline().strip())
        
    ans = 'Case #%d: %s\n'%(t, solve(N, K, C))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()