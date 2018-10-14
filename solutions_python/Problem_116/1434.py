'''
Created on 19-Apr-2012

@author: gurpreet
'''

def check_success_for_(tag, line):
    if line.count(tag) == 4 or (line.count(tag) == 3 and 'T' in line):
        return True
    else:
        return False

if __name__ == '__main__':
#    file = open("../input/1.in")
#    ofile = open("../input/1.ou", 'w+')
#    file = open("../input/A-small-practice.in")
#    ofile = open("../input/A-small-practice.ou", 'w+')
    file = open("../input/A-large.in")
    ofile = open("../input/A-large.ou", 'w+')
    
    lineNo = int(file.readline())
    
    lineCounter = 1
    while lineCounter <= lineNo:
        if lineCounter > 1:
            print 'New Game: ' + file.readline()
        winner = 'Draw'
        count = 0
        lines = {}
        while count < 4:
            line = file.readline()
            print line#            if check_success_for_('X', line):
#                winner = 'X'
#                break
#            if check_success_for_('O', line):
#                winner = 'O'
#                break
            lines[count] = line
            if '.' in line:
                winner = 'Game has not completed'
            
            count = count + 1
            
        if (winner != 'X' and winner != 'O'):
            line0 = lines[0]
            line1 = lines[1]
            line2 = lines[2]
            line3 = lines[3]
    
            lines[4] = line0[0] + line1[0] + line2[0] + line3[0]
            lines[5] = line0[1] + line1[1] + line2[1] + line3[1]
            lines[6] = line0[2] + line1[2] + line2[2] + line3[2]
            lines[7] = line0[3] + line1[3] + line2[3] + line3[3]
            lines[8] = line0[0] + line1[1] + line2[2] + line3[3]
            lines[9] = line0[3] + line1[2] + line2[1] + line3[0]
            
            i = 0
            while i < 10:
                if check_success_for_('X', lines[i]):
                    winner = 'X'
                    break
                if check_success_for_('O', lines[i]):
                    winner = 'O'
                    break
                i += 1
                
        outcome = ''    
        if (winner == 'X' or winner == 'O'):
            outcome = 'Case #' + str(lineCounter) +': '+ winner + ' won'
        else:
            outcome = 'Case #' + str(lineCounter) +': '+ winner
        
        print outcome
        ofile.write(outcome + '\n')
        lineCounter = lineCounter + 1
