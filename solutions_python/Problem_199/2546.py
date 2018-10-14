
def find_flips(pancakes, flipper_size):
    flips = 0
    for i in range(0, len(pancakes) - flipper_size + 1):
        if pancakes[i] == "-":
            for j in range(i, i + flipper_size):
                if pancakes[j] == "-":
                    pancakes[j] = "+"
                else:
                    pancakes[j] = "-"
            flips += 1

    all_happy = True
    for j in range(len(pancakes) - flipper_size, len(pancakes)):
        if pancakes[j] == "-":
            all_happy = False
            break

    if all_happy:
        return str(flips)
    else:
        return "IMPOSSIBLE"

case = "A-Big"
output = ""

with open(case + ".in", "r") as fh:
    t = int(fh.readline().strip())
    for x in range(0, t):
        problem = fh.readline().strip()
        pancakes_list = list(problem.split()[0])
        s = int(problem.split()[1])
        result = find_flips(pancakes_list, s)
        output += "Case #" + str(x+1) + ": " + result + "\n"

with open(case + ".out", "w") as fh:
    fh.write(output)
