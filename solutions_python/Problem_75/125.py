linenum = 0
for line in open("B-large.in", "rU"):
    if linenum == 0:
        cases = int(linenum)
    else:
        listy = line.strip().split(" ")
        combinelist = []
        resultlist = []
        opposelist = []
        index = 0
        combines = int(listy[index])
        while index < combines:
            index += 1
            extension = sorted([listy[index][0], listy[index][1]])
            combinelist.append(extension)
            resultlist.append(listy[index][2])
        index += 1
        opposes = int(listy[index])
        while index < combines+ opposes + 1:
            index += 1
            extension = sorted([listy[index][0], listy[index][1]])
            opposelist.append(extension)
        index += 2
        workinglist = []
        for letter in listy[index]:
            special = False
            if len(workinglist) > 0:
                if sorted([workinglist[-1], letter]) in combinelist:
                    workinglist[-1] = resultlist[combinelist.index(sorted([workinglist[-1], letter]))]
                    special = True
            if special != True:
                for letter2 in workinglist:
                    if sorted([letter, letter2]) in opposelist:
                        workinglist = []
                        special = True
            if special == False:
                workinglist.append(letter)
            
        print "Case #" + str(linenum) + ": [" + ", ".join(workinglist) + "]"
            
    linenum += 1
