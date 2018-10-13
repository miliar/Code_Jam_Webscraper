# Author: BAIZHIJIE (baizhj@gmail.com)
def solve_problem_a(n, k):
    s = 0
    p = 1
    i = 1
    while i<=k:
        s = s^p
        j = 0
        while (2**j)&s:
            j = j+1
        p = (2**(j+1))-1
        i = i+1
    if (2**n&p)!=0:
        return 'ON'
    else:
        return 'OFF'
        

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        line = raw_input()
        n,k = line.split()
        r = solve_problem_a(int(n), int(k))
        print 'Case #%d: %s' % (i+1, r) 
