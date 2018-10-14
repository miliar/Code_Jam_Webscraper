

from bisect import *
import sys

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def war(count, naomi, ken):
    points = 0

    for i in range(count):
        # XXX does this matter
        naomi_block = naomi.pop(0)
        
        j = bisect_right(ken, naomi_block)
        if j == len(ken):
            points += 1
            ken.pop(0) # remove min block
        else:
            ken.pop(j)

    return points

def deceitful_war(count, naomi, ken):
    points = 0
    while count != 0:
        naomi_min = naomi[0]
        ken_min = ken[0]
        ken_max = ken[-1]

        # Win smallest to smallest
        if naomi_min > ken_min:
            points += 1
            naomi.pop(0)
            ken.pop(0)
            
        # Lose smallest to largest
        else:
            naomi.pop(0)
            ken.pop(len(ken) - 1)

        count -= 1

    return points

def test(i):
    count = int(sys.stdin.readline())
    
    naomi = []
    for block in sys.stdin.readline().split():
        naomi.append(float(block))
        naomi.sort()

    ken = []
    for block in sys.stdin.readline().split():
        ken.append(float(block))
        ken.sort()

    war_points = war(count, list(naomi), list(ken))
    deceitful_war_points = deceitful_war(count, list(naomi), list(ken))
    print 'Case #' + str(i) + ':', deceitful_war_points, war_points

def main():
    T = sys.stdin.readline()

    for i in range(int(T)):
        test(i + 1)

main()
