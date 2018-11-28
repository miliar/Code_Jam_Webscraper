
M = None
K = 0
L = 0
S = None
N = int(raw_input().strip())
FLIP_MAP = {
    '+': '-',
    '-': '+',
}

def isAllPlus(s):
    return '-' not in s

def f(orig, _next):
    global M
    global L
    global K

    if isAllPlus(_next):
        if orig:
            if M[orig] is False:
                return 0
            else:
                # M[orig] is the minimum answer already
                raise Exception('Not sure this case occur or not')
        else:
            # All is + at the beginning
            M[_next] = 0
            return M[_next]

    # Going to expand _next
    orig = _next

    # Prune conditions
    if orig in M:
        return M[orig]

    # Mark node is processing
    M[orig] = False

    myCounts = []
    for i in xrange(L - K + 1):
        _next = [None] * L

        for index, c in enumerate(orig):
            if index >= i and (index < (i + K)):
                _next[index] = FLIP_MAP[c]
            else:
                _next[index] = c

        _next = ''.join(_next)

        # print 'orig', orig, i, 'next', _next
        result = f(orig, _next)
        # print 'orig', orig, i, 'next', _next, result
        if type(result) is int:
            myCounts.append(result)

    try:
        M[orig] = 1 + min(myCounts)
    except:
        M[orig] = False

    return M[orig]

for n in xrange(N):
    S, K = raw_input().strip().split(' ')
    K = int(K)
    M = {}
    L = len(S)
    # print 'S', S
    cnt = f(None, S)
    if type(cnt) is int:
        print 'Case #%d: %d' % (n + 1, cnt)
    else:
        print 'Case #%d: IMPOSSIBLE' % (n + 1)
    # print M