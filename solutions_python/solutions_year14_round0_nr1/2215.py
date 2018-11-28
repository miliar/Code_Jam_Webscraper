infile = open("input.txt", "rt")

t = int(infile.readline())

outfile=open('output.txt', 'w+')

for case in range(1, t + 1):
    rowNum1 = int(infile.readline()) - 1
    row1 = set()
    for i in range(0,4):
        nums = infile.readline().rstrip().split(" ")
        if (rowNum1 == i):
            for j in range(0,4):
                row1.add(int(nums[j]))

    rowNum2 = int(infile.readline()) - 1
    row2 = set()
    for i in range(0,4):
        nums = infile.readline().rstrip().split(" ")
        if (rowNum2 == i):
            for j in range(0,4):
                row2.add(int(nums[j]))
    intersection = row1.intersection(row2)
    outfile.write("Case #" + str(case) + ": ")
    if len(intersection) == 1:
        outfile.write(str(next(iter(intersection))) + "\n")
    elif len(intersection) > 1:
        outfile.write("Bad magician!" + "\n")
    else:
        outfile.write("Volunteer cheated!" + "\n")

outfile.close()
    
    
