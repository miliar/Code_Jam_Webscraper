

t = int(input())

for i in range(1, t + 1):
    # read input
    pancakes, k = input().split(" ")
    pancakes = [c=="+" for c in pancakes]
    k = int(k)

    cond = True
    index = 0
    flips = 0
    impossible = False
    while cond:
        # print (pancakes)
        if index >= len(pancakes):
            break
        if not pancakes[index]:
            # print(pancakes, index, pancakes[index])
            if index + k > len(pancakes):
                impossible = True
                break
            flips = flips + 1
            for j in range(index, index + k):
                pancakes[j] = not pancakes[j]
        index = index + 1

    output = "IMPOSSIBLE" if impossible else str(flips)

    print("Case #{}: {}".format(i, output))
    # check format
