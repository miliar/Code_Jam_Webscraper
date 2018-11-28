T = (int)(raw_input())
for x in range(T):
    array = (raw_input())
    splitted = []
    splitted = array.split(" ")
    n = (int)(splitted[0])
    s = (int)(splitted[1])
    p = (int)(splitted[2])
    scores = splitted[3:n+3]
    count1=0
    count2=0
    for score in scores:
        score = (int)(score)
        if score >= p*3-2:
            count1 += 1
            continue
        elif score >= p*3-4 and score!=0:
            count2 += 1    
            continue
    print "Case #" + str(x+1)+": " + str(count1+min(count2,s))