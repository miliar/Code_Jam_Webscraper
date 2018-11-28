'''
Created on 11/04/2014

@author: Javier
'''


fileN = "A-small-attempt0.in";

inpF = open(fileN, "r")

board = {}
totalCases = -1
currentB = 0

for line in inpF:
    line = line.strip()
    
    if totalCases == -1:
        totalCases = int(line)
        #print "Define test cases: " + str(totalCases)
        continue;
    
    else:
        
        data = line.split(" ")

        #print "Current: " + str(currentB)
        
        if len(data) == 1:
            
            if currentB in board:
                #print "Row q2 " + data[0]
                board[currentB]['row2'] = int(data[0])
                continue;
            
            inputData = {
                         'row1': int(data[0]),
                         'd': {
                               '1': [],
                               '2': [],
                         },
                         'row2': -1,
            }
            board[currentB] = inputData
            #print "Row q1 " + data[0]
            
        elif len(data) == 4:
            #print board
            
            dataIn = '1'
            if board[currentB]['row2'] != -1:
                dataIn = '2'
            
            
            currentR = len(board[currentB]['d'][dataIn]) - 1
            if(currentR == -1):
                currentR = 0
            
            #print "+" + str(currentR)
            
            tmpList = []
            for intD in data:
                tmpList.append(int(intD))
            
            board[currentB]['d'][dataIn].append(tmpList)
            
            if dataIn != '1' and len(board[currentB]['d'][dataIn]) == 4:
                currentB += 1
                #print "HERE"*5
            
            #print board[currentB]['d'][currentR]
        
        #print data;


#analize inputs
for case in board:
    status = "Volunteer cheated!"
    common = []
    row1 = board[case]['row1'] - 1
    row2 = board[case]['row2'] - 1
    
    for poss in board[case]['d']['1'][row1]:
        if poss in board[case]['d']['2'][row2]:
            common.append(poss)
    
    if len(common) == 1:
        status = str(common[0])
    elif len(common) > 1:
        status = "Bad magician!"
    
    print "Case #" + str(case + 1) + ": " + status