#!/usr/bin/env python2


def main():
    n = int(raw_input())
    for i in xrange(n):
        c = int(raw_input())
        result = twiddler(c)
        print 'Case #{0}: {1}'.format(i+1, result)


def twiddler(n):
    s = [int(i) for i in reversed(str(n))]
    carry = 0

    for i in xrange(len(s)-1):

        w = s[i]
        do_nines = False

        if carry:
            do_nines = True
            w -= 1

        carry = False

        if w < s[i+1]:
            s[i] = 9
            do_nines = True
            carry = True
        else:
            s[i] = w

        if do_nines:
            j = i-1
            for j in xrange(j, -1, -1):
                s[j] = 9

    s[-1] -= carry

    return int(''.join([str(i) for i in reversed(s)]))


if __name__ == '__main__':
    main()
