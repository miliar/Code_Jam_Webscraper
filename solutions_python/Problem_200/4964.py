import fileinput


def is_tidy(rem, mod=9):
    # base case
    if (rem < 10) and (rem <= mod):
        return True
    if ((rem % 10) <= mod):
        return is_tidy(mod=(rem % 10), rem=(rem / 10))
    else:
        return False


def get_nearest_tidy(n):
    while not is_tidy(n):
        n-=1
    return n

def results():
    for case, stack in enumerate(lines, 1):
        print "Case #{case}: {flips}".format(case=case, flips=min(pancakes_happy(stack),
                                                                  pancakes_happy(stack[::-1]) + 1))


def main():
    # We don't need the first number
    input = [line.strip() for line in fileinput.input()][1:]

    for case, n in enumerate(input, 1):
        print "Case #{case}: {n}".format(case=case, n=get_nearest_tidy(int(n)))


if __name__ == '__main__':
    main()
