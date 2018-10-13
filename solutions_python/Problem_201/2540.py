def choose(available):
    current = 0
    index = 0
    for i, stalls in enumerate(available):
        if int(stalls) > current:
            current = int(stalls)
            index = i

    if current % 2 == 0:
        right = current / 2
        left = right - 1
    else:
        right = current / 2
        left = right
    r = []
    for i, s in enumerate(available):
        if i == index:
            r.append(left)
            r.append(right)
        else:
            r.append(s)
    return r, max(left, right), min(left, right)
    
def process(s):
    stalls, person = s.split(' ')
    available = []
    available.append(int(stalls))
    for i in range(int(person)):
        available, _max, _min = choose(available)
    return _max, _min

t = int(raw_input())
for i in xrange(1, t + 1):
    _max, _min = process(raw_input())    
    print "Case #{}: {} {}".format(i, _max, _min)