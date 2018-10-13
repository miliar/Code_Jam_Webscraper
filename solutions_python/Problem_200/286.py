import sys

file_name = "B-large-practice"
sys.stdin = open(file_name + ".in", "r")
sys.stdout = open(file_name + ".out", "w")
input_line = sys.stdin.readline


def is_tidy_num(n):
    digits = set(range(10))
    n_digits = [int(i) for i in str(n)]

    for i in range(len(n_digits)):
        if n_digits[i] in digits:
            subset = set(range(n_digits[i]))
            digits -= subset
            if i == len(n_digits) - 1:
                return True
        else:
            break
    return False


def get_tidy_num(n):
    if is_tidy_num(n):
        return n
    else:
        n_digits = [int(i) for i in str(n)]
        for i in range(len(n_digits)-1, -1, -1):
            n_digits[i] = 0
            num = int(''.join(map(str, n_digits))) - 1
            if is_tidy_num(num):
                return num


for case in range(1, int(input_line())+1):
    N = int(input_line())
    result = get_tidy_num(N)
    print("Case #{0}: {1}".format(case, result))



