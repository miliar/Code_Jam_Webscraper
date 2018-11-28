def readinputfile(inputdata):
    lst=inputdata.split('\n')[:-1]
    i = int(lst[0])
    ret=[i]

    prs = [(lst[i],lst[i+1]) for i in xrange(1,len(lst),2)]

    ret.append([(int(x[0].split(' ')[0]), int(x[0].split(' ')[1]), [int(c) for c in x[1].split(' ')]) for x in prs])
    
    return ret

def runcase(R, k, players):
    totalsum = 0
    for i in xrange(R):
        sm = 0
        cyc = 0
        while (((sm+players[0])<=k) and (cyc<len(players))):
            sm += players[0]
            players.append(players[0])
            players = players[1:]
            cyc += 1
        totalsum += sm
    return totalsum

def main():
    INPUT_FILE = 'c:\\Users\\hp\\Desktop\\C-small.in'
    d = open(INPUT_FILE,'r').read()
    a = readinputfile(d)
    for i in xrange(a[0]):
        R,k,N = a[1][i]
        b=runcase(R,k,N)
        
        print 'Case #%d: %d'%(i+1,b)

main()
    
