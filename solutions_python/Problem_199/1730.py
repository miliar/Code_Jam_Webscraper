import sys

case = 0

with open(sys.argv[1]) as file:
    next(file)
    for line in file:
        case += 1
        flips = 0
        pancakes = list(line.split(" ")[0])
        size = int(line.split(" ")[1])
        if size > pancakes:
            print "Case #" + str(case) + ": IMPOSSIBLE"
        elif "-" not in pancakes:
            print "Case #" + str(case) + ": 0"
        else:
            for i in range(0, len(pancakes)):
                if pancakes[i] is "-":
                    flips += 1
                    if i + size <= len(pancakes):
                        for j in range(i, i + size):
                            if pancakes[j] is "+":
                                pancakes[j] = "-"
                            else:
                                pancakes[j] = "+"
                    else:
                        for j in range(len(pancakes) - size, len(pancakes)):
                            if pancakes[j] is "+":
                                pancakes[j] = "-"
                            else:
                                pancakes[j] = "+"
            if "-" not in pancakes:
                print "Case #" + str(case) + ":", flips
            else:
                print "Case #" + str(case) + ": IMPOSSIBLE"
