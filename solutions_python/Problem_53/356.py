import sys
def fullON( n ):
    if n == 1:
        return 1
    else:
        return fullON( n - 1 ) * 2 + 1

def doit(n, k):
    ans = fullON(n)
    if k < ans: return 0
    else:
        if (k - ans) % (ans + 1) == 0:
            return 1
        else:
            return 0

def main():
    for i, x in enumerate(sys.stdin):
        if i == 0: continue
        l = map( int, x.strip().split(' ') )
        print "Case #%d:" % (i,),
        if doit( l[0], l[1] ) == 1:
            print "ON"
        else:
            print "OFF"




if __name__ == '__main__':
    main()
