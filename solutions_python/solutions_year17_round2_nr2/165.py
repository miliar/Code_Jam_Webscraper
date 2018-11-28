from random import random
import math
import re
import fractions

#fileio
fileName = 'C-large'
# fileName = 'C-small-attempt1'
# fileName = 'C-test'
input = fileName + ".in"
output = fileName + ".myout"
MOD = 10**9+7

###
with open(input) as fi, open(output, "w") as fo:
    T = fi.readline()
    for count in xrange(1, int(T)+1):
        def f():
            m = "ROYGBV"
            arr = map(int, fi.readline().strip().split())
            N = arr[0]
            colors = arr[1:]
            oc = colors[:]
            # print colors
            if N == 1:
                return m[colors.index(1)]
            x = []
            for i in [1,3,5]:
                s = ""
                while colors[i] > 0:
                    if colors[i-3] > 0:
                        s += m[i-3] + m[i]
                        colors[i] -= 1
                        colors[i-3] -= 1
                        N -= 2
                    else:
                        return "IMPOSSIBLE"
                if s:
                    if N > 0 or len(x) > 0:
                        if colors[i-3] > 0:
                            s += m[i-3]
                            colors[i-3] -= 1
                            N -= 1
                        else:
                            return "IMPOSSIBLE"
                    x.append(s)
                    colors[i-3] += 1
                    N += 1
            r = []
            # print x, colors, N
            if N > 0:
                rby = map(lambda i: (colors[i*2], i*2), [0,1,2])
                mxsort = sorted(rby)
                r = [mxsort[2][1]]
                colors[mxsort[2][1]] -= 1
                N -= 1
                def mx(first, last):
                    if last == 0:
                        a = [2,4]
                    elif last == 2:
                        a = [0,4]
                    else:
                        a = [0,2]
                    if colors[a[0]] == colors[a[1]]:
                        if a[0] == first:
                            return a[0]
                        else:
                            return a[1]
                    return a[0] if colors[a[0]] > colors[a[1]] else a[1]
                while N > 0:
                    N -= 1
                    t = mx(r[0], r[-1])
                    if colors[t] > 0:
                        r.append(t)
                        colors[t] -= 1
                    else:
                        return "IMPOSSIBLE"
                r = map(lambda i: m[i], r)
                # print r
                if r[0] == r[-1] and len(r) > 1:
                    return "IMPOSSIBLE"
                # print r, x, colors
                for xx in x:
                    found = r.index(xx[0])
                    r = r[:found] + [xx] + r[found+1:]
                print colors
                r = "".join(r)
            if r[0] == r[-1]:
                return "IMPOSSIBLE"
            return r


        #normal
        resultStr = "Case #"+str(count)+": "+f()
        print resultStr
        fo.write(resultStr+'\n')
