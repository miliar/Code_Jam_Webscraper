def get_case(case):
    pancakes = case.split()[0]
    flipper_size = int(case.split()[1])
    min_flips = 0
    for i in range(len(pancakes) - flipper_size + 1):
        if pancakes[i] == '-':
            pancakes = flip_stack(pancakes, flipper_size, i)
            min_flips += 1
    if pancakes.find('-') == -1:
        return min_flips
    else:
        return 'IMPOSSIBLE'


def flip_stack(pancakes, flipper_size, n):
    return pancakes[:n] + ''.join([flip(pancake) for pancake in pancakes[n:n + flipper_size]]) + pancakes[(n + flipper_size):]


def flip(pancake):
    if pancake == '-':
        return '+'
    else:
        return '-'
