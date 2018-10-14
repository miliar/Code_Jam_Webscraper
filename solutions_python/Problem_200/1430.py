
def issorted(n):
    next_digit = n % 10
    n = n // 10
    while (n):
        digit = n % 10
        if digit > next_digit:
            return False
        next_digit = digit
        n = n // 10
    return True


if __name__ == '__main__':
    with open("/Users/bre50421/Downloads/B-small-attempt0.in") as fd:
        t = int(fd.readline())
        for i in range(1, t + 1):
            m = fd.readline().strip()
            if ''.join(sorted(m)) == m:
                print("Case #{}: {}".format(i, m))
            else:
                num = int(m)
                tmp_num = num
                p = 1
                while num:
                    last_digit = (tmp_num % 10 + 1) * p
                    num = num - last_digit
                    p = p * 10
                    tmp_num = num // p

                    if issorted(num):
                        print("Case #{}: {}".format(i, num))
                        break
