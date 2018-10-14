import fileinput

f = fileinput.input()
T = int(f.readline())

for case in range(T):

    num = f.readline().strip()

    prev = 0
    upper = [0]

    j = 0

    while j < len(num):
        d = int(num[j])
        if d < prev:
            break
        prev = d
        upper.append(d)
        j += 1

    while j < len(num):
        upper.append(prev)
        j += 1

    out = ''.join(map(str, upper)).lstrip('0')
    out = out or '0'

    if out != num:

        n = len(upper)

        prev = None

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                prev = upper[i]
                continue
            if upper[i] != prev:
                upper[i + 1] -= 1
                for k in range(i + 2, n):
                    upper[k] = 9
                break
            prev = upper[i]

        out = ''.join(map(str, upper)).lstrip('0')

    print("Case #" + str(case + 1) + ":", out)
