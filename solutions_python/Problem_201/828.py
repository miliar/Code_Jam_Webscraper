t = int(input())  # read a line with a single integer


def lookup_num(l, num):
    for i, (n, m) in enumerate(l):
        if n == num:
            return i
    return -1


def solve(n, m):
    spaces = [(n, 1)]

    while True:
        spaces.sort(reverse=True)
        num, count = spaces[0]
        large = num // 2
        small = (num - 1) // 2

        if count >= m:
            return large, small
        else:
            spaces = spaces[1:]
            i = lookup_num(spaces, small)
            if i != -1:
                _, temp_count = spaces[i]
                spaces[i] = (small, temp_count + count)
            else:
                spaces.append((small, count))

            i = lookup_num(spaces, large)
            if i != -1:
                _, temp_count = spaces[i]
                spaces[i] = (large, temp_count + count)
            else:
                spaces.append((large, count))

            m -= count


for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    high, low = solve(n, m)

    print("Case #{}: {} {}".format(i, high, low))
