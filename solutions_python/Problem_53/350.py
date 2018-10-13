import sys

# N = 3
# 0: 000
# 1: 001
# 2: 010
# 3: 011
# 4: 100
# 5: 101
# 6: 110
# 7: 111 *
# 8: 000

def run_case(i):
    N,K = map(int,sys.stdin.readline().split())
    if (K+1)%(1<<N)==0:
        r="ON"
    else:
        r="OFF"
    print "Case #%d: %s" % (i,r)

def main():
    T = int(sys.stdin.readline())
    for i in xrange(1,T+1):
        run_case(i)

if __name__ == '__main__':
    main()
