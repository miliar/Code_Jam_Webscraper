tests = int(input())

for z in range(tests):
    N, K = [int(x) for x in input().split()]
    last = 0
    openSpaces = {N: 1}
    for i in range(K):
        largest = max(openSpaces, key=int)
        openSpaces[largest] -= 1
        if openSpaces[largest] is 0:
            openSpaces.pop(largest)
        if largest % 2 is 0:
            val1 = largest // 2 - 1
            val2 = largest - val1 - 1
        elif largest is 1:
            val1 = 0
            val2 = 0
        else:
            val1 = largest // 2
            val2 = val1
        if not val1 in openSpaces:
            openSpaces[val1] = 0
        if not val2 in openSpaces:
            openSpaces[val2] = 0
        openSpaces[val1] += 1
        openSpaces[val2] += 1
        if i == K-1:
            print("Case #{}: {} {}".format(z+1, max(val1, val2), min(val1, val2)))

