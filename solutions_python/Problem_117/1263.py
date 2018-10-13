'''
Created on 13-Apr-2012

@author: gurpreet
'''

def check_success_for_(tag, line):
    if line.count(tag) == 4 or (line.count(tag) == 3 and 'T' in line):
        return True
    else:
        return False

                
def get_maxInCol(l, maxInCol):
    count = 0
    for i in l:
        if i > maxInCol[count]:
            maxInCol[count] = i
        count += 1 

    return maxInCol


def _can_mow_lawn(lines, maxInCol, maxInRow):
    row = 0
    for line in lines:
        col = 0
        for c in line:
            if c != maxInRow[row] and c != maxInCol[col]:
                return 'NO'
            col += 1
        row += 1
    
    return 'YES'

if __name__ == '__main__':
#    file = open("../input/B-small.in")
#    ofile = open("../input/B-small.ou", 'w+')
    file = open("../input/B-large.in")
    ofile = open("../input/B-large.ou", 'w+')
    
    lineNo = int(file.readline())
    
    gameCounter = 1
    while gameCounter <= lineNo:
        dimensions = file.readline()
        dimensions = dimensions[:len(dimensions)-1]
        input = dimensions.split(' ')
        lineCounter = int(input[0])
        colCounter = int(input[1])
        counter = 0
        
        maxInRow = {}
        maxInCol = {}
        
        j = 0
        while j < colCounter:
            maxInCol[j] = 0
            j += 1
        
        lines = []
        '''collect data '''
        while counter < lineCounter:
            line = file.readline()
            if '\n' in line:
                line = line[:len(line) - 1]
            print line#
            tuple = line.split(' ')
            l = []
            max = 0
            for c in tuple:
                if int(c) >= max:
                    max = int(c)
                l.append(int(c))
            maxInRow[counter] = max
            
            lines.append(l)
            
            maxInCol = get_maxInCol(l, maxInCol)            
            counter += 1
            
        ''' process data'''    
        outcome =  _can_mow_lawn(lines, maxInCol, maxInRow)
        
        outcomeStr = 'Case #'+ str(gameCounter) +': '+ outcome
        ofile.write(outcomeStr + '\n')   
        gameCounter += 1        
                            
        
#         print outcome
#        ofile.write(outcome + '\n')   


#            if (winner != 'X' and winner != 'O'):
#                line0 = lines[0]
#                line1 = lines[1]
#                line2 = lines[2]
#                line3 = lines[3]
#        
#                lines[4] = line0[0] + line1[0] + line2[0] + line3[0]
#                lines[5] = line0[1] + line1[1] + line2[1] + line3[1]
#                lines[6] = line0[2] + line1[2] + line2[2] + line3[2]
#                lines[7] = line0[3] + line1[3] + line2[3] + line3[3]
#                lines[8] = line0[0] + line1[1] + line2[2] + line3[3]
#                lines[9] = line0[3] + line1[2] + line2[1] + line3[0]
#                
#                i = 0
#                while i < 10:
#                    if check_success_for_('X', lines[i]):
#                        winner = 'X'
#                        break
#                    if check_success_for_('O', lines[i]):
#                        winner = 'O'
#                        break
#                    i += 1
#                    
#            outcome = ''    
#            if (winner == 'X' or winner == 'O'):
#                outcome = 'Case #' + str(lineCounter) +': '+ winner + ' won'
#            else:
#                outcome = 'Case #' + str(lineCounter) +': '+ winner
#            
#            print outcome
#            ofile.write(outcome + '\n')
