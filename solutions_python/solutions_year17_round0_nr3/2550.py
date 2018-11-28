cases = int(raw_input().split()[0])

def get(arr):
    v = max(arr)
    ind = arr.index(v)
    if arr.count(v) == 1:
        return (True, ind, v)
    else:
        return (False, ind, v)

def update(ls, rs, mins, maxs, ind):
    mins[ind] = -1
    maxs[ind] = -1
    upd_left = ls[ind]
    for i in range(upd_left):
        iup = ind - i - 1
        if mins[iup] != -1:
            rs[iup] = i
            mins[iup] = min(ls[iup], rs[iup])
            maxs[iup] = max(ls[iup], rs[iup])
    upd_right = rs[ind]
    for i in range(upd_right):
        iup = ind + i + 1
        if mins[iup] != -1:
            ls[iup] = i
            mins[iup] = min(ls[iup], rs[iup])
            maxs[iup] = max(ls[iup], rs[iup])            

for i in range(cases):
    data = raw_input().split()
    n = int(data[0])
    k = int(data[1])

    r = range(n)
    ls = [j for j in r]
    rs = [n - j - 1 for j in r]
    mins = [min(ls[j], rs[j]) for j in r]
    maxs = [max(ls[j], rs[j]) for j in r]

    index = None
    res_min = None
    res_max = None

    for p in range(k):
        first = get(mins)
        if first[0]:
            index = first[1]
            res_min = mins[index]
            res_max = maxs[index]
            update(ls, rs, mins, maxs, index)
        else:
            desired_min = first[2]
            new_maxs = [(maxs[t] if mins[t] == desired_min else -1) for t in r]
            second = get(new_maxs)
            index = second[1]
            res_min = mins[index]
            res_max = maxs[index]
            update(ls, rs, mins, maxs, index)
    
    print 'Case #%d: %d %d' % (i + 1, res_max, res_min)
