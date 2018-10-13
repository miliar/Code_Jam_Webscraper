t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    n = [c for c in input()]

    j = len(n) - 1
    while j > 0:
        if int(n[j]) < int(n[j - 1]) or int(n[j]) == 0:
            for k in range(j, len(n)):
                n[k] = '9'
            n[j - 1] = str(int(n[j - 1]) - 1)
            j = len(n) - 1
        else:
            j -= 1

    if n[0] == '0':
        n = n[1:]
    result = ''.join(n)

    print("Case #{}: {}".format(i, result))
