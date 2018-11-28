import sys, itertools

output_line = "Case #{X:d}: {C}"



if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        N = int(inhandle.readline())
        for n in range(N):
            P, Q = map(int, inhandle.readline().split())
            cells = list(map(int, inhandle.readline().split()))

            smallest = 10000000000
            for order in itertools.permutations(cells):
                payment = 0
                cellstate = [True] * P
                for cell in order:
                    cell -= 1
                    cellstate[cell] = False
                    for look in reversed(cellstate[:cell]):
                        if look: payment += 1
                        else: break
                    for look in cellstate[cell + 1:]:
                        if look: payment += 1
                        else: break
                    #print(payment)
                #print(payment, order)
                smallest = min(smallest, payment)


            print(output_line.format(X=n + 1, C=smallest), file=outhandle)
