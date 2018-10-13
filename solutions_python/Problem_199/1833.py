t = int(raw_input())

result = []

for i in range(t):
    count = 0
    entry = raw_input()
    splitEntry = entry.split()
    s = splitEntry[0]
    sList = list(s)
    k = int(splitEntry[1])


    for j in range (len(sList)):
        if sList[j] == '+':
            pass
        elif(len(sList)>=j+k):

            count += 1
            for l in range (j,j+k):
                if(sList[l] == '-'):    
                    sList[l] = '+'
                else:
                    sList[l] = '-'

    if('-' in sList):
        result.append('IMPOSSIBLE')
    else:
        result.append(str(count))

for p in range(t):
    print 'Case #'+str(p+1)+': '+result[p]





