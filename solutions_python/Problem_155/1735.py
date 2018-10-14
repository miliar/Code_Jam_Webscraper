if __name__ == "__main__":
    fin = open('A-large.in', 'r')
    fout = open('A-large.out', 'w')

    cases = fin.readline()
    #print cases

    for case_num in range(0, int(cases)):
        line = fin.readline().split(' ')
        #print line[0]
        #print line[1]
        peopleCount = 0
        guestCount = 0
        for i in range(0, int(line[0])+1):
            if peopleCount < i:
                guestCount = guestCount + i - peopleCount
                peopleCount = i
            peopleCount += int(line[1][i])

        print "Case #" + str(case_num+1) + ": " + str(guestCount)
        fout.write("Case #" + str(case_num + 1) + ": " + str(guestCount) + "\n")

    fin.close()
    fout.close()