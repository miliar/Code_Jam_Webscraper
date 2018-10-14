def GetACase():
    result = []
    casestr = raw_input()

    f = 0
    start = 0    
    for i in range(len(casestr)):
        if casestr[i] == '(':
            f +=1
            start = i + 1                  
        elif casestr[i] == ')':
            f -=1
            result.append(casestr[start:i])
        else:
            if f == 0:
                result.append(casestr[i])
            else:
                continue

    return result

#aaa= GetACase()                
#print aaa

L,D,N = raw_input().split(' ')
L,D,N = int(L),int(D),int(N)

words = []
for d in range(D):
    words.append(raw_input())
    

for n in range(N):
    count = 0
    case = GetACase()
    for word in words:
        count += 1
        for i in range(L):
            if word[i] not in case[i]:
                count -= 1
                break

    print 'Case #%d: %d' % (n+1,count)
            






        