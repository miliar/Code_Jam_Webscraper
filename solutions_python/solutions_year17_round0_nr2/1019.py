def solve(n):
    if (len(n) <= 1):
        return n
    ln = list(n)
    i = len(ln) - 1
    start = 0
    while i >= start + 1:
        if ln[i - 1] <= ln[i]:
            i = i - 1
            continue
        else:
            #if ln[i] == "0":
            ln[i - 1] = str(int(ln[i - 1]) - 1)
            j = i
            for jj in range (j, len(ln)):
                ln[jj] = "9"
            #else:
            #    ln[i] = "9"
            #    ln[i - 1] = str(int(ln[i - 1]) - 1)
            #    j = i
            #    for jj in range (j, len(ln)):
            #        ln[jj] = "9"
        i = i - 1
    res = ""
    for cc in ln:
        if cc == "0":
            start = start + 1
        else:
            break
    for cc in ln[start:]:
        res += cc
    return res

    
t=int(raw_input())
for cas in xrange(1,t+1):
    n=str(raw_input())
    print "Case #{}: {}".format(cas,solve(n))
