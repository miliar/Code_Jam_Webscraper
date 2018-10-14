#Round 1c 2017 Problem A
from itertools import combinations
import math

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n,k  = [int(s) for s in raw_input().split(" ")]
        table = []
        for j in xrange(n):
            table.append([int(s) for s in raw_input().split(" ")])
        print "Case #{}: {}".format(i, pancake(n,k,table))

def pancake(n,k,table):
    surface = []
    for each in combinations(xrange(n),k):
        l = []
        for i in xrange(k):
            l.append(table[each[i]])
        l.sort(reverse=True)
        area = 2*math.pi*l[0][0]*l[0][1]+math.pi*(l[0][0]**2)
        for i in xrange(1,len(l)):
            area += 2*math.pi*l[i][0]*l[i][1]
        surface.append(area)
    return max(surface)

def input():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n = int(raw_input())
        print "Case #{}:".format(i)
        for j in xrange(n):
            print raw_input()

if __name__ == '__main__':
    main()
