import sys

in_file = open(sys.argv[1], "r")

out_file = open("output.out", "w")

t = int(in_file.readline())

for itera in range(t):
    in_file.readline()
    params = in_file.readline().split(' ')
    mush = map(int, params)
    minmin = 0
    maxmin = 0
    worst_case = 0
    for i in range(1, len(mush)):
        if mush[i - 1] - mush[i] > 0:
            if mush[i - 1] - mush[i] > worst_case:
                worst_case = mush[i - 1] - mush[i]
            minmin += mush[i - 1] - mush[i]
    for i in range(1, len(mush)):
        if mush[i - 1] > worst_case:
            maxmin += worst_case
        else:
            maxmin += mush[i - 1]
    out_file.write("Case #" + str(itera + 1) + ": " + str(minmin) + " " + str(maxmin))

    out_file.write("\n")

in_file.close()
out_file.close()
