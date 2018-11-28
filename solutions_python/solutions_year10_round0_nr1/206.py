from pprint import pprint
import sys

def allBitsOn(num, digits):
    for i in range(digits):
        if 0 == num % 2:
            return False
        num = num >> 1
    return True

def solveCase(c, f, o):
    N, K = f.readline().strip().split()
    N = int(N)
    K = int(K)
    result = allBitsOn(K, N)
    result = 'ON' if result else 'OFF'
    o.write("Case #%d: %s\n" % (c, result))

if __name__ == '__main__':
    input = sys.argv[1]
    f = open(input, 'rb')
    o = open(input.split(".")[0] + "-out" + ".txt", 'wt')
    cases = int(f.readline())
    for c in xrange(cases):
        solveCase(c+1, f, o)
    f.close()
    o.close()
