'''
Created on Apr 13, 2013

@author: wilson
'''        

def varify_row(row):
    ans = {'X':0,'O':0,'T':0}    
    for item in row:    
        try:
            ans[item] += 1
        except KeyError:
            return False
    
    if ans['T'] == 0:
        if ans['X'] == 4:
            return 'X'
        elif ans['O'] == 4:
            return 'O'                 
    elif ans['T'] == 1:
        if ans['X'] == 3:
            return 'X'
        elif ans['O'] == 3:
            return 'O'
    else:
        return False
    
def something(items):
    for item in items:
        something_else = varify_row(item)
        if something_else:
            return something_else

    return False
                                                   
def get_result(rows):    
    cols = 4
    #check rows
    ans = something(rows)
    if ans: return ans + " won"                     
    #check columns
    columns = [[row[col] for row in rows] for col in range(cols)]    
    ans = something(columns)
    if ans: return ans + " won"            
    #check diagnols
    diagnols = [[rows[col][col] for col in range(cols)],[rows[col][cols-1-col] for col in range(cols)]]        
    ans = something(diagnols)
    if ans: return ans + " won"                 
    #Game has not completed
    for row in rows:
        if '.' in row:
            return  "Game has not completed"
        
    return  "Draw"

def TicTacTomekHelper(board_tuple):
    test, board = board_tuple
    output_file.write("Case #" +  str(test+1) +": " + get_result(board) + "\n")

input_file = open('../input/TicTacToeTomek/A-large.in')
output_file = open('output.txt', 'w+')
tests = int(input_file.readline())

lines = input_file.readlines()
rows = map(lambda line: [char for char in line][:-1],lines)
rows = [row for row in rows if row!=[]]
boards = [rows[n:n+4] for n in range(0, len(rows), 4)]        
map(TicTacTomekHelper, enumerate(boards))             
                
