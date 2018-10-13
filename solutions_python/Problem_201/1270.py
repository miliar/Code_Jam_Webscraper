import math
def calc_for_streak(length): #returns val & idx, same value
    minLR = (length - 1) / 2
    return minLR #val and idx reusable


def find_streaks(stalls): #returns (startidx, length)
    streaks = []
    started = None
    for i in xrange(len(stalls)):
        stall = stalls[i]
        if stall:
            if started is not None: #record it
                streaks.append((started, i-started))
                started = None
        elif not stall:
            if started is None: #start it
                started = i

    if started is not None:
        streaks.append((started, i-started+1))
    return streaks

def iterate(stalls):
    streaks = find_streaks(stalls)
    minLR, maxLR = None, None
    maxi, mini = None, None
    dupemin = False
    for (idx, length) in streaks:
        newminLR = calc_for_streak(length)
        newmini = newminLR + idx
        newmaxLR = (newminLR+1) if length % 2 == 0 else newminLR
        newmaxi = newmini

        if minLR is None or newminLR > minLR:
            dupemin = False
            minLR = newminLR
            maxLR = newmaxLR
            mini = newmini
            maxi = newmaxi
        elif newminLR == minLR:
            dupemin = True
            if newmaxLR > maxLR:
                maxLR = newmaxLR
                maxi = newmaxi

    next = mini
    if dupemin:
        next = maxi

    #error check
    if stalls[next]:
        'Already occupied! Somethings wrong'
    stalls[next] = True
    return stalls, maxLR, minLR



def f(numstalls, people):
    stalls = [False] * numstalls
    for i in xrange(people):
        stalls, maxLR, minLR = iterate(stalls)
    return maxLR, minLR


def MSB(n):
    ndx = 0
    while (1 < n):
        n = n >> 1
        ndx += 1
    return ndx+1

def g(x, n):
    return (x - n + 1) * 1. / n

def x(stalls, ppl):
    msb = MSB(ppl)
    msb_u = 2**msb
    msb_d = 2**(msb-1)

    n = g(stalls, msb_d)
    mx = round(n / 2)
    mn = math.floor(n / 2)
    frac = n % 1
    portion = (ppl - msb_d + 1) * 1. / msb_d
    if portion > frac:
        potential_floor = math.floor(g(stalls, msb_u))
        if mx == mn:
            mn -= 1
        else:
            mx -= 1
    return int(mx), int(mn)


#
# for i in xrange(2, 100):
#     a, b = f(729, i)
#     c, d = x(729, i)
#     print '{}: {} {}'.format(i, (a, b), (c,d))
#

t = int(raw_input())
for i in xrange(1, t+1):
    s, p = raw_input().split(' ')
    s = int(s)
    p = int(p)
    a, b = x(s, p)
    print 'Case #{}: {} {}'.format(i, a, b)
