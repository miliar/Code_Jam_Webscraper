import math
import sys

#def calc(arr):
#    pos = []
#    turns = 0
#    count = max(arr)
#    while count:
#        arr.sort()
#        pos.append(turns + max(arr))
#        m = max(arr)
#        if m <2:
#            break
#        if m==9 and arr[len(arr)/2]>5:
#            arr[arr.index(m)] = math.ceil(m/3.0)
#            arr.append(m-math.ceil(m/3.0))
#        else:
#            arr[arr.index(m)] = math.ceil(m/2.0)
#            arr.append(m-math.ceil(m/2.0))
#        if max(arr) < count:
#            count = max(arr)
#        turns += 1
#        count -= 1
#        
#    return min(pos)

def calc(arr, turns, max_turns):
    i = arr.index(max(arr))
    m = arr[i]
    if max_turns-turns <=0:
        return turns + m
    if m <=3:
        return m+turns
    arr.pop(i)
    d = m-math.ceil(m/2.0)
    arr.append(d)
    arr.append(m-d)
    r1 = calc(arr, turns+1, max_turns)
    arr.pop(-1)
    arr.pop(-1)
    d = m-math.ceil(m/3.0)
    arr.append(d)
    arr.append(m-d)
    r2 = calc(arr, turns+1, max_turns)
    arr.pop(-1)
    arr.pop(-1)
    arr.insert(i, m)
    return min(turns + max(arr), r1, r2)
    

f = open(sys.argv[1])
cases = int(f.readline().strip())
for i in xrange(1, cases + 1):
    f.readline()
    case = f.readline().strip()
    case = [int(c) for c in case.split()]
    #if i==4: print "Case #%d: %d" % (i, calc(case, 0, max(case)))
    print "Case #%d: %d" % (i, calc(case, 0, max(case)))
