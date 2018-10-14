import sys
from numpy import *

def main():
    f = open('B-small-attempt0.in')
    e = enumerate(f)

    count = int(e.next()[1])

    for i in range(count):
        res = test_it(i,e)
        print "Case #%d: %s"%(i+1, res)


def test_it(idx, e):
    nums = [int(n) for n in e.next()[1].split()]

    oldm = nums[0]
    newm = nums[1]

    buyed = nums[2]
    count = 0

    for f in range(oldm):
        for s in range(newm):
            if f&s < buyed:
                count = count +1

    return count

main()
