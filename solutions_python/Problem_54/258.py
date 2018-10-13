#!/usr/bin/python
import sys

def read_int():
    line = sys.stdin.readline().strip()
    return int(line)
def read_ints():
    line = sys.stdin.readline().strip()
    a = line.split(' ')
    return [int(e) for e in a]

def gcd(a,b):
    if b==0:
	return a
    return gcd(b, a%b)
def abs(a):
    if a<0:
	return -a
    return a
def problem(id):
    a = read_ints()
    n = a[0]
    g = 0
    for i in range(1,n):
	v = abs(a[1]-a[1+i])
	g = gcd(g, v)
#    print g
    ans = (g-a[1]%g)%g
    print "Case #%d: %d" %(id+1,ans)
def main():
    n = read_int()
    for i in range(n):
	problem(i)


if __name__ == '__main__':
    main()
