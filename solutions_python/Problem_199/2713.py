for case in range(int(input())):

    a, b = input().split()
    pancakes = list(map(lambda ch: ch == "+", a))
    size = int(b)
    count = 0
    for i in range(len(pancakes) - size + 1):

        if not pancakes[i]:

            count += 1
            for j in range(i, i + size):

                pancakes[j] = not pancakes[j]

    print(str.format("Case #{}: ", case + 1), end="")
    if not all(pancakes):

        print("IMPOSSIBLE")

    else:

        print(count)
