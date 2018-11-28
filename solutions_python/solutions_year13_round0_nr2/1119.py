from sys import stdin
from unittest import result
from math import fmod, sqrt

def main():
    n_cases = int(stdin.readline()) 

    for i_case in range(1, n_cases+1):
        a, b = [int(i) for i in stdin.readline().split(' ')]
        lawn = [ [ 0 for i in range(b) ] for j in range(a)]
        for j1 in range(a):
            seq = [int(i) for i in stdin.readline().split(' ')]
            for j2 in range(b):
                lawn[j1][j2] = int(seq[j2])
                
        hmax = max(max(l) for l in lawn)
        hmin = min(min(l) for l in lawn)
        
        corte = [ [ 'N' for i in range(b) ] for j in range(a)]

        
        for h in range(hmin, hmax+1):
            # orisontales
            for j1 in range(a):
                if max(lawn[j1]) <= h:
                    for j2 in range(b):
                        if lawn[j1][j2] == h:
                            corte[j1][j2] = 'S'
                            
            # verticales
            for j1 in range(b):
                ver = [lawn[i+a%a][j1] for i in range(a)]
                if max(ver) <= h:
                    for i in range(a):
                        if lawn[i+a%a][j1] == h:
                            corte[i+a%a][j1] = 'S'
                            
        result = True
        for ori in corte:
            for c in ori:
                if c == 'N':
                    result = False
                    break
            if not result:
                break
        
        if not result:
            print 'Case #'+str(i_case)+': '+ 'NO'
        else:
            print 'Case #'+str(i_case)+': '+ 'YES'
        

if __name__ == '__main__':
    main()