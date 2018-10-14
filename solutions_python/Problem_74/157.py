def solve(argss):
    position = {'O':1, 'B':1}
    steps = 0
    current = ''
    moves = 0
    argss.reverse()
    while argss:
        x = argss.pop()
        if current == x[0]:
            moves += abs(x[1]-position[x[0]])+1
            position[x[0]] = x[1]
        else:
            current = x[0]
            steps += moves
            if moves > abs(x[1] - position[x[0]]):
                moves = 1
            else:
                moves = abs(x[1]-position[x[0]])+1-moves

            position[x[0]] = x[1]

    steps += moves

    return steps

lines = raw_input().split('\n')
tests = int(lines[0])
for t in range(tests):
    args = lines[t+1].split()
    args = args[1:]
    args = zip(args[::2], args[1::2])
    args = map(lambda x: (x[0], int(x[1])), args)
    print 'Case #%d: %d' % (t+1, solve(args))

'''
1
4 O 26 B 26 B 67 O 69

'''
