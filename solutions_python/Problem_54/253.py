import sys;
import string;
import math;

#sys.stdin  = open('test.in', 'r')
#sys.stdout = open('test.out', 'w')
#sys.stdin = open('B-small-attempt0.in', 'r')
#sys.stdout = open('B-small-attempt0.out', 'w')
sys.stdin = open('B-large.in', 'r')
sys.stdout = open('B-large.out', 'w')
tests = int(sys.stdin.readline());

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for test in range(0, tests):
    list = sys.stdin.readline().split()
    n = int(list[0])
    num = int(list[1])
    g = abs(int(list[1]) - int(list[2]))
    for i in range(2, n):
        g = gcd(g, abs(num - int(list[i + 1])))
    if num % g == 0:
        out = 0
    else:
        out = g - num % g
    print("Case #"+str(test+1)+": "+str(out));
