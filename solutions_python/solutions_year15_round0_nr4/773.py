def readint():
    filein = open("D-small-attempt3.in")
    total = int(filein.readline())
    #filein.readline()
    data = []
    for case in range(0, total):
        templine = filein.readline()
        templine = templine.strip()
        tempre = templine.split(" ")
        for num in range(len(tempre)):
            tempre[num] = int(tempre[num])
        data.append(tempre)
    filein.close()
    return data


def dell4(case, temp):
    if case >= 4:
        return temp+1
    if case == 2:
        return temp-1
    return temp


def mainwork(data=[]):
    print(data)
    answer = []
    for case in range(len(data)):
        caseplus = case+1
        if (data[case][1]*data[case][2]) % data[case][0] == 0 and data[case][0] < 7:
            if data[case][0] <= data[case][1]:
                tempsquer = data[case][0] ** 0.5
                if tempsquer % 1 != 0:
                    tempsquer = int(tempsquer)+1
                tempsquer = dell4(data[case][0], tempsquer)
                if tempsquer <= data[case][2]:
                    answer.append("Case #"+str(caseplus)+": GABRIEL")
                else:
                    answer.append("Case #"+str(caseplus)+": RICHARD")
            elif data[case][0] <= data[case][2]:
                tempsquer = data[case][0] ** 0.5
                if tempsquer % 1 != 0:
                    tempsquer = int(tempsquer)+1
                tempsquer = dell4(data[case][0], tempsquer)
                if tempsquer <= data[case][1]:
                    answer.append("Case #"+str(caseplus)+": GABRIEL")
                else:
                    answer.append("Case #"+str(caseplus)+": RICHARD")
            else:
                answer.append("Case #"+str(caseplus)+": RICHARD")
        else:
            answer.append("Case #"+str(caseplus)+": RICHARD")
    return answer


def debuging():
    source = open("D-small-attempt3.in")
    sourceget = source.readlines()
    source.close()
    answer = open("answer.out")
    answerget = answer.readlines()
    answer.close()
    for papa in range(len(answerget)):
        print(sourceget[papa+1])
        print(answerget[papa])


if __name__ == "__main__":
    temp = mainwork(readint())
    print(temp)
    file = open("D-small-attempt3.in")
    print(file.readlines())
    file.close()
    outfile = open("answer.out", "w")
    for i in range(len(temp)):
        outfile.write(temp[i])
        outfile.write("\n")
    outfile.close()
    check = open("answer.out")
    print(check.readlines())
    check.close()
    debuging()