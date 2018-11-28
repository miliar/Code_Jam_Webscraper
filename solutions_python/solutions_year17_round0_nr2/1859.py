import sys

case = 0

with open(sys.argv[1]) as file:
    next(file)
    for line in file:
        case += 1
        number = int(line)
        i = number
        while i > 0:
            #print i
            step = ""
            isTidy = True
            temp = str(i)

            for j in range(1, len(temp)):
                if temp[j] < temp[j - 1]:
                    isTidy = False
                    break
            if isTidy:
                print "Case #" + str(case) + ": " + str(temp)
                break

            for j in range(len(temp) - 1, 0, -1):
                if temp[j] <= temp[j - 1]:
                    isTidy = False
                    step = temp[j] + step
                else:
                    break

            #print step
            if step.count("0") == len(step):
                i -= 1
            else:
                i -= int(step)
