'''
Created on Apr 12, 2014

@author: Ardi
'''
from MagicTricksSolver import MagicTricksSolver       

if __name__ == '__main__':
    iFilename = 'A-small-attempt0.in'
    lines = []
    
    with open('C:\\Users\\Ardi\\Geekery\\CodeJam2014\\input\\' + iFilename, 'r') as f:
        for line in f:        
            lines.append(line.rstrip('\n'))
    f.close()
    
    #print(lines)
    
    testNum = int(lines[0])    
    t = 0
    
    oFilename = 'A-small-attempt0.out'    
    with open('C:\\Users\\Ardi\\Geekery\\CodeJam2014\\output\\' + oFilename, 'w') as f:
        while (t < testNum):
            i = (t*10)+1
            choice1 = int(lines[i])
            cards1 = [[int(card) for card in row.split(' ')] for row in lines[i+1:i+5]]
            #print(cards1)      
            choice2 = int(lines[i+5])
            cards2 = [[int(card) for card in row.split(' ')] for row in lines[i+6:i+10]]
            #print(cards2)
            
            mts = MagicTricksSolver(choice1, cards1, choice2, cards2)
            #mts._getSetFromChoice(choice1, cards1)
            #mts._getSetFromChoice(choice2, cards2)
            output = mts.solve()
            print('Case #{0}: {1}'.format(str(t+1),output))
            lnOut = 'Case #{0}: {1}'.format(str(t+1),output)
            if t+1 < testNum:
                lnOut += '\n'
            f.write(lnOut)
            t += 1
    f.close()
    