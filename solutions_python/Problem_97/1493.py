import sys

def solve(n, m):
    cnt = 0
    for i in range(n,m):
        for j in range(i+1,m+1):
            if len(str(i))==len(str(j)) and str(j) in str(i)*2:
                cnt += 1
    return cnt
 
if __name__ == '__main__':
    fileName = sys.argv[1]
    with open(fileName + '.in') as data:
        T = int(data.readline().strip())
        for i in range(T):
            s = data.readline().strip()
            n,m = [int(x) for x in s.split()]
            print "Case #%s: %s" % (i+1, solve(n,m))
