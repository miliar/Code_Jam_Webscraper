def solve():
    t = int(raw_input())
    for case in xrange(t):
        n, s = raw_input().split()
        n = int(n)
        total = 0
        orig_sum = 0
        for i in xrange(n+1):
            if s[i] != '0':
                if total <= i:
                    total += (i-total) + ord(s[i])-ord('0')
                else:
                    total += ord(s[i])-ord('0')
            orig_sum += ord(s[i]) - ord('0')
        print "Case #" + str(case+1) + ": " + str(total-orig_sum)
if __name__ == '__main__':
    solve()
