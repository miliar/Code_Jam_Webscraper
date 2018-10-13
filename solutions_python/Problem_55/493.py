


infile = open("C-small-attempt0.in.txt")
outfile = open("C-small.out.txt", "w")

cases = int(infile.readline())

for case in range(1, cases + 1):
    runs, limit, groups = [int(string) for string in infile.readline().rstrip("\n").split(" ")]

    line = []
    total = 0
    for group in [int(string) for string in infile.readline().rstrip("\n").split(" ")]:
        line.append(group)

    for run in range(1, runs + 1):
        ride = []
        current = 0
        while True:
            if len(line) == 0:
                break
            if current + line[0] <= limit:
                current = current + line[0]
                total = total + line[0]
                ride.append(line.pop(0))
            else:
                break
        line.extend(ride)

    outfile.write("Case #" + str(case) + ": " + str(total) + "\n")

outfile.close()
