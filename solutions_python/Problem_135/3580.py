cases = int(raw_input())

for case in range(1,cases+1):
    ansA = int(raw_input())
    rowA = []
    for r in range(4):
        rowA.append(map(int,raw_input().split(" ")))
        
    ansB = int(raw_input())
    rowB = []
    for r in range(4):
        rowB.append(map(int,raw_input().split(" ")))
        
    commons = set(rowA[ansA-1]).intersection(rowB[ansB-1])
    commonsC = list(commons)
    if (len(commonsC) == 1):
        answ = str(commonsC[0])
    elif (len(commonsC) == 0):
        answ = 'Volunteer cheated!'
    else :
        answ = 'Bad magician!'
        
    print "Case #%i: %s" % (case,answ)
