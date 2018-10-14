import numpy as np
from timeit import default_timer as timer

def solve(d):
    dlen = len(d)
    if dlen==1:
        return d[0]
    s = 0 # first occurrence of the last digit
    for i in range(1, dlen):
        if d[i-1] > d[i]:
            break
        if d[i] != d[s]:
            s = i
    else:
        return d
    
    if d[s] == '1':
        return '9' * (dlen - 1)
    else:
        return d[:s] + chr(ord(d[s]) - 1) + '9' * (dlen - s - 1)
    
    
if __name__ == '__main__' :
    
    fileName = 'B-large'
    with open(fileName + '.in', 'r')  as f,     \
         open(fileName + '.out', 'w') as fout:
        start = timer()
        
        n_cases = int(f.readline()) 
        for t in range(1, n_cases+1) :
            # Read a case 
            digits = f.readline().strip()
            
            # Solve     
            solution = solve(digits)                                
            output = 'Case #%d: %s\n' % (t, solution)   
            
            # Print
            fout.write(output)
            print(output),

        elapsed = timer() - start
        print('Elapsed time: %g' % elapsed)
            
