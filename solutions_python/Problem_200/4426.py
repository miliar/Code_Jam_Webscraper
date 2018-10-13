def is_tidy(s):
    s = list(s)
    last = s[0]
    for i in s[1:]:
        if last > i:
            return False
        last = i
    return True


def last_tidy(n):
    while not is_tidy(n):
        n = str(int(n) - 1)
    return n


if __name__ == '__main__':
    t = int(input())
    for n in range(1, t+1):
        s = input()
        print('Case #{}: {}'.format(n, last_tidy(s)))
