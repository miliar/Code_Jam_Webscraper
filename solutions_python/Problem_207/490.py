def calculate(n, count):
    independent = [
        [3, 2, 4],
        [4],
        [5, 0, 4],
        [0],
        [1, 0, 2],
        [2]
    ]
    colors = "ROYGBV"

    for i, x in enumerate(count):
        _sum = 0
        for y in independent[i]:
            _sum += count[y]
        if _sum < x:
            return "IMPOSSIBLE"

    i = 0
    while count[i] == 0:
        i += 1

    result = ""

    while True:
        if len(result) == (n-1):
            return result + colors[i]

        selected = None
        max_available = -1

        for j, x in enumerate(independent[i]):
            if count[x] > max_available:
                max_available = count[x]
                selected = x
                if j == 0 and count[x] != 0:
                    break

        result += colors[i]
        count[i] -= 1
        i = selected


t = int(input())
i = 0

while t:
    t -= 1
    i += 1

    temp = list(map(int, input().split()))

    n = temp[0]
    count = temp[1:]

    print("Case #{}: {}".format(i, calculate(n, count)))
