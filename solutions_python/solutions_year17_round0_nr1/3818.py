count = 0
file_object = open("input.txt", "r")
for line in file_object:
    if count == 0:
        count += 1
        num_cases = int(line)
    elif count <= num_cases:
        pancakes, flipper = line.split(" ")
        pancakes = list(pancakes)
        flipper = int(flipper)
        flips = 0
        for pancake in range(0, len(pancakes)):
            if pancakes[pancake] != '+':
                if pancake + flipper > len(pancakes):
                    flips = "IMPOSSIBLE"
                    break
                for i in range(0, flipper):
                    pancakes[pancake + i] = '-' if pancakes[pancake + i] == '+' else '+'
                flips = flips + 1
        print("Case #{}: {}".format(count, flips))
        count += 1
