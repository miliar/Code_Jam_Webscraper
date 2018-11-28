from sys import argv

def tidy_number(number):

    num = list(reversed(list(map(int, str(number)))))
    tidy_num = []

    # fix this
    if len(num) == 1:
        return number
    else:
        if num[0] < num[1]:
            tidy_num = [9] + [num[1]-1]
        else:
            tidy_num = [num[0], num[1]]

        for i in range(2, len(num)):
            if tidy_num[i-1] < num[i]:
                tidy_num = [9]*i + [num[i]-1]
            else:
                tidy_num += [num[i]]
    return int("".join(map(str, reversed(tidy_num))))

def write_cases(func, filename):
    with open(filename) as fi, open(filename.split(".")[0] + ".out", "w") as fo:
        for i in range(1, int(fi.readline().strip())+1):
            line = func(int(fi.readline().strip()))
            print("Case #{}: {}".format(i, line), file=fo)

def print_cases(func, filename):
    with open(filename) as fi:
        for i in range(1, int(fi.readline().strip())+1):
            line = fi.readline().strip()
            print("{} -> {}".format(line, func(int(line))))

if __name__ == "__main__":
    write_cases(tidy_number, argv[1])

