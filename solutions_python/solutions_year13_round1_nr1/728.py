# Google Code-Jam Template
# By- Sannidhya Shukla

import sys

def precomp():
    #whatever
    return

def main():
    T = int(sys.stdin.readline())
    for case in xrange(1, T+1):
        case_data = read_case()
        ANS = solve(case_data)
        sys.stdout.write("Case #%d: %s\n" % (case, ANS))

def read_case():
    # Read the case from the sys.stdin
    return map(int, sys.stdin.readline().split())

def solve(data):
    #solve it baby!
    r, t = data
    out = 0
    vol = 0
    for rdash in xrange(r+1, t, 2):
        vol += (2*rdash) - 1
        if vol > t:
            break
        out +=1
    return out

precomp()
if __name__ == '__main__':    
    if len(sys.argv) > 1:
        sys.stdin = file(sys.argv[1], 'rU')
    sys.stdout = file('out.out', 'w')
    main()
