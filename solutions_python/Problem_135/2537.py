T = int(raw_input())
for i in range(1,T+1):
    choice1 = int(raw_input())
    line1 = []
    for j in range(1,5):
        tmp = map(int,raw_input().split())
        if j == choice1:
            line1 = tmp
    choice2 = int(raw_input())
    line2 = []
    for j in range(1,5):
        tmp = map(int,raw_input().split())
        if j == choice2:
            line2 = tmp
    ans = []
    for a in line1:
        if a in line2:
            ans.append(a)
    if len(ans) == 0:
        print "Case #" + str(i) + ": Volunteer cheated!"
    elif len(ans) == 1:
        print "Case #" + str(i) + ": " + str(ans[0])
    else:
        print "Case #" + str(i) + ": Bad magician!"        
    

