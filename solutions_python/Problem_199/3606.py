try:
    infile = open("A-large.in","r")
    infile.readline()
    data = infile.readlines()
    infile.close()
    outfile = open("answer_a_large.txt","w")
    case = 0
    for line in data:
        case +=1
        y = 0
        test = line.rstrip().split()
        flip = int(test[1])
        pan = list(test[0])
        for i in range(len(pan) - flip +1):
            if pan[i] == "-":
                y += 1
                for l in range(flip):
                    if pan[i+l] == "-":
                        pan[i+l] = "+"
                    else:
                        pan[i+l] = "-"
        for i in pan:
            if i == "-":
                y = "IMPOSSIBLE"
                
        outfile.write("Case #")
        outfile.write(str(case))
        outfile.write(": ")
        outfile.write(str(y))
        outfile.write("\n")
    outfile.close()
    print("Done")



except IOError:
    print("IOError")
