import sys

with open(sys.argv[1]) as file:
    ts = int(file.readline())
    for test in range(ts):
        arr1 = []
        arr2 = []
        answer1 = int(file.readline())
        for idx in range(4):
            row = file.readline().split()
            arr1.append(map(int, row))
            
        answer2 = int(file.readline())
        for idx in range(4):
            row = file.readline().split()
            arr2.append(map(int, row))

        inter = list(set(arr1[answer1 - 1]).intersection(set(arr2[answer2 - 1])))
        if not inter:
            print "Case #%d: Volunteer cheated!" %(test+1)
        else:
            if len(inter) > 1:
                print "Case #%s: Bad magician!" %(test+1)
            else:
                print "Case #%s: %d" %(test+1, inter[0])
