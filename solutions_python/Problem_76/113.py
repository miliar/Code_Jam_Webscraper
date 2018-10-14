import math
import sys

def largest_power(x):
    return 2**int(math.log(x, 2))

def insert_sorted(elem, list):
    for i in range(0, len(list)):
        if elem < list[i]:
            list.insert(i, elem)

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    N = int(f.readline())
    values = [int(x) for x in f.readline().split()]
    xor = 0
    sum = 0
    for i in range(0, len(values)):
        xor = xor ^ values[i]
        sum += values[i]
    if xor != 0:
        print "Case #%d: NO" % (case + 1)
        continue
    values.sort()
    print "Case #%d: %d" % (case + 1, sum - values[0])
"""
    sean = values
    patrick = []
    sean.sort()
    patrick = [sean[0]]
    sean = sean[1:]
    diff = xor ^ patrick[0]
    sum = sum - patrick[0]
    while diff != 0:
        find = largest_power(diff)
        print sum, diff, find
        next_turn = False
        if len(patrick) > 0:
            for i in range(0, len(patrick)):
                if patrick[i] >= find:
                    val = patrick.pop(i)
                    insert_sorted(val, sean)
                    diff = diff ^ val
                    sum += val
                    next_turn = True
                    break
        if next_turn:
            continue
        for i in range(0, len(sean)):
            if sean[i] >= find:
                val = sean.pop(i)
                insert_sorted(val, patrick)
                diff = diff ^ val
                sum -= val
                break
    print "Case #%d: %d" % (case + 1, sum)
"""
