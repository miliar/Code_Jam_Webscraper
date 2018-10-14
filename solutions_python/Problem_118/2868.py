import re

fileout = 'output.txt'
filename = 'C-small-attempt0.in'

number_re = re.compile("\d+")


def load_file(filename):
    lines = [line.strip() for line in open(filename)]
    cases = int(lines[0])
    f = open(fileout, 'w')
    for i in range(1, cases + 1):
        small, large = re.findall(number_re, lines[i])
        small = int(small)
        large = int(large)
        c = i
        amount = find_fair(small, large)
        print 'Case #' + str(c) + ': ' + str(amount)
        f.writelines('Case #' + str(c) + ': ' + str(amount) + '\n')
    f.close()


def isPali(x):
    str_x = str(x)
    if str_x == str_x[::-1]:
        return True
    else:
        return False


def isPerfect(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1
        if ans*ans != x:
            return (False, ans)
        else:
            return (True, ans)
    else:
        return (False, None)


def find_fair(small, large):
    amount = 0
    for i in range(small, large + 1):
        if isPali(i):
            perfect = isPerfect(i)
            if perfect[0]:
                if isPali(perfect[1]):
                    amount += 1
    return amount


if __name__ == '__main__':
    load_file(filename)
