'''
Created on Apr 13, 2013

@author: Saravanan
'''
XWON =  "X won"
OWON =  "O won"
DRAW =  "Draw"
NORES = "Game has not completed"
#LOOKUP= {'X':1,'O':2,'T':0,'.':-1}
def count_tok(t,token):
    count = 0
    for c in t:
        if c == token or c == 'T':
            count = count+1  
    return count
def wins(t):
    for y in t:
        if count_tok(y, 'X') == 4:
            return XWON
        elif count_tok(y, 'O') == 4:
            return OWON
    return None

with open('input.in') as f:
    lines = f.readlines()
with open('output.out', 'w') as output:
    N = int(lines[0])
    c=1
    for tc in range(N):
        s1=[
           lines[c],
           lines[c+1],
           lines[c+2],
           lines[c+3]
           ]
        t=[]
        #check game is not over and build a matrix
        completed = True
        for item in s1:
            t2=[]
            if '.' in item:
                completed = False
            for x in item.strip():
                t2.append(x)
            t.append(t2)
        
        RES = wins(t) # chk row wise winning.  
        if RES == None :
            tt = zip(*t) # zip to switch rows to col.. i.e to check col wise win
            RES = wins(tt)
        if RES == None:
            tt= [ [t[0][0],t[1][1],t[2][2],t[3][3] ],
                  [t[0][3],t[1][2],t[2][1],t[3][0] ]
                 ]
            RES = wins(tt)
        if RES == None:
            if completed:
                RES = DRAW
            else:
                RES = NORES
        c=c+5
        print RES
        output.write("Case #%d: %s\n" % (tc+1, RES) )
