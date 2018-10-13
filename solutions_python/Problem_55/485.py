import sys

infile = open(sys.argv[1])
outfile = open("out", "w")

number = infile.readline().strip()
number = int(number)

for i in range(number):
    r, k, n = infile.readline().strip().split(" ")
    r, k, n = int(r), int(k), int(n)
    groups = infile.readline().strip().split(" ")
    groups = [int(group) for group in groups]

    earning = 0
    last = 0
    for j in range(r):
        capacity = k
        for x, group in enumerate(groups):
            if capacity >= group:
                capacity -= group
                earning += group
                last = x
            else:
                break;
        groups = groups[last+1:] + groups[:last+1]

    outfile.write("Case #{0}: {1}\n".format(i+1, earning))




