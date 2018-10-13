
import itertools


def largest_tidy_num(s):
    s = [int(c) for c in s]
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            # runs of same value
            while i > 0 and s[i-1] == s[i]:
                i -= 1
            s[i+1:] = itertools.repeat(9, len(s) - i - 1)
            s[i] -= 1

    if s[0] == 0:
        s = s[1:]
    return ''.join(str(c) for c in s)


def main():
    T = int(input())
    for t in range(1, T+1):
        s = input()
        print("Case #%i: %s" % (t, largest_tidy_num(s)))


if __name__ == '__main__':
    main()
