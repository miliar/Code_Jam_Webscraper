#!/usr/bin/python

import sys

def solve(n):
    #print n
    ary = []
    while n != 0:
        ary.insert(0, n % 10)
        n /= 10
    k1 = ary[-1]
    found = False
    min_swap = None
    for j in range(1, len(ary)):
        for i in range(1, len(ary)-j+1):
            if ary[-i-j] < ary[-j]:
                if not min_swap:
                    min_swap = (-i-j, -j)
                    #print min_swap
                else:
                    if min_swap[0] < -i-j:
                        min_swap = (-i-j, -j)
                    elif min_swap[0] == -i-j:
                        if ary[-j] < ary[min_swap[1]]:
                            min_swap = (-i-j, -j)
                            #print min_swap
                found = True
                break
    if not found:
        smallest = 10
        for e in ary:
            if e < smallest and e != 0:
                smallest = e
        for i in range(0, len(ary)):
            if ary[i] == smallest:
                ary.pop(i)
                break
        ary.sort()
        result = [smallest, 0] + ary
        return "".join(map(str, result))
    else:
        tmp = ary[min_swap[0]]
        ary[min_swap[0]] = ary[min_swap[1]]
        ary[min_swap[1]] = tmp
        #print i
        left = ary[:min_swap[0]+1]
        right = ary[min_swap[0]+1:]
        #print left
        right.sort()
        #print right
        return "".join(map(str, left + right))

def main():
    f = file(sys.argv[1])
    n = int(f.readline())
    for testno in range(0, n):
        ans = solve(int(f.readline()))
        print "Case #%d: %s" % (testno + 1, ans)

if __name__ == '__main__':
    main()
