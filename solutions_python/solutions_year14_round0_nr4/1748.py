__author__ = 'unknow'

def magic(case):
    N = int(allInput.readline().replace("\n", ""))
    Naomi = allInput.readline().replace("\n", "").split(" ")
    Ken = allInput.readline().replace("\n", "").split(" ")
    Naomi = [float(x) for x in Naomi]
    Naomi = sorted(Naomi, key=float, reverse=False)
    Ken = [float(x) for x in Ken]
    Ken = sorted(Ken, key=float, reverse=True)
    Ken2 = sorted(Ken, key=float, reverse=False)
    score = 0
    flag = 0
    count = 1
    score2 = 0
    flag2 = 0
    count2 = 0
    for i in range(N):
        if flag == 1:
            flag = 0
            Ken[i-count] = 9999
        for j in range(N):
            #print Naomi[i], Ken, score

            if Naomi[i] > Ken[j]:
                score += 1
                count += 1
                Ken[j] = 9999
                flag = 0
                break
            else:
                flag = 1

    for i in range(N):
        if flag2 == 1:
            flag2 = 0
            score2 += 1

        for j in range(N):
            if Naomi[i] < Ken2[j]:
                flag2 = 0
                Ken2[j] = -1
                break
            else:
                flag2 = 1
                count2 +=1

    if flag2 == 1:
        flag2 = 0
        score2 += 1

    print "Case #%d: %d %d" % (case , score, score2)

if __name__ == "__main__":
    allInput = open("D-large.in", 'r')
    number_of_test_case = int(allInput.readline())
    case = 0
    if number_of_test_case > 100 or number_of_test_case < 1:
        exit(1)
    for a in range(number_of_test_case):
        case = case + 1
        magic(case)
    allInput.close()