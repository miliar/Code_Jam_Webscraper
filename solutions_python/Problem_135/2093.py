

T = input()
for test in xrange(T):
    ans1 = input()
    row1 = raw_input()
    row2 = raw_input()
    row3 = raw_input()
    row4 = raw_input()

    row = row1
    if ans1 == 2:
        row = row2
    if ans1 == 3:
        row = row3
    if ans1 == 4:
        row = row4

    possible = set(row.split(' '))

    ans2 = input()
    row1 = raw_input()
    row2 = raw_input()
    row3 = raw_input()
    row4 = raw_input()

    row = row1
    if ans2 == 2:
        row = row2
    if ans2 == 3:
        row = row3
    if ans2 == 4:
        row = row4

    possible2 = set(row.split(' '))

    ans = possible.intersection(possible2)

    if len(ans) == 0:
        answer = 'Volunteer cheated!'
    if len(ans) > 1:
        answer = 'Bad magician!'
    if len(ans) == 1:
        answer = ans.pop()

    print 'Case #' + str(test + 1) + ': ' + answer
