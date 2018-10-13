import sys

def count_swaps(ll):
    ss = sorted(ll)
    total = 0
    while ss:
        num = ss.pop(0)
        total += min(ll.index(num),len(ll) -ll.index(num)-1)
        ll.remove(num)
    return total
        

with open(sys.argv[1]) as ff:
    t = int(ff.readline())
    for c in range(1,t+1):
        n = map(int,ff.readline().split())
        a = map(int,ff.readline().split())
        mm = count_swaps(a)
#         mm = -1
#         for i in range(0,len(a)+1):
#             tmp = count_swaps(a[:i], False) + count_swaps(a[i:], True)
#             print i, count_swaps(a[:i], False), count_swaps(a[i:], True)
#             if mm == -1 or tmp < mm:
#                 mm = tmp 
        print "Case #%d: %d" % (c,mm)