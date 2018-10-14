import sys
import math

cin = sys.stdin.readline

def solve(lin):
    count = 0
    x = math.sqrt(int(lin[0]))
    small_int = int(math.floor(x))
    large_int = int(math.floor(math.sqrt(int(lin[1]))))
    if float(small_int) == x:
        for i in xrange(small_int, large_int+1):
            if i == int(str(i)[::-1]) and i*i == int(str(i*i)[::-1]):
                count = count + 1
    else:
        for i in xrange(small_int+1, large_int+1):
            if i == int(str(i)[::-1]) and i*i == int(str(i*i)[::-1]):
                count = count + 1
    return count



if __name__ == '__main__':
    T = int(cin())
    f = open('d.txt', 'w')
    for cnum in xrange(T):
        lin = cin().strip().split()
        f.write("Case #{0}: {1}\n".format(cnum+1, solve(lin)))
    f.close()
