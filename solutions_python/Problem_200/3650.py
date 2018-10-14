def get_sorted_index(n):
    # starting from the ending index, get up to which substring is sorted
    # Returns i: if i is 0, the whole string is sorted
    prev_n = None
    for i, c in enumerate(reversed(n)):
        if prev_n is None:
            prev_n = c
        elif c > prev_n:
            return len(n) - i
        else:
            prev_n = c
    return 0


def get_tidy_number(n):
    n = list(n)
    index = get_sorted_index(n)
    while index != 0:
        before_index = index - 1
        n[before_index] = str(int(n[before_index]) - 1)
        for i in range(before_index + 1, len(n)):
            n[i] = '9'
        index = get_sorted_index(n)
    return int(''.join(n))


with open('B-large.in') as f:
    lines = f.read().split('\n')
    cases = int(lines[0])
    case_number = 1
    for x in lines[1:]:
        print("Case #%d: %d" % (case_number, get_tidy_number(x)))
        case_number += 1
