


def findL(stalls, place):
    number = -1
    while not stalls[place]:
        number += 1
        place -= 1
    return number

def findR(stalls, place):
    number = -1
    while not stalls[place]:
        number += 1
        place += 1
    return number

def solution(n, k):
    stalls = [1,1]
    for i in range(0, n):
        stalls.insert(1, 0)
    while k is not 0:
        minset = {}
        maxset = {}
        sl = -1000000
        sr = -1000000
        maxl = -1000000
        maxr = -1000000
        minset.update({0: [sl, sr]})
        maxset.update({0: [maxl, maxr]})
        for j in range(1, len(stalls)-1):
            tl = findL(stalls, j)
            tr = findR(stalls, j)
            if min(tl, tr) > min(sl, sr):
                sl = tl
                sr = tr
                minset.clear()
                minset.update({j: [tl, tr]})
            if min(tl, tr) == min(sl, sr):
                minset.update({j: [tl, tr]})
        if (k is not 1) and (len(minset) == 1):
            stalls[minset.popitem()[0]] = 1
        for o in minset:
            tl = minset.get(o)[0]
            tr = minset.get(o)[1]
            if max(tl, tr) > max(maxl, maxr):
                maxl = tl
                maxr = tr
                maxset.clear()
                maxset.update({o: [tl, tr]})
            if max(tl, tr) == max(maxl, maxr):
                maxset.update({o: [tl, tr]})
        stalls[maxset.popitem()[0]] = 1
        if k == 1:
            return (max(maxl, maxr), min(sl, sr))
        k -= 1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [r for r in input().split(" ")] # s = String, n = Number of flip per flipper
    print("Case #{}: {} {}".format(i, solution(int(n), int(k))[0], solution(int(n), int(k))[1]))
