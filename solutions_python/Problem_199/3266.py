cases = int(input())


def is_down(char):
    return char == '-'


def flip(char):
    if is_down(char):
        return '+'
    else:
        return '-'


for case in range(0, cases):
    cake_array, flip_length = input().split(' ')
    cake_array = list(cake_array)
    flip_length = int(flip_length)
    flips = 0

    for cake in range(0, len(cake_array)):
        if is_down(cake_array[cake]):
            if cake + flip_length > len(cake_array):
                flips = 'IMPOSSIBLE'
                break
            else:
                for flip_cake in range(cake, cake + flip_length):
                    cake_array[flip_cake] = flip(cake_array[flip_cake])
                flips += 1
    print('Case #{}: {}'.format(case + 1, flips))





