def seek_out_unhappiness(pancakes, start, delta):
    i = start
    while 0 <= i < len(pancakes) and pancakes[i] == '+':
        i += delta
    return i

def im_flipping_out(pancakes, flip_size):
    L = len(pancakes)
    required_flips = 0

    # Seek first unhappy pancakes
    left = seek_out_unhappiness(pancakes, 0, 1)
    right = seek_out_unhappiness(pancakes, L-1, -1)

    # Work from the outside in
    while left+flip_size-1 <= right:
        if L-1-right <= left:
            right = flip_pancakes(pancakes, right, flip_size, -1)
        else:
            left = flip_pancakes(pancakes, left, flip_size, 1)
        required_flips += 1

    if right == -1 or left == L:
        return required_flips
    else:
        return -1

def flip_pancakes(pancakes, start, flip_size, delta):
    i = start
    remaining = flip_size
    flip = lambda p : '-' if p == '+' else '+'
    last_unhappy_seen = None 

    while remaining > 0 and 0 <= i < len(pancakes):
        pancakes[i] = flip(pancakes[i])
        if pancakes[i] == '-' and last_unhappy_seen is None:
            last_unhappy_seen = i
        remaining -= 1
        i += delta

    if not last_unhappy_seen:
        return seek_out_unhappiness(pancakes, i, delta)

    return last_unhappy_seen 

T = int(input())
for t in range(1, T+1):
    pancakes, flip_size = input().split(' ')
    required_flips = im_flipping_out(list(pancakes), int(flip_size))
    if required_flips < 0:
        required_flips = 'IMPOSSIBLE'
    print('Case #', t, ':', ' ', required_flips, sep='')

