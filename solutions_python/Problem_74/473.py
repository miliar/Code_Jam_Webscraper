def parse(l):
    robots = {'O': [], 'B': [] }
    buttons = {'O': 1, 'B': 1 }
    elements = iter(l.split())
    N = int(elements.next())
    for i in xrange(N):
        robot, button = elements.next(), int(elements.next())
        l = robots[robot]
        if buttons[robot] != button:
            l.append(('MOVE', button))
            buttons[robot] = button
        l.append(('PRESS', i, button))
    return robots['O'], robots['B']

def solve(l):
    O, B = list(parse(l))
    robots = {'O': O, 'B': B}
    pos = {'O': 1, 'B': 1}
    arrival = {'O': 0, 'B': 0}
    button_n = 0
    t = 0
    while O or B:
        button_pressed = False
        for r, actions in robots.items():
            if not actions:
                continue
            a = actions[0]
            if a[0] == 'MOVE':
                destination = a[1]
                current_pos = pos[r]
                arrival[r] = t + abs(current_pos - destination)
                pos[r] = destination
                del actions[0]
                # print t, 'Move', r, destination, arrival[r]
            else:
                assert(a[0] == 'PRESS')
                if arrival[r] <= t and a[1] == button_n:
                    assert(a[2] == pos[r])
                    button_pressed = True
                    del actions[0]
                    # print t, 'PRESS', r, a[2]
        if button_pressed:
            button_n += 1
        t += 1
    return t

if __name__ == '__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        t = solve(raw_input())
        print 'Case #%d: %d' % (i, t)
