def readint():
    filein = open("A-large.in")
    total = int(filein.readline())
    #filein.readline()
    data = []
    for case in range(0, total):
        templine = filein.readline()
        templine = templine.strip()
        tempsplit = templine.split(" ")

        tempsplit[0] = int(tempsplit[0])
        tempsplittoint = []
        for i in range(len(tempsplit[1])):
            tempsplittoint.append(int(tempsplit[1][i]))

        tempsplit[1] = tempsplittoint

        data.append(tempsplit)
    filein.close()
    return data


def mainwork(data=[]):
    answer = []
    for case in range(len(data)):
        takefriend = 0
        for time in range(len(data[case][1])-1):
            havenum = 0
            for plus in range(len(data[case][1])-1-time):
                havenum += data[case][1][plus]

            if havenum+takefriend < data[case][0]-time:
                if takefriend < data[case][0]-time-havenum:
                    takefriend = data[case][0]-time-havenum
        answer.append("Case #"+str(case+1)+": "+str(takefriend))
    return answer


if __name__ == "__main__":
    temp = mainwork(readint())
    print(temp)
    file = open("A-large.in")
    print(file.readlines())
    file.close()
    outfile = open("answerl.out", "w")
    for i in range(len(temp)):
        outfile.write(temp[i])
        outfile.write("\n")
    outfile.close()
    check = open("answerl.out")
    print(check.readlines())
    check.close()