CA = input()

T = [[1, 2, 3, 4], [2, -1, 4, -3], [3, -4, -1, 2], [4, 3, -2, -1]]
def mul(a, b):
    mul = abs(a * b) / (a * b)
    return mul * T[abs(a) - 1][abs(b) - 1]

for tc in range(1, CA + 1):
    L, X = map(int, raw_input().split())
    s = raw_input().strip() * X
    si, sj = False, False
    state = 1
    C = {'i': 2, 'j': 3, 'k': 4}
    for c in s:
        state = mul(state, C[c])
        if state == 2:
            si = True
        if state == 4 and si:
            sj = True
    ok = si and sj and state == -1


    print "Case #%d: %s" % (tc, 'YES' if ok else 'NO')
