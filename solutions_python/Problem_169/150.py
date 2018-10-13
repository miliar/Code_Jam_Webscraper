import sys

def _cc():
    for line in sys.stdin:
        for x in line.strip().split():
            yield x

_cin = _cc()
cin = _cin.next
GGGG = 10000.0

def ok(T, vol, temp, data):
    if sum(T * x[0] for x in data) < vol:
        return False
    curr_vol = 0
    curr_mass = 0
    for rate, mytemp in data:
        myvol = rate * T
        totake = min(vol - curr_vol, myvol)
        if myvol < vol - curr_vol:
            gg = True
        else:
            gg = False

        curr_vol += totake
        curr_mass += totake * mytemp
        if not gg:
            break

    min_temp = curr_mass
    
    curr_vol = 0
    curr_mass = 0
    for rate, mytemp in reversed(data):
        myvol = rate * T
        totake = min(vol - curr_vol, myvol)
        if myvol < vol - curr_vol:
            gg = True
        else:
            gg = False
        curr_vol += totake
        curr_mass += totake * mytemp
        if not gg:
            break
    max_temp = curr_mass
    #print min_temp, temp * vol, max_temp
    return min_temp  <= temp * vol <= max_temp


def solve(vol, temp, data_):
    data = sorted(data_, key=lambda x: (x[1],-1*x[0]))
    if all(x[1] > temp for x in data):
        return "IMPOSSIBLE"
    if all(x[1] < temp for x in data):
        return "IMPOSSIBLE"
    assert all(data[i][1] <= data[i+1][1] for i in xrange(0, len(data)-1))

    low = 0.0
    high = 1e20
    for i in xrange(100):
        mid = (high + low) * 0.5
        xx = ok(mid, vol, temp, data)
        #print vol * temp, vol, temp, mid, low, high, xx
        if xx:
            high = mid
        else:
            low = mid
    return "%.12lf" % (mid)


def gparse(x):
    if '.' not in x:
        return int(x) * GGGG
    a, b = x.split('.')
    while len(b) < 4:
        b = b + '0'
    return int(a) * GGGG + int(b)

T = int(cin())
for cn in xrange(1,T+1):
    N, V, X = int(cin()), gparse(cin()), gparse(cin())
    data = list((gparse(cin()), gparse(cin())) for t in xrange(N))
    print "Case #%d: %s" % (cn, solve(V, X, data))
