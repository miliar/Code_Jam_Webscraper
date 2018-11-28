import sys, StringIO

DEBUG = 0

def solution(n, k):

    #if k>n*2/3:
    #    return 0, 0
    #if k>n/3:
    #    return 1, 0
    d = [n]
    if DEBUG: print ("\t%s , k:%d" % (d, k))
    while k:
        s = d.pop()
        if s>2:
          r1 = (s-(s+1)%2)/2
          r2 = s/2
          d.extend([r1, r2])
        if s==2:
          r1 = 0
          r2 = 1
          d.append(r2)
        if s==1:
          r1 = 0
          r2 = 0
        k-=1
        d.sort()
        if DEBUG: print ("\t%s , k:%d" % (d, k))
    return r2, r1


if __name__ == '__main__':
    if len(sys.argv)>1:
        input = file(sys.argv[1])
    else:
        input = StringIO.StringIO("""5
4 2
10 5
6 2
1000 1000
1000 1""")
    cases = int(input.readline())
    for case in range(cases):
        n, k = input.readline().split()
        r1 , r2 = solution(int(n), int(k))
        print("Case #%d: %d %d" % (case+1, r1, r2))
