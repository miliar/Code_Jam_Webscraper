# GCJ 2017 A-small

infile = open("A-large.in", "r")
outfile = open("A-large-result.txt", "w")

T = int(infile.readline())
for case in range(T):
    line = infile.readline()
    line = line[:-1].split()
    array = []
    K = int(line[1])

    for pancake in line[0]:
        if pancake == "+":
            array.append(True)
        else:
            array.append(False)

    if not False in array:
        answer = 0

    else:
        flips = 0
        for i in range(0, len(array) - (K - 1)):
            if array[i] == False:
                flips += 1
                for k in range(i, i + K):
                    if array[k] == True:
                        array[k] = False
                    else:
                        array[k] = True

        if not False in array:
            answer = flips

        else:
            answer = "IMPOSSIBLE"
        

    

    outfile.write("Case #{0}: {1}\n".format(str(case + 1), str(answer)))
    


infile.close()
outfile.close()
