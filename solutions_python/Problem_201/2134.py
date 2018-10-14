

class LL(object):
    __slots__ = ('val', 'next')

    def __init__(self, val, next=None):
        self.val = val
        self.next = None


t = int(raw_input())

for ti in xrange(1, t + 1):
    n, k = map(int, raw_input().strip().split(" "))

    fst_chnk = LL(n)

    for _ in xrange(k):
        min_chnk = LL((fst_chnk.val - 1) / 2)
        max_chnk = LL(min_chnk.val + (fst_chnk.val - 1) % 2)

        if fst_chnk.next:
            fst_chnk = fst_chnk.next

            chnk = fst_chnk
            while chnk.next and chnk.next.val >= max_chnk.val:
                chnk = chnk.next
            max_chnk.next = chnk.next
            chnk.next = max_chnk

            chnk = max_chnk
            while chnk.next and chnk.next.val >= min_chnk.val:
                chnk = chnk.next
            min_chnk.next = chnk.next
            chnk.next = min_chnk

        else:
            fst_chnk = max_chnk
            fst_chnk.next = min_chnk

    print "Case #{}: {} {}".format(ti, max_chnk.val, min_chnk.val)
