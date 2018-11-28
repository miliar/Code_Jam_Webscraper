import sys


def solve(case, buttons):
    def fill_next(n, b):
        for k in n:
            if n[k]:
                continue
            for b in buttons:
                if b[0] == k:
                    n[k] = b[1]
                    break 

    bots = {'O': 1, 'B': 1}
    next_p = {'O': None, 'B': None}
    steps = 0
    while True:
        fill_next(next_p, buttons)
        try:
            next_bot, next_but = buttons[0]
        except IndexError:
            break

        steps += 1
        for bot, pos in bots.iteritems():
            if bot == next_bot and pos == next_but:
                buttons.pop(0)
                next_p[bot] = None
            else:
                if pos < next_p[bot]:
                    bots[bot] += 1
                elif pos > next_p[bot]:
                    bots[bot] -= 1

    print "Case #%d: %d" % (case, steps)


tests = int(sys.stdin.readline())
for test_case in range(1, tests + 1):
    number_buttons, sequence = sys.stdin.readline().split(None, 1)
    sequence = sequence.split()
    buttons = []
    for i in range(0, int(number_buttons) * 2, 2):
        buttons.append((sequence[i], int(sequence[i + 1])))


    solve(test_case, buttons)
