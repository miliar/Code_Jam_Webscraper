import sys


def solver(smax, s, count, add):
    while len(s) > 0:
        shyness = smax - len(s) + 1
        diff = shyness - count
        if diff > 0:
            add += diff
            count += diff

        count += int(s[0])
        s = s[1:]

    return add


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    if argc < 2:
        file = 'InputTest.txt'
    else:
        file = argvs[1]

    f = open(file, 'r')

    # 先頭行はテストケースの数
    test_case_num = int(f.readline().strip())
    num = 0
    while num < test_case_num:
        num += 1
        value = f.readline().strip().split(' ')
        result = solver(int(value[0]), value[1], 0, 0)
        print('Case #{0}: {1}'.format(num, result))

    f.close()