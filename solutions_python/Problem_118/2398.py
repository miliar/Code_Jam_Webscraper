from collections import namedtuple
import math

Case = namedtuple('Case', ['start', 'end'])

def generatePalindromicSquares(start, end):
    sqrt_start = int(math.sqrt(start))
    sqrt_end = int(math.sqrt(end))
    if sqrt_start**2 < start : sqrt_start += 1
    if sqrt_end**2 > end : sqrt_end -= 1

    pairs = [(i, i**2) for i in range(sqrt_start, sqrt_end+1)]
    palindromic_squares = []
    for p, s in pairs:        
        _p = str(p)
        _s = str(s)
        if list(_p) == list(reversed(_p)) and list(_s) == list(reversed(_s)):
            palindromic_squares.append(s)
    
    return palindromic_squares

def evaluate(case):
    palindromic_squares = generatePalindromicSquares(case.start, case.end)
    return len(palindromic_squares)    

if __name__ == '__main__':
    import sys

    if sys.argv[1:]:
        filename = sys.argv[1]
    else:
        exit('Usage: %s <input_file>' % sys.argv[0])
    
    cases = []
    with open(filename) as f:
        data = f.readlines()
        num_cases = int(data[0])        
        for line in data[1:]:
            c = [int(i) for i in line.strip().split()]            
            cases.append(Case._make(c))
    
    # for i,c in enumerate(cases):
    #     print ('Case #%s: %s' % (i+1, evaluate(c)))

    fout = filename.replace('.in', '.out')
    with open(fout, 'wb') as f:
        for i,c in enumerate(cases):
            f.write('Case #%s: %s\n' % (i+1, evaluate(c)))
