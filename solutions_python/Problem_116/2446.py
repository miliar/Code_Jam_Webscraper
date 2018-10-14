import sys

f = open('A-large.in')
output=open('output.txt','w')
cases = int(f.readline())

for t in range(cases):
    filled=True
    board=[-1]*16
    for x in range(4):
        line=f.readline();
        for y in range(4):
            board[x+y*4]=line[y:y+1]
            if board[x+y*4]=='.':
                filled=False
    #print board
    winner="none"
    
    diag1=[0,5,10,15]
    diag2=[3,6,9,12]
    poss=[0,0]# X, O
    for x in diag1:
        if board[x]=='X':
            poss[0]+=1
        elif board[x]=='O':
            poss[1]+=1
        elif board[x]=='T':
            poss[0]+=1
            poss[1]+=1
        else:
            break
    if poss[0]==4:
        winner='X'
    elif poss[1]==4:
        winner='O'
    poss=[0,0]# X, O
    for x in diag2:
        if board[x]=='X':
            poss[0]+=1
        elif board[x]=='O':
            poss[1]+=1
        elif board[x]=='T':
            poss[0]+=1
            poss[1]+=1
        else:
            break
    if poss[0]==4:
        winner='X'
    elif poss[1]==4:
        winner='O'

        
    if winner == 'none':
        for x in range(4):
            poss=[0,0]# X, O
            for y in range(0,4):
                if board[x+y*4]=='X':
                    poss[0]+=1
                elif board[x+y*4]=='O':
                    poss[1]+=1
                elif board[x+y*4]=='T':
                    poss[0]+=1
                    poss[1]+=1
                else:
                    break
            if poss[0]==4:
                winner='X'
                break
            elif poss[1]==4:
                winner='O'
                break
    
    if winner == 'none':
        for x in range(4):
            poss=[0,0]# X, O
            for y in range(0,4):
                if board[y+x*4]=='X':
                    poss[0]+=1
                elif board[y+x*4]=='O':
                    poss[1]+=1
                elif board[y+x*4]=='T':
                    poss[0]+=1
                    poss[1]+=1
                else:
                    break
            if poss[0]==4:
                winner='X'
                break
            elif poss[1]==4:
                winner='O'
                break
    
               
    if winner=='none' and filled == True:
        output.write('Case #'+str(t+1)+': Draw\n')
    elif winner=='none' and filled == False:
        output.write('Case #'+str(t+1)+': Game has not completed\n')
    else:
        output.write('Case #'+str(t+1)+': '+str(winner)+' won\n')
    f.readline()#for random empty line
f.close()
output.close()
