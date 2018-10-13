test_num = int(raw_input())
for test in xrange(test_num):
    answer = int(raw_input())
    for _ in xrange(answer - 1):
        raw_input()
    row1 = raw_input().split()
    for _ in xrange(4 - answer):
        raw_input()
    answer = int(raw_input())
    for _ in xrange(answer - 1):
        raw_input()
    row2 = raw_input().split()
    for _ in xrange(4 - answer):
        raw_input()
    common = [i for i in row1 if i in row2]
    l = len(common)
    if l == 1:
        answer = common[0]
    elif l == 0:
        answer = 'Volunteer cheated!'
    else:
        answer = 'Bad magician!'
    print 'Case #%d: %s' % (test + 1, answer)