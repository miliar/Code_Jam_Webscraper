#!/usr/bin/env python3

R = 1
Y = 2
B = 4
O = R | Y
G = Y | B
V = R | B

colors = [R, O, Y, G, B, V]

T = int(input())
for case in range(1, T + 1):
    num_color = dict()
    for c, n in zip(colors, input().split()[1:]):
        num_color[c] = int(n)
    if num_color[O] == num_color[G] == num_color[V] == 0:
        m = [(num_color[R], 'R'), (num_color[B], 'B'), (num_color[Y], 'Y')]
        m.sort()
        triple = m[0][0] + m[1][0] - m[2][0]
        if triple < 0:
            answer = 'IMPOSSIBLE'
        else:
            three = m[2][1] + m[1][1] + m[0][1]
            two1 = m[2][1] + m[1][1]
            two2 = m[2][1] + m[0][1]
            answer = three * triple + two1 * (m[1][0] - triple) + two2 * (m[2][0] - m[1][0])
    else:
        answer = 'TBA'
    print("Case #", case, ": ", answer, sep='')
