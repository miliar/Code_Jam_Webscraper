#! /usr/bin/env python3
# 2017 - Qualification
import fileinput


def is_tidy(n):
    last = 0
    for x in [int(c) for c in str(n)]:
        if x < last:
            return False
        last = x
    return True


def last_tidy(n):
    if is_tidy(n):
        return n
    s = str(n)
    for i in range(len(s)):
        if not is_tidy(int(s[:i + 1])):
            break
    left = str(int(s[:i]) - 1)
    pad = len(s) - i
    result = int(left + '9' * pad)
    return last_tidy(result)



def main(reader=fileinput.input()):
    t = int(reader.readline())
    for i in range(t):
        n = int(reader.readline())
        result = last_tidy(n)
        print('Case #{}: {}'.format(i + 1, result))


if __name__ == '__main__':
    main()
