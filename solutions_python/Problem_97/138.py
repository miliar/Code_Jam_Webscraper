def rotate(num):
    num = str(num)
    digits = len(num)
    ans = list()
    for x in xrange(digits-1):
        num = ''.join((num[-1], num[:-1]))
        ans.append(num)
    ans = list(set(ans))
    return filter(lambda x: x > 10**(digits-1), map(int, ans))

T = int(raw_input())

for case in xrange(T):
    A, B = map(int, raw_input().split(' '))

    ans = set()

    for i in xrange(A, B+1):
        rotations = filter(lambda x: x <= B, rotate(i))
        for rotation in rotations:
            if i < rotation:
                ans.add((i, rotation))
            elif rotation > i:
                ans.add((rotation, i))

    print 'Case #%s: %s' %(case+1, len(ans))
