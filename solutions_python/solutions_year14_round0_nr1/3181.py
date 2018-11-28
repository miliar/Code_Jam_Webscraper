from sets import Set


def get_matrix():
    A = [[0]*4] * 4
    for i in range(4):
        A[i] = map(int, raw_input().split())
    return A

N = int(raw_input())

for n in range(N):
    first_try = int(raw_input()) - 1
    A = get_matrix()

    second_try = int(raw_input()) - 1
    B = get_matrix()

    result = Set(A[first_try]) & Set(B[second_try])

    print 'Case #%d:' % (n+1),
    if not result:
        print 'Volunteer cheated!'
    elif len(result) > 1:
        print 'Bad magician!'
    else:
        print result.pop()
