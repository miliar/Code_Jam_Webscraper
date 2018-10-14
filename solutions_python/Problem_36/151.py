template = "welcome to code jam"

with open("C.in") as infile:
    with open("C.out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            # Perform all nessesary calculation
            string = infile.readline().splitlines()[0]
            prev = [1] + [0] * len(template)
            for ch in string:
                cur = prev[:]
                for i, c in enumerate(template):
                    if c==ch:
                        cur[i + 1] += prev[i]
                        cur[i + 1] %= 10000
                prev = cur
            times = cur[-1]
            outfile.write("Case #{nc}: {data:04}\n".format(nc=ncase+1,data=times))
print("Ready")
