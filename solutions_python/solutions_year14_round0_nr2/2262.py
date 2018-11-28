



t = int(raw_input())
for case in range(1,t+1):
    f = int(raw_input())
    l =[]
    for i in range(1,5):
        row = raw_input().split()
        if (i==f):
            l = row
    s = int(raw_input())
    r = []
    for i in range(1,5):
        row = raw_input().split()
        if(i==s):
            r = row
    count = 0
    ans = ''
    for el in l:
        if el in r:
            count += 1
            ans = el

    if(count==1):
        print "Case #" + str(case) + ": " + ans
    elif(count > 1):
        print "Case #" + str(case) + ": " + "Bad magician!"
    else:
        print "Case #" + str(case) + ": " + "Volunteer cheated!"


        
        
