# !/bin/python3

import math

with open("pba.input", "r") as input:
    with open("pba.output", "w") as output:
        testCases = int(input.readline().strip())

        T = 0
        for line in input.readlines():
            T += 1
            data = line.strip().split(" ")
            pancakes = list(data[0])
            nbPancakes = len(pancakes)
            k = int(data[1])

            print("K:", k, " => Pancakes:", pancakes)

            nbSwap = 0
            if k > math.floor(nbPancakes / 2) and pancakes[-k:k].count("-") > 0 and pancakes[-k:k].count("+") > 0:
                output.write("Case #" + str(T) + ": IMPOSSIBLE\n")
                print("Case", T, "IMPOSSIBLE => Pancakes du milieu inversés")
            else:
                for i in range(nbPancakes - (k - 1)):
                    if pancakes[i] == "-":
                        nbSwap += 1
                        for j in range(k):
                            pancakes[i + j] = "+" if pancakes[i + j] == "-" else "-"
                        # pancakes[i + 1] = "+" if pancakes[i + 1] == "-" else "-"
                        # pancakes[i + 2] = "+" if pancakes[i + 2] == "-" else "-"

                if pancakes.count("+") == nbPancakes:
                    output.write("Case #" + str(T) + ": " + str(nbSwap) + "\n")
                else:
                    output.write("Case #" + str(T) + ": IMPOSSIBLE\n")
                    print("Case", T, "IMPOSSIBLE => ", pancakes)

        pass