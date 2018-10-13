n = int(input())
for i in range(n):
    s = input()
    a = list(map(int, s))
    size = len(a)
    j = 0

    while j < size - 1:
        if a[j] <= a[j + 1]:
            j += 1
        else:
            break

    if j >= size - 1:
        print("Case #{}: {}".format(i + 1, "".join([str(x) for x in a])))
        continue
    while j > 0:
        a[j] -= 1
        if a[j - 1] > a[j]:
            j -= 1
        else:
            res = "".join([str(x) for x in a[:j + 1]])
            res += "9" * (size - j - 1)
            print("Case #{}: {}".format(i + 1, "".join(res)))
            break
    if j == 0:
        if a[j] == 0:
            print("Case #{}: {}".format(i + 1, "9" * (size - 1)))
        else:
            s = str(a[j] - 1) if a[j] > 1 else ""
            print("Case #{}: {}".format(i + 1, s + "9" * (size - j - 1)))
