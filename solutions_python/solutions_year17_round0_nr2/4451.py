import fileinput


def answer_prod():
    t = int(input())  # read a line with a single integer
    inputf = []
    for i in range(1, t + 1):

        n = str(input()).strip()  # read a list of integers, 2 in this case
        inputf.append(n)
        # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
    return inputf


def answer_dev():
    fi = fileinput.input("B-small-attempt0.in.txt")
    t = int(fi.readline())  # read a line with a single integer
    inputf = []
    for i in range(1, t + 1):
        ss = fi.readline()
        # n, m = [s for s in ss.strip().split(' ')]  # read a list of integers, 2 in this case
        n = ss.strip()  # read a list of integers, 2 in this case
        inputf.append(n)
        # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
    fileinput.close()
    return inputf

# for debuging in IDE set to answer_dev()
inp = answer_prod()
# inp = answer_dev()


def isTidy(array):
    for i in range(len(array)-1):
        if int(array[i])>int(array[i+1]):
            return False
    return True


def answer(number):
    s = list(str(number))
    max_index = len(s)-1
    max_value = s[max_index]
    decer = 9
    # print(number)
    tmp = len(s)
    prev_max_index = max_index
    while max_index == len(s)-1:
        tmp -= 1
        max_index = tmp
        max_value = s[max_index]
        for key in range(tmp):
            if int(s[key]) > int(max_value):
                max_value = s[key]
                max_index = key


    while not isTidy(s):
        # print(s)
        # find max
        for key in range(len(s)-(len(s)-max_index-1)):
            if int(s[key]) > int(max_value):
                max_value = s[key]
                max_index = key

        # fill everything after max(until previous max ) by 9's when found for the first time ,
        # for the second by  8's, 3rd by 7's etc.
        for j in range(max_index + 1, (len(s) - (len(s) - prev_max_index-1))):
            s[j] = str(decer)
        decer -= 1

        # correct max index if there is no max for max - 1
        if max_index != prev_max_index:
            s[max_index] = str(int(s[max_index]) - 1)
        prev_max_index = max_index - 1
        max_index = max_index - 1
        if max_index < 0:
            max_index = 0
        # print(max_index)
        max_value = s[max_index]
        # find new max
        for key in range(len(s) - (len(s) - max_index - 1)):
            if int(s[key]) > int(max_value):
                max_value = s[key]
                max_index = key
    res = ""
    # to remove 0's in front if there is any
    return str(int(res.join(s)))

# print(answer(627))
for test in range(len(inp)):
    print("Case #{}: {}".format(test + 1, answer(inp[test])))
