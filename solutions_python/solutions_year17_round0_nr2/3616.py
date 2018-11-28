

def _convert_list_to_integer(list_n):
    result = 0
    for i in range(0, len(list_n)):
        result += list_n.pop() * 10**i
    return result


def _convert_to_list(n):
    str_n = str(n)
    list_str_n = list(str_n)
    list_n = [int(i) for i in list_str_n]
    return list_n


def _flip_the_rest_of_the_digits(i, length, list_n):
    for j in range(i, length):
        list_n[j] = 9


def _adjust_numbers(i, list_n):
    list_n[i] -= 1
    if i == 0:
        return i
    if list_n[i-1] > list_n[i]:
        return _adjust_numbers(i-1, list_n)
    return i


def find_last_tidy_number_improved(n):
    list_n = _convert_to_list(n)
    length = len(list_n)
    for i in range(0, length-1):
        if list_n[i] <= list_n[i+1]:
            continue
        else:
            i = _adjust_numbers(i, list_n)
            _flip_the_rest_of_the_digits(i+1, length, list_n)
            break
    return _convert_list_to_integer(list_n)

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    result = find_last_tidy_number_improved(n)
    print("Case #{}: {}".format(i, result))
