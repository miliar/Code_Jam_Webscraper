def process():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        digits = [int(i) for i in input()]
        tidy = get_largest_tidy(digits)
        print("Case #{}: {}".format(i, tidy))


def get_largest_tidy(digit_array):
    rev_arr = digit_array[::-1]
    max_idx = len(rev_arr)
    for i in range(1, max_idx):
        if rev_arr[i-1] < rev_arr[i]:
            k = i
            while rev_arr[k] == 0:
                k += 1
            rev_arr[i] -= 1
            backprop_nines(rev_arr, i)
    return int(''.join([str(d) for d in rev_arr[::-1]]))


def backprop_nines(digit_array, backprop_from):
    for i in range(0, backprop_from):
        digit_array[i] = 9


if __name__ == "__main__":
    process()
