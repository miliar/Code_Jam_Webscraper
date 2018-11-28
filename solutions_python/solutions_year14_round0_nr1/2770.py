def solve(_A, _B, A, B):
    cardsA = A[_A]
    cardsB = B[_B]
    matches = [0]*4

    for a in cardsA:
        i = 0
        for b in cardsB:
            if a == b:
                matches[i] = a
            i += 1

    ans = [v for v in matches if v != 0]
    if len(ans) == 1:
        return ans[0]
    if any(matches):
        return 'Bad magician!'
    return 'Volunteer cheated!'

T = input()
for i in range(1, T+1):
    _A = input()
    A = [map(int, raw_input().split()) for _ in range(4)]
    _B = input()
    B = [map(int, raw_input().split()) for _ in range(4)]

    print 'Case #%d: %s' % (i, solve(_A-1, _B-1, A, B))
