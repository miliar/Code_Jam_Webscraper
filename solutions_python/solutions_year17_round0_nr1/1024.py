__author__ = 'User'

pancakes = ""


def flip(pancakes, i, k):
    for j in range(i, i + k):
        pancakes[j] = "-" if pancakes[j] == "+" else "+"

def flip_pancakes(pancakes, k):
    pancakes = list(pancakes)
    flips = 0
    i = 0
    while i <= len(pancakes) - k:
        if pancakes[i] == "-":
            flip(pancakes, i, k)
            flips += 1
        i += 1

    if pancakes.count('-') > 0:
        return 'IMPOSSIBLE'
    return flips


with open("input.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            line, k = line.split(" ")
            x = flip_pancakes(line.strip(), int(k))
            write_file.write("Case #" + str(i) + ": " + str(x) + "\n")