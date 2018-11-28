t = int(raw_input())

for i in range (0, t):
    case = raw_input()
    case = case.split()
    s = case[0]
    shy = str(case[1])
    answer = 0
    total = 0
    for j in range (0, int(s)+1):
        total = total + int(shy[j])
        if (total < (j+1)):
            answer = answer + (j + 1 - total)
            total = total + (j + 1 - total)
        else:
            continue
    print ("Case #" + str(i+1)+ ": "+ str(answer))
    #print str(answer)
