def testcase():
    tokens = input().split(" ")
    flipper_size = int(tokens[1])
    pancakes = [0 if n == '-' else 1 for n in tokens[0]]

    count = 0
    for i in range(len(pancakes) - flipper_size + 1):
        if pancakes[i] == 0:
            count += 1
            for j in range(flipper_size):
                pancakes[i + j] ^= 1

    return count if not 0 in set(pancakes) else "IMPOSSIBLE"

t = int(input())

for num in range(t):
    print("Case #{num}: {result}".format(num=num+1, result=testcase()))