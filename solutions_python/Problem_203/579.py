#Name: Robin Park
#Username: robinp
#Google Code Jam Round 1A 2017

import random
import re

def solve(cake, R, C, t):
    regex = r'\?{%d}' % C;
    
    for r in range(R):
        for c in range(C):
            if cake[r][c] != '?':
                for k in range(c - 1, -1, -1):
                    if cake[r][k] == '?':
                        cake[r][k] = cake[r][c]
                    else:
                        break
        for c in range(C-1, -1, -1):
            if cake[r][c] != '?':
                break
        d = c;
        for k in range(d+1, C):
            cake[r][k] = cake[r][d]
            # print("test")       
            
    for r in range(R):
        if len(re.findall(regex, ''.join(cake[r]))) == 0:
            for c in range(r-1, -1, -1):
                if len(re.findall(regex, ''.join(cake[c]), 0)) != 0:
                    cake[c] = cake[r]
                else:
                    break
                
    for r in range(R-1, -1, -1):
        if len(re.findall(regex, ''.join(cake[r]), 0)) == 0:
            break
        
    fill = cake[r]
    for c in range(r, R):
        cake[c] = fill
        
    w.write('Case #' + str(t+1) + ':\n')
    for r in range(R):
        w.write(''.join(cake[r]))
        w.write('\n')


if __name__ == '__main__':
    with open('cake.in', 'r') as file, open('cake.out', 'w') as w:  
        T = int(file.readline().strip())
        for t in range(T):
            cake = []   # R x C
            R, C = map(int, file.readline().strip().split())

            for r in range(R):
                cake.append(list(file.readline().strip()))

            solve(cake, R, C, t)



print("done")
