import math

PI = math.pi

def find(l, k):
    l = sorted(l, key=lambda x: x[0], reverse=True)
    store = []

    for v in l:
        a = float(PI) * float(math.pow(v[0], 2))
        b = float(2) * float(PI) * float(v[0]) * float(v[1])
        store.append([a, b])

    for i in range(len(store) - k):
        store = remove(store)

    summation = 0
    summation += store[0][0] + store[0][1]
    for i in range(1, len(store)):
        summation += store[i][1]
    
    return summation

def remove(l):
    selected = -1
    last_selected = -1
    
    for (i, v) in enumerate(l):
        if selected == -1 or l[selected][1] > v[1]:
            selected = i
        elif last_selected == -1 or l[last_selected][1] > v[1]:
            last_selected = i

    if selected == 0 and is_replaced(l, last_selected) != True:
        del l[last_selected]
        return l

    del l[selected]
    return l

    
def is_replaced(l, last_selected):
    a = (l[0][0] - l[1][0]) + l[0][1]
    b = l[last_selected][1]

    return a < b
    
    
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    l = []
    for j in xrange(n):
        r, h = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        l.append([r, h])

    solution = find(l, k)

    print "Case #%d: %f" % (i, solution)
    # check out .format's specification for more formatting options
 
