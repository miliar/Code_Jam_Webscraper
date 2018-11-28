import sys


def gen_arr(n):
    arr = [False]
    for i in range(n):
        arr.append(True)
    arr.append(False)
    return arr


def get_min_ids(arr):
    _max = -1
    ids = []
    arrlen = len(arr)
    for i in range(1, arrlen - 1):
        val = arr[i]
        if val != -1:
            if val > _max:
                ids = [i]
                _max = val
            elif val == _max:
                ids.append(i)
                _max = val
    return ids


def get_max_ids(arr, _ids):
    _max = -1
    ids = []
    arrlen = len(arr)
    for i in _ids:
        val = arr[i]
        if val != -1:
            if val > _max:
                ids = [i]
                _max = val
            elif val == _max:
                ids.append(i)
                _max = val
    return ids


def rate_stalls(stalls):
    rarr = [-1]
    larr = [-1]
    slen = len(stalls)
    for i in range(1, slen):
        l, r = 0, 0
        if stalls[i]:
            j = i - 1
            while stalls[j]:
                l += 1
                j -= 1
            j = i + 1
            while stalls[j]:
                r += 1
                j += 1
            rarr.append(r)
            larr.append(l)
        else:
            rarr.append(-1)
            larr.append(-1)
    return rarr, larr

def prob(stalls, k, case):
    while k:
        rarr, larr = rate_stalls(stalls)
        minarr = [min(larr[i], rarr[i]) for i in range(len(larr))]
        mins = get_min_ids(minarr)
        if len(mins) > 1:
            maxarr = [max(larr[i], rarr[i]) for i in range(len(larr))]
            maxs = get_max_ids(maxarr, mins)
            _id = maxs[0]
        else:
            _id = mins[0]
        stalls[_id] = False
        k -= 1
    print("Case #{}: {} {}".format(case, rarr[_id], larr[_id]))


with open('small0.in', 'r') as fin:
    T = int(fin.readline().strip())
    for i in range(1, T + 1):
        # N stalls
        # K ppl
        N, K = (int(x) for x in fin.readline().strip().split())
        arr = gen_arr(N)
        prob(arr, K, i)
