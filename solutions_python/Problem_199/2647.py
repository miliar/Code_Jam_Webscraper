

def solve(start, flipper_size):
    array = [True if c == '+' else False for c in start]
    count = 0
    try:
        for i in range(len(array)):

            if not array[i]:
                array = flip(array, i, flipper_size)
                count += 1
    except ValueError:
        return 'IMPOSSIBLE'

    return count


def flip(array, index, size):
    if (index + size) > len(array):
        raise ValueError()
    else:
        return array[:index] + [not x for x in array[index:index+size]] + array[index+size:]

