with open('output', 'w') as fw:
    for idx, line in enumerate(open('A-large.in')):
        if not idx == 0:
            crawd = [int(c) for c in line.strip().split()[1]]
            active = []
            culmu = 0
            for thres, x in enumerate(crawd):
                active.append(x + culmu - thres - 1)
                culmu += x
            active.append(0)
            fw.write('Case #{idx}: {friend}\n'.format(idx=idx, friend=-min(active)))
