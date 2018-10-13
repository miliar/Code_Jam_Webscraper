def flip(cakes, width, index):
    for i in range(index, index + width):
        cakes[i] = "-" if cakes[i] == "+" else "+"


def is_happy(cakes):
    return all(map(lambda x: x == "+", cakes))


def flips(pancakes, width):
    cakes = list(pancakes)
    flip_count = 0
    for i in range(len(cakes) - width + 1):
        if cakes[i] == "-":
            flip_count += 1
            flip(cakes, width, i)
            # print("".join(cakes))

    return str(flip_count) if is_happy(cakes) else "IMPOSSIBLE"


# import random
#
# test_cakes = [random.choice("+-") for i in range(1000)]
#
# print(test_cakes)
#
# print(flips(test_cakes, 3))
# print(flips("+++++", 4))
# print(flips("+-+-+", 4))

# INPUT = "TestInput"
# OUTPUT = "TestOutput"

# INPUT = "SmallInput"
# OUTPUT = "SmallOutput"


INPUT = "LargeInput"
OUTPUT = "LargeOutput"

with open(INPUT, "r") as input_file:
    with open(OUTPUT, "w") as output_file:
        output_file.truncate()

        t = int(input_file.readline())
        for i in range(t):
            cakes, width = input_file.readline().split()
            width = int(width)

            output_file.write(f"Case #{i+1}: {flips(cakes, width)}\n")
