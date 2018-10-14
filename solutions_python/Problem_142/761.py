def process_name(name):
    curr = 0
    rv = []
    while curr < len(name):
        _curr = curr
        while _curr < len(name) and name[_curr] == name[curr]:
            _curr += 1
        rv.append((name[curr], _curr - curr))
        curr = _curr
    return rv

def possible(l1, l2):
    if len(l1) != len(l2):
        return False
    for a1, a2 in zip(l1, l2):
        if a1[0] != a2[0]:
            return False
    return True

def uber(names, i):
    mi = 1000
    ma = 0
    for j in xrange(len(names)):
        mi = min(mi, names[j][i][1])
        ma = max(ma, names[j][i][1])
    best = 1000
    for target in xrange(mi, ma + 1):
        value = 0
        for j in xrange(len(names)):
            value += abs(target - names[j][i][1])
        best = min(best, value)
    return best

def process_game():
    N = int(raw_input())
    names = []
    for i in xrange(N):
        names.append(process_name(raw_input()))
    for i in xrange(1, N):
        if not possible(names[0], names[i]):
            print "Fegla Won"
            return
    best = 0
    for i in xrange(len(names[0])):
        best += uber(names, i)
    print best
    

for i in xrange(1, int(raw_input()) + 1):
    print "Case #%d:" % (i),
    process_game()
