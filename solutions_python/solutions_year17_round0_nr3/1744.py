from Queue import PriorityQueue
class segment():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = end - start
    def __cmp__(self, obj):
        return cmp([-self.length, self.start], [-obj.length, obj.start])
def main():
    n = int(raw_input())
    for i in xrange(n):
        ans = solve()
        print_ans(ans, i)

def print_ans(ans, i):
    print 'Case #%d: %s' % (i +1, ans)

def solve():
    s = raw_input()
    n = int(s.split(' ')[0])
    k = int(s.split(' ')[1])
    init_seg = segment(0, n+1)
    queue = PriorityQueue()
    queue.put(init_seg)
    l, r = 0, 0
    while k > 0:
        k -= 1
        seg = queue.get()
        mid = (seg.start + seg.end) / 2
        left_seg = segment(seg.start, mid)
        right_seg = segment(mid, seg.end)
        l, r = mid - seg.start -1, seg.end - mid - 1
        for s in [left_seg, right_seg]:
            if s.length > 1:
                queue.put(s)
    return '%d %d' % (r, l)

if __name__ == "__main__":
    main()

