def solver():
    test_cases = int(raw_input(""))
    for test_case in xrange(1,test_cases+1):
        row_1_number = int(raw_input(""))
        row1 = []
        for row_number in xrange(1,5):
            s = raw_input("")
            if( row_number == row_1_number ):
                row1 = map(int, s.split())

        row_2_number = int(raw_input(""))
        row2 = []
        for row_number in xrange(1,5):
            s = raw_input("")
            if( row_number == row_2_number ):
                row2 = map(int, s.split())

        row_1_hash_map = [False] * 16
        for i in row1:
            row_1_hash_map[i-1] = True

        common = []
        for i in row2:
            if(row_1_hash_map[i-1]):
                common.append(i)

        if len(common) == 0: #Volunteer cheated
            print "Case #" + str(test_case) + ": Volunteer cheated!"
        elif len(common) == 1: #The magician succeeded
            print "Case #" + str(test_case) + ": " + str(common[0])
        else: # The magician screwed up
            print "Case #" + str(test_case) + ": Bad magician!"

if __name__ == '__main__':
    solver()
