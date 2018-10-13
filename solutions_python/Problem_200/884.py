file = "B-large.in"

def tidy_number(N):
    digits = str(N)

    if len(digits) == 1:
        return N

    split_index = 0
    while split_index < len(digits) - 1 and digits[split_index] <= digits[split_index + 1]:
        split_index += 1

    if split_index == len(digits) - 1:
        return N

    while split_index and digits[split_index] == digits[split_index - 1]:
        split_index -= 1

    return N - (int(digits[split_index + 1:]) + 1)

with open(file) as handle:
    T = int(handle.readline())

    for i in range(T):
        N = int(handle.readline())

        print 'Case #{}: {}'.format(i + 1, tidy_number(N))
