
import math

PI = 3.14

def black_paint(r):
    return (r**2 - (r-1)**2)


input_r, input_t = 3, 40


def do(r, t):
    s = 0
    n = 0
    r += 1

    while s <= t:
        s += (r) **2 - (r-1) ** 2
        r+=2
        n+=1

    return n-1


"""
print do(1,9)
print do(1,10)
print do(3,40)
print do(1,1000000000000000000)
print do(10000000000000000,1000000000000000000)
"""

if __name__ == '__main__':
    import sys
    read = sys.stdin.readlines()
    read = map(lambda x: x.strip(), read)
    read = read[1:]

    for n, case in enumerate(read):
        read_r, read_t = case.split(' ')
        read_r = int(read_r)
        read_t = int(read_t)
        result = do(read_r, read_t)
        
        print "Case #{0}: {1}".format(n+1, result)


