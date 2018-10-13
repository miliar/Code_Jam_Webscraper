#!/usr/bin/python3

t = int(input())


def test(x, r, c):
    if x == 2 and (r * c) % 2 == 0:
        return True
    if (r * c) % x != 0:
        return False
    if x > max(r, c):
        return False
    if x >= 2 * min(r, c):
        return False

    return True


for test_num in range(t):
    x, r, c = [int(i) for i in input().split()]

    cond = test(x, r, c)

    #print(x, r, c, 'WORKS' if cond else 'NOT')
    print('Case #{}: {}'.format(test_num + 1,
                                'GABRIEL' if cond else 'RICHARD'))
