__author__ = 'unknow'

def magic(case):
    row1 = []
    row2 = []
    count_cheated = 0
    flag = 0
    result = ""
    choose1 = int(allInput.readline().replace("\n", ""))
    for i in range(4):
        row1.append(allInput.readline().replace("\n", "").split(" "))

    choose2 = int(allInput.readline().replace("\n", ""))
    for i in range(4):
        row2.append(allInput.readline().replace("\n", "").split(" "))

    #check cheated
    for i in row1[choose1-1]:
        for j in row2[choose2-1]:
            if i == j:
                result = i
            else:
                count_cheated += 1
    if count_cheated == 16:
        print "Case #%d: Volunteer cheated!" %case
        return

    #check bad magician
    check = set(row1[choose1-1]).intersection(set(row2[choose2-1]))
    if len(check) > 1:
        print "Case #%d: Bad magician!" %case
        return
    else:
        flag = 1

    if flag ==1:
        print "Case #%d: %s" %(case, result)


if __name__ == "__main__":
    allInput = open("A-small-attempt2.in", 'r')
    number_of_test_case = int(allInput.readline())
    case = 0
    if number_of_test_case > 100 or number_of_test_case < 1:
        exit(1)
    for a in range(number_of_test_case):
        case = case + 1
        magic(case)
    allInput.close()