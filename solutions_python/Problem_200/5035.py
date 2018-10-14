import sys


def sheep(n):
    found = [False] * 10
    if n == 0:
        print("INSOMNIA")
    else:
        cur = 0
        while found != [True] * 10:
            cur += n
            num = list(f"{cur}")
            for a in num:
                found[int(a)] = True
        print(cur)


def tidy(n):
    if n == 1:
        print(1)
        return

    def tidyN(k):
        last = None
        for b in str(k):
            if last is None or b >= last:
                last = b
            else:
                return False
        return True

    for a in range(0, n - 1):
        p = n - a
        if tidyN(p):
            print(p)
            break


filename = "test.in"
lines = open(filename).read().splitlines()
# print(lines)
n = int(lines[0])
i = 1
for _ in range(n):
    sys.stdout.write(f"Case #{i}: ")
    tidy(int(lines[i]))
    i += 1
