from pip._vendor.distlib.compat import raw_input


def check(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def tidy(n):
    if len(n) == 1:
        return n
    l = [int(x) for x in n]
    i = len(l) - 1
    while i > 0:
        if check(l):
            break
        else:
            l[i] = 9
            l[i - 1] -= 1
        i -= 1
    l = [str(x) for x in l]
    n = int(''.join(l))
    return n


if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t + 1):
        data = raw_input()
        count = tidy(data)
        print("Case #{}: {}".format(i, count))
