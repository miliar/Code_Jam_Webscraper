import sys

def solve(line):
    Smax, levels = line.split()[:2]
    Smax = int(Smax)
    total = 0
    need = 0
    #print levels
    for n, i in enumerate(levels):
        i = int(i)
        total += i
        if total <= n:
            need += 1
            total += 1
    return need

def main():
    f = open(sys.argv[1])
    T = int( f.next() )
    for i in range(T):
        print "Case #{0}: {1}".format( i+1, solve(f.next()) )

main()


