def solve(cookies, size):
    ret = 0
    for i in xrange(len(cookies) - size + 1):
        if cookies[i] == -1:
            ret += 1
            for t in xrange(size):
                cookies[i + t] *= -1
    return 'IMPOSSIBLE' if -1 in cookies else ret


if __name__ == '__main__':
    testcases = int(raw_input())
    for tc in xrange(testcases):
        cookies_str, size_str = raw_input().split()
        cookies = [1 if c == '+' else -1 for c in cookies_str]
        print 'Case #{}: {}'.format(tc + 1, solve(cookies, int(size_str)))
