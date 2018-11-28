from datetime import datetime

if __name__ == "__main__":
    fin = "../in/small.in"
    fou = "../out/small.out"
    stt = datetime.now()

    inf = open(fin, "r")
    ouf = open(fou, "w")

    numcases = int(inf.readline())
    for tst in range(numcases):
        # Clear lists
        rows = []
        grid = []

        # First shuffle
        rows.append(int(inf.readline()))
        grid.append([inf.readline().split() for i in xrange(4)])
        # Second shuffle
        rows.append(int(inf.readline()))
        grid.append([inf.readline().split() for i in xrange(4)])

        tstnums = grid[0][rows[0]-1]      # Get list of nums in row from first shuffle
        count = 0
        validnums = []
        for num in tstnums:
            if num in grid[1][rows[1]-1]:
                count += 1
                validnums.append(num)

        rtn = "Case #%d: " % (tst+1)
        if count == 0:
            rtn += "Volunteer cheated!"
        elif count == 1:
            rtn += str(validnums[0])
        else:
            rtn += "Bad magician!"
        ouf.write(rtn + "\n")

    print "Answer in: " + str(datetime.now() - stt)
