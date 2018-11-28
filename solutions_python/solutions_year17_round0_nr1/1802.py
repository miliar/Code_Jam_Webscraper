with open('A-large.in', 'r') as f:
    tasks = [l.strip().split() for l in f.readlines()[1:]]

for task_idx, t in enumerate(tasks):
    cakes, flipper = t[0], int(t[1])

    solved = False
    cake_idx = 0
    flips = 0
    while cake_idx < len(cakes)-flipper+1:
        cake_idx = cakes.find('-')
        if cake_idx == -1:
            solved = True
            break
        cakes = ''.join([
            cakes[:cake_idx],
            ''.join(['+' if p == '-' else '-' for p in cakes[cake_idx:cake_idx+flipper]]),
            cakes[cake_idx+flipper:]
        ])
        flips += 1
    print 'Case #{}:'.format(task_idx+1), flips if solved else 'IMPOSSIBLE'
