import sys

def reverse(pancake):
    if pancake == '+':
        return '-'
    else:
        return '+'


def flip(pancake, times):
    if times % 2 == 1:
        return reverse(pancake)
    else:
        return pancake


def flips_number(pancakes, size):
    flips = set()
    count = 0
    for i in range(len(pancakes)):
        pancake = pancakes[i]
        if flip(pancake, len(flips)) == '-':
            flips.add(i)
            count += 1

        if i + 1 - size in flips:
            flips.remove(i + 1 - size)

    if len(flips) == 0:
        return count
    else:
        return 'IMPOSSIBLE'

file_name = sys.argv[1]
with open(file_name) as file:
    T = int(file.readline())
    for x in range(T):
        pancakes, size = file.readline().split(' ')
        print('Case #{}: {}'.format(x+1, flips_number(pancakes, int(size))))