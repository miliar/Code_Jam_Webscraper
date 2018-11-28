import itertools
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

def secondSmallest(li):
    lic = li[:]
    cm = min(lic)
    try:
        while True:
            lic.remove(cm)
    except:
        try:
            return min(lic)
        except:
            return "done"
def success(pos, fail):
    p = 0
    for i in range(0, len(pos)):
        a= reduce(lambda x, y: x*y, pos[i])
        if fail[i] != []:
            b = reduce(lambda x, y: x*y, fail[i])
        else:
            b = 1
        p += a*b
    return p
##probs = [0.9, 0.8]
##pos = []
##fail = []
##k = 1
##n = 2
##for i in range(k, n+1):
##    for j in itertools.combinations(probs, i):
##        pos.append(j)
##        fail.append([1-item for item in probs if item not in j])
##print(list(pos))
##print(fail)
##print(success(pos, fail))
##print("h")
t = int(input())
for test in range(1, t+1):
    data = [int(x) for x in input().split()]
    n = data[0]
    k = data[1]
    u = float(input())
    probs = [float(x) for x in input().split()]
    while round(u, 10) != 0:
##        print(u)
##        print(probs)
        curMin = min(probs)
        sec = secondSmallest(probs)
        if sec == "done":
            d = u/len(probs)
            for i in range(0, len(probs)):
                if probs[i] == curMin:
                    probs[probs.index(curMin)] +=d
                    u -= d
        else:
            diff = sec-curMin
            if probs.count(curMin) == 1:
                if u >= diff:
                    probs[probs.index(curMin)] = sec
                    u -= diff
                else:
                    probs[probs.index(curMin)] += u
                    u = 0
            else:
                oc = probs.count(curMin)
##                print(curMin)
##                print(diff)
                if u >= diff*oc:
                    for i in range(0, len(probs)):
                        if probs[i] == curMin:
                            probs[probs.index(curMin)] = sec
                            u -= diff
                else:
                    nd = u/oc
                    for i in range(0, len(probs)):
                        if probs[i] == curMin:
                            probs[probs.index(curMin)] += nd
                            u -= nd
    
    print("Case #" + str(test) + ": " + str(reduce(lambda x, y: x*y, probs)))
