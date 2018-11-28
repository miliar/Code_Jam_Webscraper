#! /usr/bin/env python3

UP = '+'
DOWN = '-'
NOWAY = 'IMPOSSIBLE'


def is_tidy(num):
    for digit, following in zip(num, num[1:]):
        if digit > following:
            return False
    return True


def largest_tidy(n):
    number_len = len(n)
    for i in range(number_len-1, -1, -1):
        # print(n[i:])
        # print(i)
        if not is_tidy(n[i:]):
            new_n = n[:i] + str(int(n[i])-1) + '9' * (number_len-i-1)
            # print("NEW", new_n)
            new_n = new_n.lstrip('0')
            return largest_tidy(new_n)
    return n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print("Case #{}: {}".format(i + 1, largest_tidy(n)))
