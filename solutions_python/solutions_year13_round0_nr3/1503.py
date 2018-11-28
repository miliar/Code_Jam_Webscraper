#!/usr/bin/python
import gmpy


def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


def do_calc(xfrom, xto):
    count = 0
    for i in range(xfrom, xto + 1):
        if is_palindrome(str(i)):
            if gmpy.is_square(i):
                if is_palindrome(str(gmpy.sqrt(i))):
                    count += 1
    return count

fromlist = []
tolist = []
first = True
T = 0
for line in open('inp', 'r'):
    line = line.strip()
    if first:
        T = int(line)
        first = False
        continue
    xfrom, xto = line.split()
    fromlist.append(int(xfrom))
    tolist.append(int(xto))

res = []
for i in range(0, T):
    res.append(do_calc(fromlist[i], tolist[i]))

file = open('out', 'w')
for i in range(0, T):
    file.write('Case #' + str(i + 1) + ': ' + str(res[i]) + '\n')
