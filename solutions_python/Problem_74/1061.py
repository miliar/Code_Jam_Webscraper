import sys
import math

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename,'r')
    t = int(f.readline())
    
    for i in range(t):
        input_line = f.readline()
        commands = input_line.split(' ')
        n = int(commands[0])
        del(commands[0]);
        timerO=0
        timerB=0
        bseqO = [1,]
        bseqB = [1,]
        for j in range(n):
            robot = commands[2*j]
            button = int(commands[2*j+1])
            if (robot == 'O'):
                timerO = timerO + int(math.fabs(button-bseqO[-1])) + 1
                if(timerO > timerB):
                    pass
                else:
                    timerO = timerB+1
                bseqO.append(button)
            else:
                timerB = timerB + int(math.fabs(button-bseqB[-1])) + 1
                if(timerB > timerO):
                    pass
                else:
                    timerB = timerO+1
                bseqB.append(button)
        print "Case #%d: %d"%(i+1,max(timerO,timerB))
                    
        
