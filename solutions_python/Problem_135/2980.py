test_cases = int(raw_input())
for i in range(0,test_cases):
    set1 = []
    answer1 = int(raw_input())
    for j in range(1,5):
        values = map(int,(raw_input().split()))
        set1.append(values)
    set2 = []
    answer2 = int(raw_input())
    for j in range(1,5):
        values = map(int,(raw_input().split()))
        set2.append(values)
    flag = 0
    for j in range(0,4):
        for k in range(0,4):
            if set1[answer1-1][j] == set2[answer2-1][k]:
                flag = flag + 1
                value = set1[answer1-1][j]

    if flag == 1:
        print "Case #" + str(i+1) + ": " + str(value)
    elif flag > 1:
        print "Case #" + str(i+1) + ": Bad magician!"
    else:
        print "Case #" + str(i+1) + ": Volunteer cheated!"
        
    
