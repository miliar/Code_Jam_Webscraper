
def is_tiny(number):
    for i in range(len(number) - 1):
        if (number[i] > number[i + 1]):
            return False
    return True


def make_tiny(number):
    for i in range(len(number) - 1):
        if (number[i] > number[i + 1]):
            for j in range(len(number) - i - 1):
                # print("# i: {0}, ch: {1} in {2} ".format(
                #     i, i + 1 + j, "".join(number)))
                number[i + 1 + j] = "9"
            if i > 0 or int(number[i]) > 1:
                number[i] = str(int(number[i]) - 1)
            else:
                number = number[1:]
            return number


with open("B-large.in") as f:
    TESTS = int(f.readline())
    for test in range(TESTS):
        numb = list(f.readline().strip())

        while not is_tiny(numb):
            numb = make_tiny(numb)

        print("Case #{0}: {1}".format(test + 1, "".join(numb)))
