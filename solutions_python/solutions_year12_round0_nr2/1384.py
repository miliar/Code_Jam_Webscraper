def GetBestScore(num, surprising):
    r = num%3
    n = num/3

    if ( num == 0 ):
        return 0
    if ( num == 1 ):
        return 1
    
    
    if ( r == 0 ):
        if surprising:
            return n+1
        else:
            return n
    if ( r == 1 ):
        if surprising:
            return n+1
        else:
            return n+1
    if ( r==2 ):
        if surprising:
            return n+2
        else:
            return n+1

def Satisfy(number, bestScore):
    s = GetBestScore(number,True)
    ns = GetBestScore(number,False)

    return( (s>=bestScore, ns>=bestScore))

numInputs = input('')

response = []

for j in range(0,numInputs):
    line  = str(raw_input('')).split(' ')

    s = int(line[1])
    p = int(line[2])
    scores = line[3:]

    # The number of players who achieve above the given score
    numP = 0

    for i in scores:
        d = Satisfy(int(i), p)
        if d[0] and not d[1] and s>0:
            s = s-1
            numP = numP + 1
        if d[1]:
            numP = numP + 1
    response.append(numP)

j = 0
for i in response:
    print "Case #" + str(j) + ": " + str(i)
    j = j+1
