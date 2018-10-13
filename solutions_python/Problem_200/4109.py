"""
B - Tidy numbers
"""


def is_tidy(x):
    """
    check if number is tidy
    :param x: number to check
    :return: true is tidy
    """
    result = True
    prev = 0
    for i, n in enumerate(str(x)):
        n = int(n)
        if n < prev:
            return False, i
        prev = n
    return result, None


def largest_tidy_number(n):
    tidy, index = is_tidy(n)
    while not tidy:
        output = []
        inp = str(n)
        for i in range(len(inp)):
            if i < index - 1:
                output.append(inp[i])
            elif i == index - 1:
                output.append(str(int(inp[i])-1))
            else:
                output.append('9')
        n = int(''.join(output))
        tidy, index = is_tidy(n)
    return n


def test_largest_tidy():
    numbers = {
        1: 1,
        10: 9,
        3324: 2999,
        2324: 2299,
        793: 789,
        786: 779,
        794: 789,
        342: 339,
        1000: 999,
        773: 699
    }
    for n in numbers:
        result = largest_tidy_number(n)
        print('{0}: {1}'.format(n, result))
        if result != numbers[n]:
            print('  should be {0}'.format(numbers[n]))


def test_tidy():
    numbers = [23, 3445, 9999, 87, 65, 1, 8, 3324]
    for n in numbers:
        print('{0}: {1}'.format(n, is_tidy(n)))

if __name__ == '__main__':
    # test_tidy()
    # test_largest_tidy()
    T = int(input())
    for i in range(T):
        n = int(input())
        res = largest_tidy_number(n)
        print('Case #{0}: {1}'.format(i+1, res))
