read_ints = lambda: map(int, raw_input().split())

# pal: palindrome
def is_pal(x):
    x = str(x)
    for _ in xrange(len(x)/2):
        if x[_] != x[-_-1]:
            return False
    else:
        return True

# 2036 --> 20366302
def gen1(x):
    x = str(x)
    return x + ''.join(reversed(x))

# 2036 --> 2036302
def gen2(x):
    x = str(x)
    return x + ''.join(reversed(x[:-1]))

BOUND = 10**100

sqs = [] # all fair palindromic squares <= BOUND

def gao(s):
    def maybe_add(y1):
        if is_pal(y1) and y1 <= BOUND:
            sqs.append(y1)
            return True
        return False

    for c in '0123':
        if not s and c == '0':
            continue
        s2 = s + c
        x1 = int(gen1(s2))
        x2 = int(gen2(s2))
        y1 = x1 * x1
        y2 = x2 * x2
        res1 = maybe_add(y1)
        res2 = maybe_add(y2)
        if not res1 and not res2:
            return
        gao(s2)

gao('')
#for _ in sorted(sqs):
#    print _
#print 'len = %d' % len(sqs)

T = int(raw_input())
for no_t in xrange(1, T + 1):
    #A, B = 1, BOUND # stress test?
    A, B = read_ints()
    ans = 0
    for _ in sqs:
        if A <= _ <= B:
            ans += 1
    print 'Case #%d: %s' % (no_t, ans)
