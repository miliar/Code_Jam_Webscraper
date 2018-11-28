from heapq import heappush, heappop
def get_position(n, k):

    if (n * 3)/4 < k - 1:
        return (0, 0)
    pos_diff = []
    heappush(pos_diff, -n)
    l = r = n
    ct = 0
    while len(pos_diff) > 0 and ct < k:
        cd = abs(heappop(pos_diff))
        ct += 1
        v = cd / 2
        if cd%2 == 0:
            l = v - 1
            r = v
            heappush(pos_diff, -v)
            heappush(pos_diff, -(v - 1))
        else:
            l = v
            r = v
            heappush(pos_diff, -v)
            heappush(pos_diff, -v)
    return (r, l)


#ans = get_position(821275, 662896)
#ans = get_position(8, 4)
#print ans
with open('/Users/girishkadli/Desktop/codejam/test.txt', 'r') as f:
    lines = f.readlines()
    t = int(lines[0])
    for i in range(1, t + 1):
        token = lines[i].split(' ')
        n = int(token[0])
        k = int(token[1])
        ans = get_position(n, k)
        print 'Case #%s: %s %s' % (str(i), str(ans[0]), str(ans[1]))
