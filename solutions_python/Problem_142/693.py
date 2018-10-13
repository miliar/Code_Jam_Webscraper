def get_letters(strs, i):
    l1 = strs[0][i]
    l2 = None
    l1c, l2c = 0, 0
    for j in xrange(len(strs)):
        if i >= len(strs[j]):
            return None
        if strs[j][i] == l1:
            l1c += 1
            continue
        if l2 is None:
            l2 = strs[j][i]
        if strs[j][i] == l2:
            l2c += 1
            continue
    return [l1, l2]


def can_get(string, letter, i):
    if string[i] == letter:
        return 0
    if (i > 0) and (string[i - 1] == letter):
        return 1
    if (i == 0) or (string[i] != string[i - 1]):
        return None
    j = i + 1
    while string[j] == string[j - 1]:
        j += 1
    if string[j] == letter:
        return j - i
    else:
        return None


def get(string, letter, i):
    if string[i] == letter:
        return string
    if (i > 0) and (string[i - 1] == letter):
        return string[:i] + string[i - 1] + string[i:]
    j = i + 1
    while string[j] == string[j - 1]:
        j += 1
    return string[:i] + string[j:]


def are_equal(strs, i):
    for j in xrange(1, len(strs)):
        if strs[j - 1][i] != strs[j][i]:
            return False
    return True

def solve(test_number):
    str_num = int(raw_input())
    strs = list()
    for i in xrange(str_num):
        strs.append(raw_input() + '@')
    i = 0
    res = 0
    while True:
        if i >= len(strs[0]):
            break
        if are_equal(strs, i):
            i += 1
            continue
        letters = get_letters(strs, i)
        if letters is None:
            print 'Case #%d: Fegla Won' % test_number
            return
        minl = None
        minlc = 1000000000
        for letter in letters:
            m = 0
            for string in strs:
                c = can_get(string, letter, i)
                if c is None:
                    m = None
                    break
                m += c
            if m is not None:
                if (minlc > m):
                    minlc = m
                    minl = letter
        if minl is None:
            print 'Case #%d: Fegla Won' % test_number
            return
        for x in xrange(len(strs)):
            strs[x] = get(strs[x], minl, i)
        res += minlc
    print 'Case #%d: %d' % (test_number, res)


def main():
    test_count = int(raw_input())
    for test_number in xrange(1, test_count + 1):
        solve(test_number)


if __name__ == '__main__':
    main()