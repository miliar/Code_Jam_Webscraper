infile = open("input.txt")
outfile = open("output.txt", 'w')

one = infile.readline()
testCases = int(one)
print(str(testCases) + " test cases")


case = 1

for line in infile:
    n, r, c = map(int, line.strip().split())
    print("n = " + str(n))
    print("r = " + str(r))
    print("c = " + str(c))

    area = r * c
    can_win = False

    if ((area - n) % n != 0):
        can_win = True
    elif (area < n):
        can_win = True
    else:
        if (n == 2 or n == 1):
            can_win = False
        elif (n == 3):
            if (area == 3):
                can_win = True
            else:
                can_win = False
        elif (n == 4):
            if (area == 8 or area == 4):
                can_win = True
            elif (area == 12 or area == 16):
                can_win = False




    if can_win:
        print("RICHARD")
        outfile.write("Case #" + str(case) + ": " + "RICHARD" + "\n")
    else:
        print("GABRIEL")
        outfile.write("Case #" + str(case) + ": " + "GABRIEL" + "\n")
    case += 1

outfile.close()
infile.close()
