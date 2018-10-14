def inp():
    cases = []
    t = int(input())
    for i in range(t):
        num = input()
        array = [int(digit) for digit in num]
        cases.append(array)
    return cases


def process(a):
    """
    :param a: Array of digits of a number
    :return: Largest smaller tidy number
    """
    # print("Case:" + str(a))
    n = len(a)
    cutoff = 0
    for i in range(1, n):
        if a[n - i] < a[n - i - 1]:
            a[n - i - 1] -= 1
            cutoff = i
        # print(a)
    s = ''.join(str(i) for i in a[:n - cutoff]).lstrip("0")
    return s + ('9' * cutoff)


def main():
    cases = inp()
    for i in range(len(cases)):
        print("Case #{}: {}".format(i+1, process(cases[i])))


if __name__ == '__main__':
    main()
