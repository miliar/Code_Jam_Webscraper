def recycled_numbers():
    inputFile = open('input.txt','r')
    outputFile = open('output.txt','w')
    numTestCases = int(inputFile.readline())
    for tc in range(0,numTestCases):
        line = [int(num) for num in inputFile.readline().split()]
        a = line[0]
        b = line[1]
        recycledPairs = []
        for i in range(a,b+1):
            stringN = '%s'%i;
            n = int(stringN)
            for j in range(1,len(stringN)):
                stringM = '%s%s'%(stringN[-j:],stringN[:-j])
                m = int(stringM)
                stringM = '%s'%m
                if m <= b and m >= a and n!=m and len(stringM)==len(stringN):
                    s = set((n,m))
                    if s not in recycledPairs:
                        recycledPairs.append(s)
        outputString = 'Case #%d: %d\n'%(tc+1,len(recycledPairs))
        outputFile.write(outputString)
            
if __name__ == '__main__':
    recycled_numbers()