import numpy as np
from timeit import default_timer as timer


def solve(happy, k):
    n = len(happy)
    flips = 0
    i = 0
    while True:
        while i<n and happy[i]:
            i += 1
        if i==n:
            return str(flips)
        elif k > n-i:
            return 'IMPOSSIBLE'
        else:
            flips += 1
            j = i + 1
            lim = i + k
            while j<lim and not happy[j]:
                j += 1
            i = j
            for j in range(j, lim):
                happy[j] = not happy[j]
            

    
if __name__ == '__main__' :
    
    fileName = 'A-large'
    with open(fileName + '.in', 'r')  as f,     \
         open(fileName + '.out', 'w') as fout:
        start = timer()
        
        n_cases = int(f.readline()) 
        for t in range(1, n_cases+1) :
            # Read a case 
            s, k = f.readline().split()
            happy = [True if x=='+' else False for x in s]
            k = int(k)
            
            # Solve     
            solution = solve(happy, k)                              
            output = 'Case #%d: %s\n' % (t, solution)   
            
            # Print
            fout.write(output)
            print(output),

        elapsed = timer() - start
        print('Elapsed time: %g' % elapsed)
            
