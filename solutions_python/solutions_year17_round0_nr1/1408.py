import sys
sys.setrecursionlimit(1500)

def flip(array, K, current=0, total=0):

    while current < len(array) and array[current] > 0:
        current += 1

    if current == len(array):
        print('YES ', total, array)
        return total
    elif current + K > len(array):
        return 'IMPOSSIBLE'

    # print(array)
    for i in range(K):
        array[current + i] = array[current + i] == 0 and 1 or 0

    total += 1
    print(current, total, array)
    return flip(array, K, current, total)


def parse(fn):
    results = []
    f = open(fn)
    output = open(fn + '.output', 'w')
    # skip first line
    next(f)
    case = 1
    for line in f:
        print(line)
        array, K = line.split(' ')
        K = int(K)
        array = [(a == '+' and 1 or 0) for a in array]
        result = flip(array, K)
        print('Case #{}: {}'.format(case, result), file=output)
        case += 1
    f.close()
    output.close()

parse('A-large.in')