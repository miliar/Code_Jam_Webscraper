def is_tidy(num):
    """
    Check if a list is sorted
    :param num:
    :return:
    """
    num_str = str(num)
    length = len(num_str)
    for i in range(length - 1):
        first = int(num_str[i])
        second = int(num_str[i + 1])
        if first > second:
            return False
    return True


def decrease_num_pair(current_num, current_num_length, position):
    """
    Decrease the num pair at the given position
    :param current_num:
    :param position:
    :return:
    """
    # Get the position from the right
    realpos = current_num_length - position - 1
    subval = 10 ** realpos
    return current_num - subval


def last_tidy(num):
    """
    Returns the last tidy number counting up to the given number

    If already sorted return
    Subtract one from the first negative difference from the right,
    if a set of numbers then the leftmost number of the set,
    and append the rest of the number as 9s
    Examples:
    1000
    0999

    132
    129

    11110
    09999

    7
    7

    32111
    29999

    223311
    222999

    22033
    21999
    :param num:
    :return:
    """
    if is_tidy(num):
        return num
    current_num = num
    current_num_str = str(num)
    for i in range(0, len(current_num_str) - 1):
        left = int(current_num_str[i])
        right = int(current_num_str[i + 1])
        # Check if the current pair is valid
        if left > right:
            # If left is in a set, find the leftmost of the set
            set_index = i
            if set_index == 0:
                # Handle zero index
                head = int(current_num_str[set_index]) - 1
            else:
                left_in_set = int(current_num_str[set_index - 1])
                right_in_set = int(current_num_str[set_index])
                while left_in_set == right_in_set:
                    set_index -= 1
                    left_in_set = int(current_num_str[set_index - 1])
                    right_in_set = int(current_num_str[set_index])
                # Subtract one from the found index
                head = int(current_num_str[:(set_index + 1)]) - 1

            # Append 9s as the rest of the number
            num_to_append = len(current_num_str) - 1 - set_index
            final = str(head) + '9' * num_to_append
            return int(final)
    return current_num


if __name__ == '__main__':
    input_size = int(input())
    for i in range(1, input_size + 1):
        cur_num = int(input())
        try:
            print("Case #{}: {}".format(i, last_tidy(cur_num)))
        except:
            print('Case #{}: X{}'.format(i, str(cur_num)))
