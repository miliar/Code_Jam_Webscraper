

input = open("A-small-attempt0.in", 'r')
output = open("output.txt", 'a')

cases = int(input.readline())
if (cases < 1) or (cases > 100):
    output.write("Bad Input!\n")

else:
    outs = []
    for i in range(cases):
        ans1 = int(input.readline())
        for j in range(4):
            temp = input.readline()
            if (j+1 == ans1):
                line = temp.rstrip('\n').split(" ")
                poss1 = [ ]
                for val in line:
                    poss1.append(int(val))

        ans2 = int(input.readline())
        for j in range(4):
            temp = input.readline()
            if (j+1 == ans2):
                line = temp.rstrip('\n').split(" ")
                poss2 = [ ]
                for val in line:
                    poss2.append(int(val))
    
        poss = list(set(poss1).intersection(set(poss2)))

        if len(poss) < 1:
            outs.append("Volunteer cheated!")
        elif len(poss) > 1:
            outs.append("Bad magician!")
        else:
            outs.append(str(poss[0]))
        

    for i in range(cases):
        output.write("Case #" + str(i+1) + ": " + outs[i] + "\n")
