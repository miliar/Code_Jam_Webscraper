with open("A-small-attempt0.in") as f:
    T = f.readline().rstrip('\n');
    #print T
    for ii in range(int(T)):
        guess1 = f.readline().rstrip('\n');
        for _ in range(int(guess1)-1):
            f.readline();
        list1 = f.readline().rstrip('\n').split(' ')
        #print list1
        for _ in range(4-int(guess1)):
            f.readline();

        guess2 = f.readline().rstrip('\n');
        for _ in range(int(guess2)-1):
            f.readline();
        list2 = f.readline().rstrip('\n').split(' ')
        #print list2
        for _ in range(4-int(guess2)):
            f.readline();

        common = list(set(list1).intersection(list2))
        #print common

        length = len(common)
        if length==1:
            print "Case #%s: %s" %(ii+1, common[0])
        elif length > 1:
            print "Case #%s: Bad magician!" %(ii+1)
        else:
            print "Case #%s: Volunteer cheated!" %(ii+1)


