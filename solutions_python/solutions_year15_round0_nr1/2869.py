#Standing Ovation

try:
    infile = open("A-large.in", "r")
    outfile = open("A-large-attempt-output.txt", "a")

    #Get number of testcases
    testcases = int(infile.readline().rstrip())
    lines = infile.readlines()

    for test in range(0, testcases):
        line = lines[test].rstrip().split(" ")
        smax = int(line[0])
        audience = line[1]

        friends = 0
        clapping = int(audience[0])

        if clapping >= smax: #No friends needed
            output = "Case #{0}: 0\n".format(test+1)
            outfile.write(output)
        else:
            for slevel in range(1, len(audience)):
                if int(audience[slevel]) > 0 and slevel > clapping: #Not enough!
                    friends += (slevel - clapping)
                    clapping += (slevel - clapping) #Friends also clapping
                    clapping += int(audience[slevel])
                else:
                    clapping += int(audience[slevel])
            output = "Case #{0}: {1}\n".format(test+1, friends)
            outfile.write(output)
    
    infile.close()
    outfile.close()

except IOError:
    print("File could not be opened.")
