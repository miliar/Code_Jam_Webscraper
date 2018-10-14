def complete(s):
    for x in s:
        if x != '+':
            return False
    return True

def solve():
    s, k = raw_input().split()
    n = len(s)
    s = list(s)
    k = int(k)
    ans = 0
    for i in xrange(0, n - k + 1):
        # print i
        # print s
        if complete(s):
            # print "Completed"
            break
        if s[i] == '-':
            ans += 1
            # flip
            for j in xrange(i, i + k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
        else:
            # do nothing
            pass
    if complete(s):
        return ans
    else:
        return "IMPOSSIBLE"


def main():
    t = int(raw_input())
    for qq in xrange(t):
        ans = solve()
        print "Case #{0}: {1}".format(qq + 1, ans)

if __name__ == '__main__':
    main()
