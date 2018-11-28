from math import sqrt

filename = 'C-small-attempt0'
f_in = open(filename + '.in')
f_out = open(filename + '.out', 'w')

count = int(f_in.readline())


def is_palindrome(num):
    num_str = str(num)
    l = len(num_str)

    if l % 2 == 0:
        check = l / 2
    else:
        check = (l - 1) / 2

    for i in xrange(check):
        if num_str[i] != num_str[l - 1 - i]:
            return False

    return True


def is_fs(num):
    if is_palindrome(num):
        root = sqrt(num)

        if root % 1 == 0 and is_palindrome(int(root)):
            return True

    return False


fs = {}

for case in xrange(count):
    start, end = map(int, f_in.readline().split(' '))
    total = 0

    for num in xrange(start, end + 1):
        if num not in fs:
            #print(num)
            fs[num] = is_fs(num)

        if fs[num]:
            total += 1

    f_out.write('Case #%d: %d\n' % (case + 1, total))

