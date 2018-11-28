def get_tidy(n):
    untidy_index = get_first_untidy_index(n)
    if untidy_index == -1:
        return int(n)
    new_n = drop_index(n, untidy_index)
    return get_tidy(new_n)


def get_first_untidy_index(n):
    n_str = str(n)
    length = len(n_str)
    if length <= 1:
        return -1
    for index in range(length -1):
        digit = int(n_str[index])
        next_digit = int(n_str[index+1])
        if digit > next_digit:
            return index
    return -1


def drop_index(n, index):
    n_str = str(n)
    part1 = n_str[:index]
    part2 = str(int(n_str[index]) - 1)
    part3_length = len(n_str) - index - 1
    part3 = "".join(["9" for j in range(part3_length)])
    return part1 + part2 + part3


t = int(raw_input())
for i in xrange(1, t + 1):
    input_number = [int(s) for s in raw_input().split(" ")][0]
    output_number = str(get_tidy(input_number))
    print "Case #{}: {}".format(i, output_number)
