# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import fileinput


def answer_prod():
    t = int(input())  # read a line with a single integer
    inputf = []
    for i in range(1, t + 1):

        n, m = [s for s in (str(input()).split(' '))]  # read a list of integers, 2 in this case
        inputf.append(tuple([n, m]))
        # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
    return inputf


def answer_dev():
    fi = fileinput.input("small_input.txt")
    t = int(fi.readline())  # read a line with a single integer
    inputf = []
    for i in range(1, t + 1):
        ss = fi.readline()
        n, m = [s for s in ss.strip().split(' ')]  # read a list of integers, 2 in this case
        inputf.append(tuple([n, m]))
        # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
    fileinput.close()
    return inputf


inp = answer_prod()


def flip(in_array, start, end):

    for i in range(start, end):
        if in_array[i] == '+':
            in_array[i] = '-'
        else:
            in_array[i] = '+'
    return in_array


# just starting flipping from the beginning
def answer(in_array_2, k):
    number_of_flips = 0
    for i in range(len(in_array_2) - int(k) + 1):
        if in_array_2[i] == '-':
            in_array_2 = flip(in_array_2, i, i + int(k))
            number_of_flips += 1

    ss = set(in_array_2)
    if '-' in ss:
        return "IMPOSSIBLE"
    else:
        return number_of_flips


for test in range(len(inp)):
    print("Case #{}: {}".format(test + 1, answer(list(inp[test][0]), inp[test][1])))
