import sys


def print_case(n, solution):
    print("Case #{}: {}".format(n, solution))


def is_tidy(number):
    str_num = str(number)
    for i in reversed(range(1, len(str_num))):
        if str_num[i] < str_num[i-1]:
            return False
    return True

def last_tidy_number(N):
    while not is_tidy(N):
        N -= 1

    return N

def first_come_down(N):
    str_num = str(N)
    for i in range(len(str_num)-1):
        if str_num[i] > str_num[i+1]:
            return i+1
    return -1


def subtract_rightmost(N, index):
    to_subtract = int(str(N)[index:])
    return N - to_subtract - 1

def last_tidy_number_optimized(N):
    while not is_tidy(N):
        i = first_come_down(N)
        if i > -1:
            N = subtract_rightmost(N, i)
        else:
            N -= 1

    return N

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    T = int(lines[0])


    i = 1
    while i <= T:
        N = int(lines[i])

        # print(subtract_rightmost(43111, 1))
        # print( first_come_down(N))
        print_case(i, last_tidy_number_optimized(N))
        i += 1
