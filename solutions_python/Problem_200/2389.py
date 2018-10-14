def is_non_decreasing(n):
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            return False
    return True


def remove_leading_zeroes(n):
    while len(n) > 0 and n[0] == 0:
        n.pop(0)
    return n


def fix_first_non_decreasing(n):
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            index = i - 1
            break

    n[index] -= 1
    for i in range(len(n[index + 1:])):
        n[index + i + 1] = 9
    return remove_leading_zeroes(n)


def solve(n):
    while not is_non_decreasing(n):
        n = fix_first_non_decreasing(n)

    return ''.join([str(i) for i in n])


def main():
    t = int(input())
    case = 1
    while t > 0:
        n = list(map(int, list(input())))
        answer = solve(n)
        print('Case #{case}: {answer}'.format(case=case, answer=answer))
        case += 1
        t -= 1


main()
