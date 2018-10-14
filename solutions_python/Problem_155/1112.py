infile = open("B-input.txt")
outfile = open("B-output.txt", 'w')

one = infile.readline()
testCases = int(one)
print(str(testCases) + " test cases")


case = 1

for line in infile:
    s_max, bitstring = line.strip().split()
    print(s_max)
    print(bitstring)

    standing = 0
    invited = 0

    for i in range(0, len(bitstring)):
        s_i = int(bitstring[i])
        if (standing >= i):
            standing += s_i
        else:
            invited += (i - standing)
            standing += (i - standing) + s_i

    print("invited: " + str(invited))
    outfile.write("Case #" + str(case) + ": " + str(invited) + "\n")
    case += 1

outfile.close()
infile.close()
