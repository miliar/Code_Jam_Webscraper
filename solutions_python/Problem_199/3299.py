def flip_pancakes(pancakes):
    return ''.join('-' if p == '+' else '+' for p in pancakes)

def flip_pancake_counter(pancakes, f_size):
    c = 0
    while pancakes:
        pancakes = pancakes.strip('+')
        if 0 < len(pancakes) < f_size:
            return 'IMPOSSIBLE'
        if pancakes.startswith('-'):
            c += 1
            pancakes = flip_pancakes(pancakes[:f_size]) + pancakes[f_size:]
    return c

cases = int(input())
for case in range(1, cases+1):
    pancakes, f_size = input().split()
    f_size = int(f_size)
    print('Case #{}: {}'.format(case, flip_pancake_counter(pancakes, f_size)))
