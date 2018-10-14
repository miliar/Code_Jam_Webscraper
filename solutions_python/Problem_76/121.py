from sys import argv
from itertools import izip, imap, count, combinations, permutations

def solvecase( line ):
    line = line.split()
    line = map( int, line )
    if reduce( lambda x,y: x^y, line ):
        return "NO"
    else:
        return sum(line)-min(line)

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        l = inf.readline().strip()
        l = inf.readline().strip()
        ans = solvecase( l )
        print "Case #{n}: {ans}".format(n=case, ans=ans)

main()

