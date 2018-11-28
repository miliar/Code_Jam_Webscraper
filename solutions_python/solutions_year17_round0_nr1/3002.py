def flipper_simulator(pancake, k):
    counter = 0
    for i in range(len(pancake) - k + 1):
        if pancake[i] == "-":
            for j in range(k):
                if pancake[i + j] == '+':
                    pancake[i + j] = '-'
                else:
                    pancake[i + j] = '+'
            counter += 1
    for i in range(k):
        if pancake[len(pancake) - i - 1] == '-':
            return 'IMPOSSIBLE'
    return counter

t = int(input())
for i in range(1, t + 1):
    pancakeList = []
    pancakes, k = input().split(" ")
    for j in pancakes:
        pancakeList.append(j)
    k = int(k)
    print("Case #{}: {}".format(i, flipper_simulator(pancakeList, k)))
