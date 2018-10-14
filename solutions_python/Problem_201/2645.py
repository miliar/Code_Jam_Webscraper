from heapq import *
import sys
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for t in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    heap = []
    array = [False] * (n+2)
    array[0] = True
    array[len(array)-1] = True

    heappush(heap, (t*-1, (0,len(array)-1)))
    last = 0

    for j in range(0,k):
        start, end = heappop(heap)[1]
        size = (end - start)+1
        add_pos = start+(size/2)
        last = add_pos
        array[add_pos] = True

        count_empty_1 = add_pos - start - 1
        count_empty_2 = end - add_pos - 1

        heappush(heap, (count_empty_1*-1,(start,add_pos)))
        heappush(heap, (count_empty_2*-1,(add_pos,end)))

    min = sys.maxint
    max = -sys.maxint
    current_min = 0
    current_max = 0
    for i in range(last-1,-1,-1):
        if array[i]:
            if current_min < min:
                min = current_min
            if current_max > max:
                max = current_max
            break
        else:
            current_min += 1
            current_max += 1

    current_min = 0
    current_max = 0
    for i in range(last+1, len(array)):
        if array[i]:
            if current_min < min:
                min = current_min
            if current_max > max:
                max = current_max
            break
        else:
            current_min += 1
            current_max += 1

    print "Case #{}: {} {}".format(t, max, min)
# check out .format's specification for more formatting options