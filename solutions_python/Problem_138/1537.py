with open("D-large.in") as f:
    T = f.readline().rstrip('\n');
    #print T
    for ii in range(int(T)):
        N = f.readline().rstrip('\n')
        list1 = f.readline().rstrip('\n').split(' ')
        list2 = f.readline().rstrip('\n').split(' ')
        list1.sort()
        list2.sort()

        # War
        #print list1
        #print list2
        index2 = 0
        war_count = 0
        curr_index = 0
        for item in list2:
            if item > list1[curr_index]:
                war_count += 1
                curr_index += 1
        """
        for item in list1:
            print "considering item: ", item
            #print "item: ", item
            #print index2
            while (list2[index2] < item):
                index2 += 1
                if index2 >= len(list2):
                    break
                elif list2[index2] > item:
                    war_count += 1
                    index2 += 1
                    if index2 >= len(list2):
                        break
            print "index2: ", index2
            if index2 >= len(list2):
                    break
        """
        #print war_count
        answer2 = int(N) - war_count
        #print "answer2: ", answer2

        """
        # Deceit war
        answer11 = 0
        index1 = 0
        index2 = 0
        print list1
        print list2
        #print "comparing: ", list1[index1], " and ", list2[index2]
        while (list1[index1] < list2[index2]):
            #print "comparing: ", list1[index1], " and ", list2[index2]
            answer11 += 1
            if (index1 < len(list1)-1):
                index1 += 1
                index2 += 1
            else:
                break
        print "answer11: ", answer11
    
        answer12 = 0
        index1 = 0
        index2 = 0
        list2.sort(reverse=True)
        #print list1
        #print list2
        while (list1[index1] < list2[index2]):
            answer12 += 1
            if (index1 < len(list1)-1):
                index1 += 1
                index2 += 1
            else:
                break
        print "answer12: ", answer12

        if answer11 < answer12:
            answer1 = answer11
        else:
            answer1 = answer12
        answer1 = int(N) - answer1
        """
        # Deceit war
        answer1 = 0
        curr_index = 0
        for item in list1:
            if item > list2[curr_index]:
                answer1 += 1
                curr_index += 1

        """
        answer1 = 0
        list1.sort()
        list2.sort()
        for idx, val in enumerate(list2):
            if list1[idx] > list2[idx]:
                answer1 += 1
        """
        """
        answer1 = 0
        index1 = 0
        index2 = 0
        list1.sort()
        list2.sort(reverse=True)
        print list1
        print list2
        while (list1[index1] < list2[index2]):
            answer1 += 1
            if (index1 < len(list1)-1):
                index1 += 1
                index2 += 1
            else:
                break

        answer1 = int(N) - answer1
        """

        print "Case #%s: %d %d" %(ii+1, answer1, answer2)

        #print N
        #print list1
        #print list2
