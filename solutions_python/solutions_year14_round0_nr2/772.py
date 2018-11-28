import math

def koszt(c,f,x,i):
    cost = 0
    for j in range(0, i):
        cost += c/(2+j*f)
    cost += x/(2+f*i)
    return cost

def local_min(c,f,x):
    return (f*x - 2*c)/(f*c) - 1

def solve():
    T = int(raw_input())
    for i in range(T):
        c, f, x = map(float, raw_input().split(' '))
        where = max(0, local_min(c, f, x))

        res = min(koszt(c, f, x, int(math.floor(where))), 
                koszt(c, f, x, int(math.ceil(where))))
        print "Case #%d: %.9f" % (i+1, res)

if __name__ == '__main__':
    solve()
