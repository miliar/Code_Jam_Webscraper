import pdb
T = input()
def check(arr):
    for x in arr:
        if not x:
            return False
    return True
def flip(arr, p, k):
    narr = [0] * len(arr)
    for x in xrange(p):
        narr[x] = arr[x]
    for x in xrange(p, p+k):
        narr[x] = not arr[x]
    for x in xrange(p+k, len(narr)):
        narr[x] = arr[x]
    return narr

for test in xrange(T):
    row, k = raw_input().strip().split()
    k = int(k)
    row = map(lambda a: True if a == '+' else False, row)
    def comp(f, p, arr):
        if False in arr[:p]:
            return float("inf")
        #print f, p, arr
        #pdb.set_trace()
        c = check(arr)
        if c:
            return f
        if p == len(arr) - k + 1:
            return float("inf")
        return min(comp(f+1, p+1, flip(arr, p, k)), comp(f, p+1, arr))
    if k == 1:
        print "Case #%d: %d" % (test, len(filter(lambda a: not a, row)))
    else:
        val = comp(0, 0, row)
        if val == float("inf"):
            res = "IMPOSSIBLE"
        else:
            res = str(val)
        print "Case #%d: %s" % (test+1, res)
