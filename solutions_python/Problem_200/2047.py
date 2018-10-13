
k = int(raw_input())

all_data = [raw_input() for i in range(k)]


def check(sub_num):
    if len(sub_num) == 1:
        return True
    l = len(sub_num)
    for i in range(1, len(sub_num)):
        if sub_num[l - i] < sub_num[l - i - 1]:
            return i
    return True


def has_bigger(n, sub_num):
    """
    :param n: int
    :param sub_num: str
    :return: bool
    """
    for i in sub_num:
        if int(i) > n:
            return True
    return False


def cal(number):
    if check(number) is True:
        return number
    r = 1
    l = len(number)
    while True:
        i = check(number)
        if not (i is True):
            if i < r:
                number = list(number)
                number[l-i] = '9'
                number = ''.join(number)
                continue
        else:
            break
        while has_bigger(int(number[l-r]), number[:l-r]):
            number = int(number)
            number -= 10**(r-1)
            number = str(number)
            l = len(number)
            if l == 1:
                return number
        r += 1

    return number

for i in range(k):
    r = cal(all_data[i])
    print 'Case #{0}: {1}'.format(i+1, r)
