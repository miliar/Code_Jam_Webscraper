def is_tidy(n):
    if n < 10:
        return True

    m = n // 10
    return (m % 10) <= (n % 10) and is_tidy(m)


def last_nine(n):
    while n % 10 != 9:
        n -= 1
    return n


def last_tidy(n):
    if is_tidy(n):
        return n

    n = last_nine(n)
    return last_tidy(n // 10) * 10 + (n % 10)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        print('Case #{t}: {v}'.format(t=i+1, v=last_tidy(n)))
