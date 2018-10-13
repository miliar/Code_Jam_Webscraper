
def findDest(char,moves):
    for x in moves:
        if(x[0] == char):
            return x[1]
    return -1

def solve(moves):
    turn=moves[0][0]
    Odest=findDest('O',moves)
    Bdest=findDest('B',moves)
    Opos=1
    Bpos=1
    seconds=0
    #print "first: ",Odest,Bdest,Opos,Bpos
    while(Odest!=-1 and Bdest!=-1):
        if(turn == 'X'):
            turn = 'B'
        if(Opos==Odest):
            if(turn=='O'):
                #change players and update dest
                moves.pop(0)
                turn = moves[0][0]
                if(turn=='B'):
                    turn = 'X'
                Odest=findDest('O',moves)
            #otherwise, just wait, don't increment position
        else:
            if(Odest<Opos):
                Opos-=1
            else: 
                Opos+=1
        if(Bpos==Bdest):
            if(turn=='B'):
                #change players and update dest
                moves.pop(0)
                turn=moves[0][0]
                Bdest=findDest('B',moves)
            #otherwise, just wait, don't increment position
        else:
            if(Bdest<Bpos):
                Bpos-=1
            else:
                Bpos+=1
        seconds+=1
        #print turn,Opos,Odest,Bpos,Bdest,seconds
    if(Odest==-1): #DOESNT WORK IF MORE THAN ONE A OR B's TO GO!
        for y,x in enumerate(moves):
            seconds+=abs(x[1]-Bpos)+1
            Bpos=x[1]
    elif(Bdest==-1):
        for y,x in enumerate(moves):
            seconds+=abs(x[1]-Opos)+1
            Opos=x[1]
    return seconds
        

T = int(raw_input())
for i in range(T):
    line = raw_input().split()
    N = int(line[0])
    moves=[]
    for x in range(1,N*2+1,2):
        moves+=[(line[x],int(line[x+1]))]
    seconds=solve(moves)
    print "Case #%d: %d"%(i+1,seconds)
