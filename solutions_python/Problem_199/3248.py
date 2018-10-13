def flip(pancakes):

    flipped = ['-' if pancake == '+' else '+' for pancake in pancakes]

    return flipped

t = int(input())

for test_case in range(1, t+1):

    pancake, k = input().strip().split()
    k = int(k)
    pancake = list(pancake)

    no_flips = 0


    for i, char in enumerate(pancake):

        if i < len(pancake) - k + 1:
            if char == '-':
                pancake[i:i + k] = flip(pancake[i:i+k])
                no_flips += 1


    if '-' in pancake:
        print("Case #{}: {}".format(test_case, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(test_case, no_flips))

