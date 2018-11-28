T = int(raw_input())

for i in xrange(T):
    a = int(raw_input())
    first_grid = [raw_input().split(' ') for j in xrange(4)]
    b = int(raw_input())
    second_grid = [raw_input().split(' ') for j in xrange(4)]

    possible = [c for c in first_grid[a - 1] if c in second_grid[b - 1]]

    if len(possible) == 0:
        y = 'Volunteer cheated!'
    elif len(possible) == 1:
        y = '{}'.format(possible[0])
    else:
        y = 'Bad magician!'

    print 'Case #{}: {}'.format(i + 1, y)