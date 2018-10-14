def small(n, r, o, y, g, b, v): #r, y, b only
    horses = {'R': r, 'Y': y, 'B': b}
    most = max(r, y, b)
    if sum([r,y,b]) - most < most:
        return 'IMPOSSIBLE'
    # others = set(horses) - set(max_color)
    sequence = []
    valid_horses = set(horses)
    placed = 0
    while placed < n:
        next_color = max(valid_horses, key=horses.get)
        sequence.append(next_color)
        horses[next_color] -= 1
        valid_horses = set(horses) - set(sequence[placed])
        placed += 1

    if sequence[-1] == sequence[0]:
        color = sequence[0]
        idx = len(sequence)-2
        while sequence[idx] == color or sequence[idx-1] == color:
            idx -= 2
        sequence[idx] = color+sequence[idx]
        sequence = sequence[:-1]
    return ''.join(sequence)

# small(12,4,0,4,0,4,0)
# print small(4, 2, 0, 1, 0, 1, 0)


t = int(raw_input())
for i in xrange(1, t+1):
    n, r, o, y, g, b, v = [int(x) for x in raw_input().split(' ')]
    print 'Case #{}: {}'.format(i, small(n, r, o, y, g, b, v))
