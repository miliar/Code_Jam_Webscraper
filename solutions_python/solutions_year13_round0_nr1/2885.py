def check_Char(inChar):
    if inChar == 'X':
        return 'X'
    if inChar == 'O':
        return 'O'
    if inChar == '.':
        return '.'
    if inChar == 'T':
        return 'T'

def check_Line(inLine):
    graph = {}
    graph['X'] = 0
    graph['O'] = 0
    graph['T'] = 0
    graph['.'] = 0
    for i in inLine:
        result = check_Char(i)
        graph[result] += 1
    return graph

def check_TestCase(four_lines):
    #horizontal line tests
    gH = {}
    for entry in four_lines:
        gH = check_Line(entry)
        if gH['X'] == 4 or (gH['X'] == 3 and gH['T'] == 1):
            return 'X won'
        if gH['O'] == 4 or (gH['O'] == 3 and gH['T'] == 1):
            return 'O won'
        

    #vertical line tests
    firstLine = four_lines[0][0] + four_lines[1][0] + four_lines[2][0] + four_lines[3][0]
    secondLine = four_lines[0][1] + four_lines[1][1] + four_lines[2][1] + four_lines[3][1]
    thirdLine = four_lines[0][2] + four_lines[1][2] + four_lines[2][2] + four_lines[3][2]
    fourthLine = four_lines[0][3] + four_lines[1][3] + four_lines[2][3] + four_lines[3][3]
    new_four_lines = [firstLine, secondLine, thirdLine, fourthLine]
    gV = {}
    for entry in new_four_lines:
        gV = check_Line(entry)
        if gV['X'] == 4 or (gV['X'] == 3 and gV['T'] == 1):
            return 'X won'
        if gV['O'] == 4:
            return 'O won'
        if gV['O'] == 4 or (gV['O'] == 3 and gV['T'] == 1):
            return 'O won'
    
    #diagonal line tests
    diagLine1 = four_lines[0][3] + four_lines[1][2] + four_lines[2][1] + four_lines[3][0]
    diagLine2 = four_lines[0][0] + four_lines[1][1] + four_lines[2][2] + four_lines[3][3]
    g1, g2 = {}, {}
    g1 = check_Line(diagLine1)
    if g1['X'] == 4 or (g1['X'] == 3 and g1['T'] == 1):
          return 'X won'
    if g1['O'] == 4 or (g1['O'] == 3 and g1['T'] == 1):
          return 'O won'
    g2 = check_Line(diagLine2)
    if g2['X'] == 4 or (g2['X'] == 3 and g2['T'] == 1):
          return 'X won' 
    if g2['O'] == 4 or (g2['O'] == 3 and g2['T'] == 1):
          return 'O won'
          
    
    #check if game incomplete
    if gH['.'] != 0 or gV['.'] != 0 or g1['.'] != 0 or g2['.'] != 0:
        return 'Game has not completed'
    else:
        return 'Draw'
        

def tic_tac_toe(inputdata):
    inlist = []
    inlist += inputdata.split()
    numTestCases = (len(inlist)-1)/4
    j = 1
    start, end = 1, 1
    while j <= numTestCases:
        four_lines = inlist[start:end+4]
        if j != numTestCases:
              print "Case #" + str(j) + ": " + check_TestCase(four_lines)
              start, end = end+4, end+4
        j += 1
    return "Case #" + str(numTestCases) + ": " + check_TestCase(four_lines)
