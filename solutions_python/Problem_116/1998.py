__author__ = 'guoyongzhen'

class Player:
    def __init__(self):
        self.col=[0,0,0,0]
        self.line=0
        self.row=0
        self.dia_left=0
        self.dia_right=0
        self.win=False
    def setLine(self,line):
        self.line=line
        self.row=0

    def addSym(self,index):
        self.row+=1
        if self.row==4:
            self.win=True
        self.col[index]+=1
        if 4 in self.col:
            self.win=True
        if index==self.line:
            self.dia_left+=1
            if self.dia_left==4:
                self.win=True
        elif index+self.line==3:
            self.dia_right+=1
            if self.dia_right==4:
                self.win=True
        return self.win

class Board:
    def __init__(self):
        self.empty=0
        self.X=Player()
        self.O=Player()

    def process(self,game):
        for line in range(len(game)):
            line=int(line)
            self.X.setLine(line)
            self.O.setLine(line)
            for index in range(4):
                sym=game[line][index]
                if sym=='.':
                    self.empty+=1
                    continue
                if self.check(sym,index):
                    return self.winner()
        if self.empty>0:
            return 'Game has not completed'
        else:
            return 'Draw'

    def winner(self):
        if self.X.win:
            return 'X won'
        else:
            return 'O won'

    def check(self,symbol,index):
        if symbol=='X':
            self.X.addSym(index)
        elif symbol=='O':
            self.O.addSym(index)
        else:
            self.X.addSym(index)
            self.O.addSym(index)
        return self.X.win or self.O.win

input=file('A-large.in','r')
output=file('A-large.out','w')
result=[]
for case in range(int(input.readline())):
    game=[]
    for line in range(4):
        game.append(input.readline())
    board=Board()
    result.append('Case #%s: %s\r\n'%(case+1,board.process(game)))
    input.readline()
output.writelines(result)
output.close()
input.close()
print result
