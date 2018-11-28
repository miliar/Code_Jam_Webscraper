import sys


def pancake_flips(pancakes, k):
    flips = 0
    for i, pan in enumerate(pancakes):
        if pan == '-':
            if i > len(pancakes)-k:
                return "IMPOSSIBLE"
            else:
                # print("Before flip at {0}".format(i))
                # print(pancakes)
                flips = flips + 1
                for j in range(i, i+k):
                    pancakes[j] = '+' if pancakes[j] == '-' else '-'
                # print("After flip")
                # print(pancakes)
    return flips


if __name__ == "__main__":
    name = "A-large"
    f = open("{0}.in".format(name))
    output = open("{0}.out".format(name), "w")
    cases = int(f.readline())
    for i in range(cases):
        split = f.readline().split()
        # print(split)
        pancakes = list(split[0])
        k = int(split[1])
        output.write("Case #" + str(i + 1) + ": " + str(pancake_flips(pancakes, k)) + "\n")
    f.close()
    output.close()
