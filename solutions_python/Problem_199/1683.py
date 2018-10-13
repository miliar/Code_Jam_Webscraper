def main():
    n = int(raw_input())
    for i in xrange(n):
        ans = solve()
        print_ans(ans, i)

def print_ans(ans, i):
    print 'Case #%d: %s' % (i +1, ans)

def solve():
    i = raw_input()
    s = i.split(' ')[0]
    k = int(i.split(' ')[1])
    total = 0
    cut = s.find('-')
    while cut >= 0:
        s = s[cut:]
        total += 1
        if len(s) < k:
            return 'IMPOSSIBLE'
        s = flip(s,k)
        cut = s.find('-')
    return str(total)
def flip(s, k):
    return ''.join([swap(c) for c in s[:k]]) + s[k:]

def swap(s):
    if s == '-':
        return '+'
    return '-'

if __name__ == "__main__":
    main()

