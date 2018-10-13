#!/usr/bin/env python3
t = int(input())

for case in range(1, t+1):
    n, r, o, y, g, b, v = map(int, input().split())
    if max([r+o+v, y+o+g, b+g+v]) > n/2:
        print('Case #{}: {}'.format(case, 'IMPOSSIBLE'))
        continue
    horses = sorted([[r,'R'], [o,'O'], [y,'Y'], [g,'G'], [b, 'B'], [v,'V']], reverse=True)
    horses = [[x, 5-i, c] for i, (x,c) in enumerate(horses)]
    last = None
    answer = []
    for i in range(n):
        horse = horses[1] if horses[0][2] == last else horses[0]
        horse[0] -= 1
        last = horse[2]
        answer.append(last)
        horses = sorted(horses, reverse=True)

    print('Case #{}: {}'.format(case, ''.join(answer)))
