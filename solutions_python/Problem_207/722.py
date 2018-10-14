from collections import Counter
from itertools import izip_longest, repeat

letters = ('R', 'O', 'Y', 'G', 'B', 'V')

def B(n, colors):
    c = Counter(**colors)
    if c.most_common(1)[0][1] > n / 2:
        return "IMPOSSIBLE"
    ret = [None] * n
    el, k = c.most_common(1)[0]
    for i in range(0, n, 2):
        ret[i] = el
        k -= 1
        if not k:
            break

    iters = [repeat(el, times=times) for (el, times) in c.most_common()[1:]]
    seq = izip_longest(*iters)
    l = [list(filter(bool, q)) for q in seq]
    l = sum(l, [])
    for i in range(n):
        if ret[i] is None:
            ret[i] = l.pop()
    return ''.join(ret)



def main():
    t = int(raw_input().strip())
    for i in xrange(t):
        nums = map(int, raw_input().strip().split())
        n, nums = nums[0], nums[1:]
        colors = dict(zip(letters, nums))
        ans = B(n, colors)
        print "Case #%s: %s" % (i + 1, ans)

if __name__ == '__main__':
    main()