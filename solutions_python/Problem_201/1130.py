# !/bin/python3

import math

with open("pbc.input", "r") as input:
    with open("pbc.output", "w") as output:
        testCases = int(input.readline().strip())

        T = 0
        for line in input.readlines():
            T += 1
            data = line.strip().split()

            n = int(data[0])
            k = int(data[1])

            if n == k:
                x = 0
                y = 0
            else:
                l = pow(2, math.floor(math.log(k, 2))) - 1
                l_1 = pow(2, math.floor(math.log(k, 2)) + 1) - 1

                print(k - 1, l, l_1)

                average_zone =(n - l) / (l + 1)
                percentage_zone = 100 * (average_zone - math.floor(average_zone))
                percentage_k = ((k - l) / (l_1 - l)) * 100

                if l_1 <= n and percentage_k > percentage_zone:
                    n = math.floor(average_zone)
                else:
                    n = math.ceil(average_zone)
                print("N:", n)

                y = math.floor((n - 1) / 2)
                x = math.ceil((n - 1) / 2)

            output.write("Case #" + str(T) + ": " + str(x) + " " + str(y) + "\n")
            print(data)