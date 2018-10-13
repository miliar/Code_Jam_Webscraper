linenum = 0
for line in open("A-large.in", "rU"):
    if linenum == 0:
        cases = int(line)
    else:
        listy = line.split(" ")
        status = 0
        workinglist = []
        extension = []
        listy.remove(listy[0])
        for item in listy:
            if status == 0:
                extension.append(item)
            elif status == 1:
                extension.append(int(item))
                workinglist.append(extension)
                extension = []
            status = 1 - status

        poso = 1
        posb = 1
        indexo = 0
        indexb = 0
        while indexo < len(workinglist) and workinglist[indexo][0] != "O":
            indexo += 1
        if indexo != len(workinglist):
            targeto = workinglist[indexo][1]
        while indexb < len(workinglist) and workinglist[indexb][0] != "B":
            indexb += 1
        if indexb != len(workinglist):
            targetb = workinglist[indexb][1]
        currentindex = 0

        time = 0
        while currentindex < len(workinglist):
            opush = False
            if indexo != len(workinglist):
                if poso > targeto:
                    poso -= 1
                elif poso < targeto:
                    poso += 1
                elif poso == targeto:
                    if currentindex == indexo:
                        indexo += 1
                        while indexo < len(workinglist) and workinglist[indexo][0] != "O":
                            indexo += 1
                        if indexo != len(workinglist):
                            targeto = workinglist[indexo][1]
                        currentindex += 1
                        opush = True
            if indexb != len(workinglist):
                if posb > targetb:
                    posb -= 1
                elif posb < targetb:
                    posb += 1
                elif posb == targetb:
                    if currentindex == indexb and opush == False:
                        indexb += 1
                        while indexb < len(workinglist) and workinglist[indexb][0] != "B":
                            indexb += 1
                        if indexb != len(workinglist):
                            targetb = workinglist[indexb][1]
                        currentindex += 1
            time += 1
            #print time, poso, posb
        print "Case #" + str(linenum) + ": " + str(time)
    linenum += 1


    
