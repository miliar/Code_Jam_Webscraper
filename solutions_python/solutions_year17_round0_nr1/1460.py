with open("A-large.in", "r") as inp:
    with open("A-large.out", "w") as outp:
        cases = int(inp.readline())
        for i in range(cases):
            flips = 0
            pancakes, size = inp.readline().strip().split()
            pancakes = list(pancakes)
            size = int(size)
            for j in range(len(pancakes)-size+1):
                if pancakes[j] == "-":
                    for k in range(j, j+size):
                        if pancakes[k] == "-":
                            pancakes[k] = "+"
                        else:
                            pancakes[k] = "-"
                    flips += 1
            if "-" in pancakes:
                outp.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")
            else:
                outp.write("Case #" + str(i+1) + ": " + str(flips) + "\n")
