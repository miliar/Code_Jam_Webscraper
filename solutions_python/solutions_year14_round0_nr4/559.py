def warGames(infile):
    N = int(infile.readline().strip())
    Naomi = map(lambda x: float(x), infile.readline().split())
    Ken = map(lambda x: float(x), infile.readline().split())
    Naomi.sort()
    Ken.sort()
    return playDeceitfulWar(Naomi[:],Ken[:],N), playWar(Naomi[:],Ken[:],N)


def playWar(Naomi, Ken, N):
    
    wins = 0
    for i in range(N):
        x = Naomi.pop()
        if Ken[-1] < x:
            del Ken[0]
            wins += 1
        else:
            Ken.pop()
    return wins

## If the Naomi's smallest number is less than Ken's say the lowest is the avg of Ken's top 2
## Else say the lowest is greater than Ken's largest
def playDeceitfulWar(Naomi, Ken, N):
    wins = 0
    for i in range(N):
        if Naomi[0] <= Ken[0]:
            del Naomi[0]
            Ken.pop()
        else:
            del Naomi[0]
            del Ken[0]
            wins += 1      
    return wins



if __name__ == "__main__":
    infile = open("sample.in",'r')
    outfile = open("sample.out",'w')
    tests = int(infile.readline().strip())
    for test in range(tests):
        outfile.write('Case #' + str(test+1) + ': ')
        d, w = warGames(infile)
        outfile.write(str(d) + ' ' + str(w) + '\n')
    infile.close()
    outfile.close()
