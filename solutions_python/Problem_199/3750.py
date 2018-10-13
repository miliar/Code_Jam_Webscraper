import sys


n = int(sys.stdin.readline().strip())

for case in range(1, n+1):
    cake_string, flip_width = sys.stdin.readline().strip().split(' ')
    flip_width = int(flip_width)
    cakes_bool = [cake == '+' for cake in cake_string]
    cakes = sum(v<<i for i, v in enumerate(reversed(cakes_bool)))

    checker = 1
    for _ in range(len(cake_string)-1):
        checker <<= 1
        checker += 1

    #if not (cakes & (cakes + 1)) and cakes:
    if not (cakes ^ checker):
        print('Case #{}: 0'.format(case))
        continue

    flipper = 0
    for _ in range(flip_width):
        flipper = (flipper<<1) + 1

    flips = 0
    cur_bit = 1
    for x in range(len(cake_string) - flip_width + 1):
        if not (cakes & cur_bit):
            flips += 1
            cakes = cakes ^ flipper
        flipper <<= 1
        cur_bit <<= 1

    # if not (cakes & (cakes + 1)) and cakes:
    if not (cakes ^ checker):
        print('Case #{}: {}'.format(case, flips))
    else:
        print('Case #{}: IMPOSSIBLE'.format(case, flips))
