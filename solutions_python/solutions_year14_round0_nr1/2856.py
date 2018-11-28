def magic(row1, arr1, row2, arr2):
    ans = set(arr1[row1 - 1]).intersection(set(arr2[row2 - 1]))
    if len(ans) == 1:
        return ans.pop()
    if len(ans) > 1:
        return 'Bad magician!'
    return 'Volunteer cheated!'


T = int(raw_input())
for case in xrange(T):
    row1 = int(raw_input())
    arr1 = [[int(card) for card in raw_input().split()] for _ in xrange(4)]
    row2 = int(raw_input())
    arr2 = [[int(card) for card in raw_input().split()] for _ in xrange(4)]
    status = magic(row1, arr1, row2, arr2)
    print 'Case #%d: %s' % (case + 1, status)
