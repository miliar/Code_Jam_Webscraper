def oversized_pancake_flipper(inputfile, outputfile):
    fin = open(inputfile, "r")
    fout = open(outputfile, "w")
    no_of_cases = int(fin.readline())

    case_no = 1

    while case_no <= no_of_cases:
        pancakes, K = fin.readline().strip("\n").split(" ")
        pancakes = list(pancakes)
        K = int(K)
        count = 0

        for i in range(len(pancakes)):

            if pancakes[i] == "-":
                if i + K - 1 >= len(pancakes):
                    count = "IMPOSSIBLE"
                    break

                for j in range(K):
                    pancakes[i + j] = "+" if pancakes[i + j] == "-" else "-"

                count += 1

        fout.write("Case #" + str(case_no) + ": " + str(count) + "\n")

        case_no += 1


    fin.close()
    fout.close()

oversized_pancake_flipper("A-large.in", "A-large.out")