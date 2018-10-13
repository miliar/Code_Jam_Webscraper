def ratatuj(input):
    lines = input.split('\n')
    cases = int(lines.pop(0))
    for case in range(cases):
        destination, num_horses = (int(x) for x in lines.pop(0).split(' '))
        horses = []
        for i in range(num_horses):
            horses.append([float(x) for x in lines.pop(0).split(' ')])

        print 'Case #%d: %s' % (case+1, solve(destination, num_horses, horses))


def solve(destination, num_horses, horses):
    # print ''
    # print destination
    # print num_horses
    # print(horses)

    horses = sorted(horses, key=lambda x: x[1])
    time = 0

    for horse in horses:
        time = max(time, (destination - horse[0]) / horse[1])


    return destination / time


ratatuj(input)