import numpy as np
filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round Qualification\\D\\D-small-attempt3"


fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())


class Board:
    def __init__(self, n):
        self.count = 0
        self.n, self.models = n, {}
    def add(self, ij):
        self.models[self.count] = ij
        self.count += 1
    def removelast(self):
        del self.models[self.count-1]
        self.count -= 1
    def size(self):
        return self.n
    def getmodels(self):
        return dict(self.models)
    def score(self):
        return self.count
    def avail(self, ij):
        return not ij in self.models.values()
    def comparetoold(self, oldbr):
        ch = []
        for j in range(oldbr.score(), self.count):
            ch.append(self.models[j])
        return ch[:]
    def move(self, i, to):
        self.models[i] = to
    def copy(self):
        cp = Board(self.n)
        cp.models = dict(self.models)
        cp.count = self.count
        return cp
        
def collisioncount(board, i):
    cnt = 0
    models = board.getmodels()
    if i == -1:
        for k in range(0, board.score() - 1):
            for j in range(k+1, board.score()):
                if (models[k][0]+models[k][1] == models[j][0]+models[j][1] 
                    or models[k][0]-models[k][1] == models[j][0]-models[j][1]):
                    cnt += 1
    else:
        for j in range(0, i) + range(i+1, board.score()):
            if (models[i][0]+models[i][1] == models[j][0]+models[j][1] 
                or models[i][0]-models[i][1] == models[j][0]-models[j][1]):
                cnt += 1
    return cnt

def generateRandomPBoard(board): ##???
    for j in range(board.size()):
        if board.avail((0,j)):
            board.add((0,j))
    for j in range(1, board.size()-1):
        board.add((board.size()-1, j))

def generateRandomXBoard(board):
    num = board.size() - board.score()
    rowsnotused, colsnotused = [el[0] for el in board.getmodels().values()], [el[1] for el in board.getmodels().values()]
    rowsnotused, colsnotused = [i for i in range(board.size()) if not i in rowsnotused], [i for i in range(board.size()) if not i in colsnotused]
    colsnotused = np.random.permutation(colsnotused)
    toadd = zip(rowsnotused, colsnotused)
    for i in range(num):
        board.add(toadd[i])
        
def optimizePBoard(donttouch, board):
    newcount = collisioncount(board, -1)
    oldcount = newcount

    while oldcount > 0:    
        colls = range(donttouch, board.score())
        model = sorted(colls, key = lambda x: -collisioncount(board, x))[0]
        pos = board.getmodels()[model]
        newcollisions = []
        
        for i in range(board.size()):
            if board.avail((i, pos[1])):
                board.move(model, (i, pos[1]))
                newcollisions.append(((i, pos[1]), collisioncount(board, model)))
                board.move(model, pos)
        for j in range(board.size()):
            if board.avail((pos[0], j)):
                board.move(model, (pos[0], j))
                newcollisions.append(((pos[0], j), collisioncount(board, model)))
                board.move(model, pos)
                
        newcollisions = sorted(newcollisions, key = lambda x: x[1])
        board.move(model, newcollisions[0][0])
        newcount = collisioncount(board, -1)
        if newcount >= oldcount:
            break
        oldcount = newcount
        
    return (newcount == 0)
    
    
def tryaddps(board):
    while True:
        added = 0
        for i in range(board.size()):
            for j in range(board.size()):
                if board.avail((i,j)):
                    board.add((i,j))
                    if collisioncount(board, board.score()-1) != 0:
                        board.removelast()
                    else:
                        added += 1
        if added == 0:
            break
    

def mergechanges(chp, chx, olp, olx):
    dic = {}
    for el in chp:
        if el in olx.values():
            dic[el] = 'o'
        else:
            dic[el] = '+'
    for el in chx:
        if el in dic.keys() + olp.values():
            dic[el] = 'o'
        else:
            dic[el] = 'x'
    return dict(dic)

def visualize(i, boardp, boardx):
    f = open(filename+'v'+'0'*(3-len(str(i+1)))+str(i+1)+".txt","w")
    arr = [['.' for i in range(boardp.size())] for j in range(boardp.size())]
    for el in boardp.getmodels().values():
        arr[el[0]][el[1]] = '+'
    for el in boardx.getmodels().values():
        if arr[el[0]][el[1]] != '.':
            arr[el[0]][el[1]] = 'o'
        else:
            arr[el[0]][el[1]] = 'x'
    for i in range(boardp.size()):
            f.write("".join(arr[i])+"\n")
    f.close()



for T in xrange(trials):

    n, m = map(int, fin.readline().split(' '))
    boardp, boardx, oldbrp, oldbrx = Board(n), Board(n), Board(n), Board(n)
    
    for i in range(m):
        tmp = fin.readline().strip().split(' ')
        char, [i, j] = tmp[0], map(int, tmp[1:])
        if char != 'x':
            boardp.add((i-1, j-1))
            oldbrp.add((i-1, j-1))
        if char != '+':
            boardx.add((i-1, j-1))
            oldbrx.add((i-1, j-1))
    
    generateRandomPBoard(boardp)
    generateRandomXBoard(boardx)
    #print boardp.getmodels()

    #while collisioncount(boardp, -1) > 0:
    #    if not optimizePBoard(oldbrp.score(), boardp):
    #        #print collisioncount(boardp, -1)
    #        boardp = oldbrp.copy()
    #        generateRandomPBoard(boardp)
    #    else:
    #        break
    tryaddps(boardp)
    #print collisioncount(boardp, -1)
    
    changep, changex = boardp.comparetoold(oldbrp), boardx.comparetoold(oldbrx)    
    changes = mergechanges(changep, changex, oldbrp.getmodels(), oldbrx.getmodels())

    fout.write("Case #{0}: {1} {2}\n".format(T+1,boardp.score() + boardx.score(), len(changes)))
    for el in changes.keys():
        fout.write(changes[el]+" {0} {1}\n".format(el[0]+1, el[1]+1))
    #visualize(T, boardp, boardx)
    print "Case {0} done".format(T+1)
                    
fin.close()
fout.close()