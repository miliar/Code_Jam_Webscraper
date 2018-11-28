

def jump_to_next(num, index):

    if index < 0:
        return num

    keep = num[0:index - 1]
    fill_length = len(num) - index
    if fill_length < 0:
        fill_length = 0
    decrement = int(num[index - 1]) - 1
    if decrement < 0:
        decrement = 9

    return '{0}{1}{2}'.format(keep, decrement, ''.join(['9'] * fill_length))


def is_number_not_ascending(num):
    """
    Returns -1 if the number is ascending
    the index where it is wrong otherwise

    """
    faulty_index = -1
    last_value = 0
    for i, c in enumerate(num):
        current = int(c)
        if current < last_value:
            faulty_index = i
            break
        else:
            last_value = current

    if faulty_index == -1:
        return faulty_index

    return faulty_index

t = int(input())

for test in range(t):
    n = int(input())

    while n > 0:

        string_number = str(n)
        current_number_faulty_index = is_number_not_ascending(string_number)
        if current_number_faulty_index == -1:
            print('Case #{0}: {1}'.format(int(test + 1), string_number))
            break
        else:
            n = int(jump_to_next(string_number, current_number_faulty_index))




