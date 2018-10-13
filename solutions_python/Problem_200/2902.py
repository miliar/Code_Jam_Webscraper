n = input()
for i in range(0,n):
    a = input()
    astr = str(a)
    isAnswer = True
    for j in range(1,len(astr)):
        if astr[j] < astr[j-1]:
            isAnswer = False
        if isAnswer == False:
            break
    if isAnswer:
        print "Case #" + str(i+1) + ": " + astr
        continue
    while True:
        a -= 1
        astr = str(a)
        isAnswer = True
        for j in range(1, len(astr)):
            if astr[j] < astr[j-1]:
                isAnswer = False
            if isAnswer == False:
                break
        if isAnswer:
            print "Case #" + str(i+1) + ": " + astr
            break
