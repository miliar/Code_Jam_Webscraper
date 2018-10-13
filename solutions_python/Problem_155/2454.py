cases = int(raw_input())

for i in range(cases):
    shyness = map(int, raw_input().split(' ')[1])
    to_add = 0
    standing = 0

    for looking_for in range(len(shyness)):
        sitting = shyness[looking_for]
        will_add = 0

        if sitting > 0:
            if standing < looking_for:
                will_add = looking_for - standing
            standing += will_add + sitting

        to_add += will_add

    print 'Case #%d: %d' % (i+1, to_add)