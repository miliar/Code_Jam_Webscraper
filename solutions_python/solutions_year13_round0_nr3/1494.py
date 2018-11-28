import math

def next_pali(n):
    s = str(n)
    digits = len(s)

    if digits > 2 and s[0] > "2":
        return 10 ** (digits) + 1

    if s == "9" * digits:
        return n + 2

    if digits % 2 == 0:
        a = s[:digits / 2]
        a = str(int(a) + 1)
        return int(a + a[::-1])

    a = s[:digits / 2 + 1]
    a = str(int(a) + 1)
    return int(a + a[:-1][::-1])


def is_pali(n):
    s = str(n)
    digits = len(s)
    a = s[:digits / 2]
    b = s[::-1][:digits / 2]
    return a == b


def find_pali(n):

    if is_pali(n):
        return n

    s = str(n)
    digits = len(s)

    if digits % 2 == 0:
        a = s[:digits / 2]
        p = int(a + a[::-1])
    else:
        a = s[:digits / 2 + 1]
        p = int(a + a[:-1][::-1])

    if n < p:
        return p

    return next_pali(p)


def iter_pali(a, b):
    i = find_pali(a)
    while i <= b:
        yield i
        i = next_pali(i)


def iter_sq_pali(a, b):
    for i in iter_pali(a, b):
        if is_pali(i ** 2):
            yield i


def count_sq_pali(a, b):
    n = 0
    for i in iter_sq_pali(a, b):
        n += 1
    return n


def count_sq_pali2(a2, b2):
    return count_sq_pali(int(math.ceil(math.sqrt(a2))), int(math.floor(math.sqrt(b2))))

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        a, b = map(int, raw_input().split(" "))
        print "Case #%d: %d" % (i+1, count_sq_pali2(a, b))