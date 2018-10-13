

if __name__ == '__main__':
    # load input file
    
    inputfile = file("A-small-attempt1.in")
    outputfile = file("output.txt", "w+")
    num_of_testcases = int(inputfile.readline())
    print num_of_testcases



    
    for testcase in range(1,num_of_testcases+1):
        cards = [False] * 17
        row = 1
        count = 0;
        print "Load testcase: %s" % testcase
        first_ans = (int)(inputfile.readline())

        ''' skip unnecessary rows '''
        while (row != first_ans):
            inputfile.readline()
            row += 1

        ''' read row '''
        target = inputfile.readline().strip().split(" ")
        print target 
        for s in target:
            cards[int(s)] = True
        row += 1
        
        while (row <= 4):
            inputfile.readline()
            row += 1

        second_ans = (int)(inputfile.readline())
        row = 1
        ''' skip unnecessary rows '''
        while (row != second_ans):
            inputfile.readline()
            row += 1

        ''' read row '''
        target = inputfile.readline().strip().split(" ")
        count = 0;
        number = 0;
        for s in target:
            if (cards[int(s)] == True):
                number = int(s)
                count += 1
                if (count > 1):
                    number = 0
                    break
        row += 1
        while (row <= 4):
            inputfile.readline()
            row += 1
        if (count == 0):
            print "Case #%s: Volunteer cheated!" % testcase
            outputfile.write("Case #%s: Volunteer cheated!\n" % testcase)
        elif (count == 1):
            print "Case #%s: %d" % (testcase, number)
            outputfile.write("Case #%s: %d\n" % (testcase, number))
        else:
            print "Case #%s: Bad magician!" % testcase
            outputfile.write("Case #%s: Bad magician!\n" % testcase)

    #for result in results:
     #   outstring = "Case #%s: %s\n" % result
      #  print outstring
      #  outputfile.write(outstring)

    outputfile.close()
    inputfile.close()

    
