import sys

sys.setrecursionlimit(12000)


def which_side(pancakes, flipper):
    if '-' in pancakes:
        leftminus = pancakes.index('-')
        rightminus = list(reversed(pancakes)).index('-')
        if leftminus == len(pancakes) - rightminus - 1:
            return -2
        elif rightminus < leftminus:
            return 1
        elif ((leftminus + flipper) > len(pancakes)) or (len(pancakes) - rightminus - flipper) < 0:
            return -2
        else:
            return -1
    else:
        return 0


def isodd(num):
    return num % 2 == 0


def reverse(pancake):
    if pancake == '+':
        return '-'
    elif pancake == '-':
        return '+'


def flip(side, flipper, pancakes):
    if side == -1:
        leftminus = pancakes.index('-')
        for i in range(leftminus, leftminus + flipper):
            pancakes[i] = reverse(pancakes[i])

    elif side == 1:
        rightminus = len(pancakes) - list(reversed(pancakes)).index('-')
        for i in range(rightminus - flipper, rightminus):
            pancakes[i] = reverse(pancakes[i])

    return pancakes


def solve(pancakes, flipper, step):
    if(step > 10000):
        return "IMPOSSIBLE"
    side = which_side(pancakes, flipper)
    if side == 0:
        return step
    elif side == -2:
        return "IMPOSSIBLE"
    else:
        pancakes = flip(side, flipper, pancakes)
        return solve(pancakes, flipper, step + 1)

with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as fw:
        c = int(f.readline())
        for i in range(c):
            pancakes, flipper = f.readline().split(' ')
            res = solve(list(pancakes), int(flipper), 0)
            fw.write("Case #{}: {}\n".format(i + 1, res))
