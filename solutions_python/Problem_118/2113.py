import os
from numpy import array, arange

def solve(lawn):
    
    row, col = lawn.shape
    for i in range(1, row - 1): 
        left, right = lawn[i, [0, -1]]
        for j in range(1, col - 1):
            val = lawn[i, j]
            top, bottom = lawn[[0, -1], j]
            
            if val < left and val < right:
                return 'NO'
            if val < bottom and val < top:
                return 'NO'
    return 'YES'
    


def main(filename):
    
    with open(filename) as inp: 
        n_cases = inp.readline().strip()
        n_cases = int(n_cases)
        
        with open(os.path.splitext(filename)[0] + '.out', 'w') as out:
        
            for i in range(n_cases):
                a, b = inp.readline().split()
                rng = arange(int(a), int(b) + 1)
                sqrt = (rng ** 0.5).astype(int)
                which = (rng == sqrt ** 2).nonzero()[0]
                count = 0
                for w in which: 
                    s = str(sqrt[w])
                    t = str(rng[w])
                    if s == s[::-1] and t == t[::-1]:
                        count += 1
                line = 'Case #{}: {}'.format(i+1, count)
                out.write(line + '\n')
                print line


if __name__ == '__main__':
    
    main('C-small-attempt0.in')
