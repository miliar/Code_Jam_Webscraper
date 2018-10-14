from sys import argv

script, filename = argv

f = open(filename)

T = int(f.readline())


def comb(n, m):
    """
    :param n: total number
    :param m: max number of 1
    """
    if n <= m:
        return 2 ** n
    res = 1  # all zeroes
    res1 = 1  # nums with one 1
    for j in range(m):
        res1 = res1 * (n - j) / (j + 1)
        res = res + res1
    return res


def num(reg):
    if reg == 1:
        return 3
    elif reg == 2:
        return 2
    elif reg == 3:
        return 5
    elif reg % 2 == 0:
        res = 1  # 2...2
        n = (reg / 2) - 1
        res = res + comb(n, 4)
    else:
        res = 2  # 2..0..2 and 2..1..2
        n = ((reg - 1) / 2) - 1
        #case with 2 in middle
        res = res + comb(n, 1)
        #case with 0 or 1 in middle
        res = res + 2 * comb(n, 4)
    return res


def more(str1):
    if len(str1) == 1:
        ar = ['1', '2', '3']
    elif len(str1) == 2:
        ar = ['11', '22']
    elif len(str1) == 3:
        ar = ['101', '111', '121', '202', '212']
    if len(str1) < 4:
        return len(filter(lambda x: cmp(x, str1) == 1, ar))

    if len(str1) % 2 == 0:
        if str1[0] == '2':
            return 0
        else:
            n = len(str1) / 2
            ones = 0
            lastOne = 0
            for i in range(n):
                if str1[i] == '1':
                    ones = ones + 1
                    lastOne = i
            return max(0, comb(n - lastOne - 1,
                               4 - ones) - 1)  # 1 for all zeros
    else:
        if str1[0] == '2':
            if str1[len(str1) / 2] == '0':
                return 1
            else:
                return 0
        else:
            if str1[len(str1) / 2] == '1':
                return 1
            elif str1[len(str1) / 2] == '2':
                return 0
            n = len(str1) / 2
            ones = 0
            lastOne = 0
            for i in range(n):
                if str1[i] == '1':
                    ones = ones + 1
                    lastOne = i
            res = 2 * comb(n - lastOne - 1, 4 - ones)
            if ones == 1:
                res += comb(n - lastOne - 1, 1)
            return max(0, res)


def sum(str1, str2):
    s1 = str1[::-1]
    s2 = str2[::-1]
    s = []
    for i in range(max(len(s1), len(s2))):
        if len(s1) <= i:
            s.append(s2[i])
        else:
            s.append(str(int(s1[i]) + int(s2[i])))
    return ''.join(s[::-1])


def power2(str1):
    if str1 == '3':
        return '9'
    s = '0'
    for i in range(len(str1)):
        if str1[i] == '1':
            s = sum(s, str1 + '0' * i)
        if str1[i] == '2':
            s = sum(s, sum(str1 + '0' * i, str1 + '0' * i))
    return s


def check(x, y):
    if len(x) == len(y):
        return more(x) - more(y)

    res = 0
    for i in range(len(x) + 1, len(y)):
        res += num(i)

    res = res + more(x)
    res = res + num(len(y)) - more(y)

    return res


def cmp(x, y):
    """
    Compare two string
    """
    if len(x) > len(y):
        return 1
    elif len(x) < len(y):
        return -1
    elif x == y:
        return 0
    elif x > y:
        return 1
    else:
        return -1


def repl(st, pos, char):
    s = list(st)
    s[pos] = char
    return ''.join(s)


def findMax(str1):
    s = '1'
    while cmp(power2(s + '1'), str1) < 1:
        s += '0'

    if len(s) == 1:
        if cmp('9', str1) < 1:
            return '3'
        elif cmp('4', str1) < 1:
            return '2'
        return '1'

    s = repl(s, -1, '1')
    s2 = s[:]
    s2 = repl(s2, 0, '2')
    s2 = repl(s2, -1, '2')
    if cmp(power2(s2), str1) < 1:
        if len(s2) % 2 == 1:
            s3 = repl(s2, len(s2) / 2, '1')
            if cmp(power2(s3), str1) < 1:
                return s3
        return s2

    def inside(s, start, finish):
        if start >= finish:
            return s
        else:
            for i in range(start, finish):
                s2 = s[:]
                s2 = repl(s2, i, '1')
                s2 = repl(s2, -1 - i, '1')
                if cmp(power2(s2), str1) < 0:
                    return inside(s2, i + 1, finish)
            return s

    s2 = inside(s, 1, len(s) / 2)
    if cmp(power2(s2), str1) < 1:
        if len(s2) % 2 == 1:
            s3 = repl(s2, len(s2) / 2, '1')
            if cmp(power2(s3), str1) < 1:
                s4 = repl(s2, len(s2) / 2, '2')
                if cmp(power2(s4), str1) < 1:
                    return s4
                return s3
    return s2


for t in range(T):
    (x, y) = map(str, f.readline().split())

    x1 = findMax(x)
    y1 = findMax(y)
    res = check(x1, y1)
    if cmp(power2(x1), x) == 0:
        res = res + 1

    a = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944]

    x2, y2 = int(x), int(y)
    b = filter(lambda i: a[i] >= x2 and a[i] <= y2, range(len(a)))

    if len(b) != res:
        print x, y, x1, y1, power2(x1), len(b)

    print 'Case #{0}: {1}'.format(t + 1, res)


f.close()
