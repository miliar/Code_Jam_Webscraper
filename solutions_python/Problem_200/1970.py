def main():
    t = int(raw_input())

    result = []


    for i in xrange(t):
        n = raw_input()

        nList = list(n)

        while nList != sorted(nList):
            nList = trials(nList)

        result.append(int(''.join(nList)))

    for p in range(t):
        print 'Case #'+str(p+1)+': '+str(result[p])



def trials(nList):
    for j in range (len(nList)):

        if(j+1<len(nList)):
            if nList[j] > nList[j+1]:
                if nList[j] == '0':
                    nList[j] = '9'
                else:
                    nList[j] = str(int(nList[j])-1)


                for k in range(j+1, len(nList)):
                    nList[k] = '9'

    return nList

main()
