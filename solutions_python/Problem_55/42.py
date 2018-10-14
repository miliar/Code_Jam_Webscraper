#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
import operator

__author__="Shahar"
__date__ ="$08-May-2010 09:16:14$"

def RollerCoaster(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    T = int(fin.readline())
    for iT in xrange(T):
        numbers = fin.readline().rstrip('\n').split(' ')
        R = int(numbers[0])
        k = int(numbers[1])
        N = int(numbers[2])
        numbers = fin.readline().rstrip('\n').split(' ')
        g = map(int, numbers[:N])
        #print 'R: ' + str(R) + ' k: ' + str(k) + ' N: ' + str(N)
        #print 'g: ' + str(g)
        gVisited = {}
        Pay = [0]
        firstG = 0
        while firstG not in gVisited :
            gVisited[firstG] = len(Pay)-1
            currFill = 0
            currG = firstG
            while True :
                if (currFill + g[currG] > k) :
                    break;
                currFill += g[currG]
                currG = (currG + 1) % N
                if (currG == firstG) :
                    break
            firstG = currG
            Pay.append(currFill)
        roundStart = gVisited[firstG]
        #print 'Pay: ' + str(Pay) + ' roundStart: ' + str(roundStart)
        
        startPay = [0]
        for P in Pay[1:roundStart+1] :
            startPay.append(startPay[-1]+P)
        #print 'startPay: ' + str(startPay)

        roundPay = [0]
        for P in Pay[roundStart+1:] :
            roundPay.append(roundPay[-1]+P)
        #print 'roundPay: ' + str(roundPay)

        roundLen = len(roundPay)-1

        if (R > roundStart) :
            Radj = R - roundStart
            TotalPay = startPay[-1] + roundPay[-1]*(Radj//roundLen)+roundPay[Radj%roundLen]
        else :
            TotalPay = startPay[R]

        text = 'Case #' + str(iT+1) + ': ' + str(TotalPay)
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #RollerCoaster(sys.argv[1]);
    #RollerCoaster('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\C-test.in');
    #RollerCoaster('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\C-small-attempt0.in');
    #RollerCoaster('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\C-small-attempt1.in');
    RollerCoaster('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\C-large.in');

