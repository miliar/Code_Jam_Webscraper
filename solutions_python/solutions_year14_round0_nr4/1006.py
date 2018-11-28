__author__ = 'Gantmajer_viv'

''' I'm using the numpy library. http://www.numpy.org/ '''

from numpy import array , count_nonzero

def normalGameResult(player1, player2):
    player1Norm = array(player1[:])
    player2Norm = array(player2[:])
    total = 0
    player1Winning = True
    while len(player1Norm):
        n = 0
        if(player1Winning):
            n = count_nonzero(player1Norm > player2Norm.max())
        else:
            n = count_nonzero(player2Norm > player1Norm.max())

        player1Norm = player1Norm[:len(player1Norm) - n]
        if player1Winning:
            player2Norm = player2Norm[n:]
            total += n
        else:
            player2Norm = player2Norm[:len(player2Norm) - n]
        player1Winning = not player1Winning
    return total

def cheatGameResult(player1, player2):
    total = 0
    while len(player1):
        if player1[0] > player2[0]:
            player1.pop(0)
            player2.pop(0)
            total += 1
        else:
            player1.pop(0)
    return total

if __name__ == '__main__':
    inFile = open('D-large.in', 'r')
    numberOfTests = int(inFile.readline())
    outFile = open('D-large.out', 'w')
    for i in range(1, numberOfTests + 1):
        inFile.readline()
        naomiWeights = [float(elem) for elem in inFile.readline().split()]
        kenWeights = [float(elem) for elem in inFile.readline().split()]
        naomiWeights.sort()
        kenWeights.sort()
        normalGameWins = normalGameResult(naomiWeights, kenWeights)
        cheatGameWins = cheatGameResult(naomiWeights, kenWeights)
        outFile.write('Case #%d: %d %d\n' % (i, cheatGameWins, normalGameWins))