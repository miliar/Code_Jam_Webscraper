import sys
cases = int(input())
for case in range(1, cases + 1):
    diners = int(input())

    def best(a):
        a = sorted(a)
        last = a[-1]
        if last == 1:
            return 1
        b = map(lambda y: y-1, a)
        results = []
        limit = 4 if last == 9 else 3
        for i in range(2, limit):
            x = a[:]
            x[-1] = last - (last // i * (i - 1))
            x += [last // i] * (i - 1)
            results.append((i - 2) + best(x))
        results.append(best(b))
        return 1 + min(results)
    print("Case #{}: {}".format(case, best(map(int, input().split()))))