"""
Dancing With the Googlers
https://code.google.com/codejam/contest/1460488/dashboard#s=p1
"""

def main():
    T = int(raw_input())
    for id in xrange(T):
        nums = [int(s) for s in raw_input().split(' ')]
        N = nums.pop(0)
        S = nums.pop(0)
        p = nums.pop(0)
        ans = 0
        for t in nums:
            if t < p:
                continue
            if t >= p * 3 - 2:
                ans = ans + 1
            elif t >= p * 3 - 4 and S > 0:
                ans = ans + 1
                S = S - 1
        print "Case #%d: %d" % (id + 1, ans)

main()
