import decimal

DEBUG = False

def printd(s):
    if DEBUG:
        print(s)

def solve(x):
    out = x
    n = getditycount(x)
    if len(str(x)) != n:
        while True:
            out = getcandidate(out)
            printd("out:{}".format(out))
            if istidy(out):
                break
    return out


def getcandidate(n):
    c = getditycount(n)
    k = len(str(n)) - c
    return int(decimal.Decimal(n) / decimal.Decimal(10 ** k)) * 10 ** k - 1


def getditycount(n):
    s = str(n)
    count = 1
    for i in range(len(s) - 1):
        if s[i] <= s[i + 1]:
            count += 1
        else:
            break
    return count


def istidy(n):
    s = str(n)
    for i in range(len(s) - 1, 0, -1):
        if int(s[i]) < int(s[i - 1]):
            return False
    return True


def main():
    n = int(input())
    for i in range(1, n + 1):
        x = int(input())
        out = solve(x)
        print("Case #{}: {}".format(i, out))

if __name__ == "__main__":
    main()
