import sys

sys.setrecursionlimit(100000)


def solve(number):
    print (number)
    print (len(number))
    for i in number:
        print (i)


def get_last_tidy(original_number, number):
    length = len(number)
    if length == 1:
        return number

    is_tidy = True
    for i in range(0, length - 1):
        cur = length - i - 1;
        head = length - i - 2;
        # print ("cur:" + number[cur] + " < head: " + number[head])
        # print ("zero " + str(seq_zero))
        if number[cur] < number[head]:
            is_tidy = False
            number = str(int(str(int(number[0:cur]) - 1) + '9' * (i + 1)))

    if is_tidy:
        return number
    return get_last_tidy(original_number, str(number))


if __name__ == "__main__":
    import fileinput

    f = fileinput.input()
    T = int(f.readline())
    for case in range(1, T + 1):
        number = f.readline().strip()
        tidy_number = get_last_tidy(number, number)
        print("Case #{0}: {1}".format(case, tidy_number))
