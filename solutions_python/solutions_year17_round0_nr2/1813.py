def main():
    n = int(raw_input())
    for i in xrange(n):
        ans = solve()
        print_ans(ans, i)

def print_ans(ans, i):
    print 'Case #%d: %s' % (i +1, ans)

def solve():
    i = int(raw_input())
    idx = find_untidy(i)
    while idx >= 0:
        i = tidyup(i, idx)
        idx = find_untidy(i)
    return str(i)

def find_untidy(n):
    s = str(n)
    for i in xrange(len(s) - 1):
        if int(s[i]) > int(s[i+1]):
            return i
    return -1

def tidyup(n, idx):
    s = list(str(n))
    s[idx] = str(int(s[idx]) - 1)
    for i in xrange(idx+1, len(s)):
        s[i] = '9'
    return int(''.join(s))

if __name__ == "__main__":
    main()

