inputFile = open('A-large.in', 'r')
lines = inputFile.readlines()
inputFile.close()

outputFile = open('A-large.out', 'w')

numTests = int(lines[0])

def makeTournament(n,letters):
    ''' letters as [(num1, let1) num2, num3), (let1, let2, let3)]'''
    sortedLetters = sorted(letters)
    sortedLetters.reverse()
    #print sortedLetters
    n1 = sortedLetters[0][0]
    l1 = sortedLetters[0][1]
    n2 = sortedLetters[1][0]
    l2 = sortedLetters[1][1]
    n3 = sortedLetters[2][0]
    l3 = sortedLetters[2][1]
    if min([n1,n2,n3]) < 0:
        return None
    if n == 1:
        if n1 != 2:
            sortedTourney = sorted([l1] + [l2])
            return sortedTourney[0]+sortedTourney[1]
        else:
            return None
    else:
        dist = getDistribution(n-1)
        
        t1 = makeTournament(n-1, [(dist[0], l1), (dist[1], l2), (dist[2], l3)])
        remainingLetters = [(n1-dist[0], l1), (n2-dist[1], l2), (n3-dist[2], l3)]
        t2 = makeTournament(n-1, sorted(remainingLetters))
        if t1 and t2 and t1 != t2:
            if t1 < t2:
                return t1 + t2
            else:
                return t2 + t1
    
        

def getDistribution(n):
    x = [0,0,0]
    c = 0
    while c < 2**n:
        x[c%3] += 1
        c += 1
    return x


for i in range(1, numTests+1):
    [n, r, p, s] = map(lambda x: int(x), lines[i].split())

    t = makeTournament(n, [(r, 'R'), (p, 'P'), (s, 'S')])

    if not t:
        t = 'IMPOSSIBLE'

    outputFile.write('Case #'+str(i)+': ' + t+'\n')

outputFile.close()
