import sys

def main():
    T = int(sys.stdin.readline())

    for tp in xrange(T):
        A, B = map(int, sys.stdin.readline().split())
        sol = set()

        for i in range(A, B):
            y = str(i)

            for j in range(i+1, B+1):
                x = str(j)
                
                for k in xrange(len(x)-1):
                    x = x[-1] + x[:-1]
                    if y == x:
                        sol.add((y, str(j)))
        
        print "Case #%d: %d" % (tp+1, len(sol))
                
if __name__ == '__main__':
    main()
