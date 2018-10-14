def getLastTidy(N):
    lastTidy = 0
    for i in range(N + 1):

        # check if tidy
        digits = []
        for c in str(i):
            digits.append(int(c))

        isTidy = True
        highest = 0
        for j in range(len(digits)):
            if digits[j] >= highest:
                highest = digits[j]
            else:
                isTidy = False
                break
        
        if isTidy:
            lastTidy = i

    return lastTidy

inputfile = open("small.in")
inputs = inputfile.readlines()

counter = 0
for l in inputs:
    counter += 1

    print("Case #" + str(counter) + ": " + str(getLastTidy(int(l))))
                
