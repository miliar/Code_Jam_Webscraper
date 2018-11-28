# f = open('B-small-attempt3b.in')
# rl = f.readline
rl = lambda: raw_input().strip()

def count_inversions(A):
    ret = 0
    for i in xrange(len(A)):
        for j in xrange(i):
            if A[j] > A[i]:
                ret += 1
    return ret

cases = int(rl())
for cc in xrange(cases):
    print 'Case #%d:' % (cc+1),

    n = int(rl())
    A = map(int, rl().split())

    max_index = 0
    max_value = A[0]
    for i in xrange(n):
        if max_value < A[i]:
            max_value = A[i]
            max_index = i

    ret = n*n+1

    for mask in xrange(2**n):
        if mask & (2 ** max_index): continue

        # if mask == 62: 
        #     import pdb; pdb.set_trace()
        L = []
        R = []
        from_left = from_right = 0
        cand = 0
        for i in xrange(n):
            if i == max_index: continue
            at_left = (mask & (2 ** i)) > 0

            if i < max_index and not at_left:
                cand += max_index - i - from_left
                from_left += 1
            elif max_index < i and at_left:
                cand += i - max_index - from_right
                from_right += 1

            if at_left:
                L.append(A[i])
            else:
                R.append(A[i])

        # print 'mask', mask
        # print '\tL %s R %s from_left %d from_right %d' % (L, R, from_left,
        #                                                   from_right)
        cand += from_left * from_right
        cand += count_inversions(L)
        cand += count_inversions(list(reversed(R)))

        ret = min(ret, cand)

    print ret


