#!/bin/python

# def getBits(val):
#     result = []
#     v = val
#     while v > 0:
#         result.append(v % 2)
#         v = v / 2
#     result.reverse()
#     return result

# def findMaxMin(n, k):
#     kbits = getBits(k)
#     spc = n
#     adjustment = 0                  # to order even cases properly
#     for b in kbits[1:]:
#         if spc % 2 == 1:
#             ls = (spc - 1) / 2
#             rs = ls
#         else:
#             if adjustment == 1:
#                 (ls, rs) = (spc/2, spc/2)
#             elif adjustment == 0:
#                 (ls, rs) = (spc/2, spc/2 - 1)
#             else:
#                 (ls, rs) = (spc/2 - 1, spc/2 - 1)
#         # set adjustment modifier
#         if ls == rs and ls % 2 == 0:
#             adjustment = 1 if b == 0 else -1
#         else:
#             adjustment = 0
#         spc = ls if b == 0 else rs

#     if spc == 0:
#         return (0, 0)
#     elif spc % 2 == 0:
#         return (spc/2, spc/2 - 1)
#     else:
#         return ((spc - 1)/2, (spc - 1)/2)

def split(spc):
    if spc % 2 == 0:
        return (spc/2, spc/2 - 1)
    else:
        return ((spc - 1)/2, (spc - 1)/2)

def consolidate(hist):
    n = len(hist)
    if n == 1:
        return hist
    else:
        result = []
        hist.sort(reverse=True)
        (spc, freq) = hist[0]
        i = 1
        while i < n:
            (nspc, nfreq) = hist[i]
            if nspc == spc:
                freq += nfreq
            else:
                result.append((spc, freq))
                spc, freq = nspc, nfreq
            i += 1
        result.append((spc, freq))
        return result

def getLevelStats(n, k):
    """Return the frequencies of the space sizes at time when kth user would
    appear"""
    def freqsplit(spc, freq):
        l, r = split(spc)
        return [(l, freq), (r, freq)]
    
    hist = [(n, 1)]
    tot = 0
    ntot = 1
    while ntot < k:
        # nexhist = reduce(lambda res, (s, f): res + freqsplit(s, f), hist, [])
        tot = ntot
        nexhist = []
        for (s, f) in hist:
            ntot += 2 * f
            (l, r) = split(s)
            nexhist += [(l, f), (r, f)]
        nexhist = consolidate(nexhist)
        hist = nexhist
    return (tot, hist)

def findMaxMin(n, k):
    (t, stats) = getLevelStats(n, k)
    n = len(stats)
    count = t
    i = 0
    while count < k and i < n:
        (spc, c) = stats[i]
        count += c
        i = i + 1
    return split(spc)
        
t = int(raw_input().strip())

for i in xrange(1, t+1):
    n, k = map(int, raw_input().strip().split(' '))
    hi, lo = findMaxMin(n, k)
    print "Case #%d: %d %d" % (i, hi, lo)


