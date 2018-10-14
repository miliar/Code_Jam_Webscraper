import math
import copy


class Stage():
    def __init__(self, N):
        self.score = 0
        self.dimension = N
        self.stage = [['.']*N for x in range(N)]

        self.stage_pluses = [[False for x in range(N)] for y in range(N)]
        self.stage_xes = [[False for x in range(N)] for y in range(N)]

        self.stage_plus = [[True for x in range(N)] for y in range(N)]
        self.stage_x = [[True for x in range(N)], [True for y in range(N)]]
        
    def countScore(self):
        stage_str = ''.join([''.join(x) for x in self.stage])
        self.score = stage_str.count('+') + stage_str.count('x') + 2*stage_str.count('o')
        return self.score
    
    def update(self, model, x, y):
        self.stage[x][y] = model
        if model in ["+","o"]:
            self.stage_pluses[x][y] = True
            for i in range(-x,self.dimension-x):
                row1 = x+i
                col1 = y+i
                row2 = x+i
                col2 = y-i
                if (col1 >= 0) and (col1 < self.dimension):
                    self.stage_plus[row1][col1] = False
                if (col2 >= 0) and (col2 < self.dimension):
                    self.stage_plus[row2][col2] = False
        if model in ["x","o"]:
            self.stage_xes[x][y] = True
            self.stage_x[0][x] = False
            self.stage_x[1][y] = False
        
        self.countScore()
    def edgesPlus(self):
        for j in range(math.ceil(self.dimension/2)):
            for i in range(j, self.dimension-j):
                if self.stage_plus[j][i]:
                    self.update('+',j,i)
            for i in range(j, self.dimension-j):
                if self.stage_plus[self.dimension-j-1][i]:
                    self.update('+',self.dimension-j-1,i)
            for i in range(j, self.dimension-j):
                if self.stage_plus[i][j]:
                    self.update('+',i,j)
            for i in range(j, self.dimension-j):        
                if self.stage_plus[i][self.dimension-j-1]:
                    self.update('+',i,self.dimension-j-1)
    def greedyX(self):
        for row in range(self.dimension):
            if not self.stage_x[0][row]:
                continue
            for column in range(self.dimension):
                if not self.stage_x[1][column]:
                    continue
                self.update('x',row,column)
                break
    def mergePlusX(self):
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.stage_pluses[row][col] and self.stage_xes[row][col]:
                    self.stage[row][col] = 'o'
                elif self.stage_pluses[row][col]:
                    self.stage[row][col] = '+'
                elif self.stage_xes[row][col]:
                    self.stage[row][col] = 'x'
                else:
                    pass


if __name__ == "__main__":
    modelinput = 'D-large.in'
    modeloutput = 'D-large.out'

    inputlines = []
    with open(modelinput, 'r') as f:
        inputlines = f.readlines()

    numcases = int(inputlines.pop(0))

    with open(modeloutput,'w') as f:
        for casenum in range(numcases):
            print('Case '+str(casenum+1))
            case = inputlines.pop(0)
            N = int(case.split()[0])
            M = int(case.split()[1])

            init_stage = Stage(N)
            for y in range(M):
                placement = inputlines.pop(0)
                model = placement.split()[0]
                x = int(placement.split()[1])
                y = int(placement.split()[2])
                init_stage.update(model,x-1,y-1)
            best_stage = copy.deepcopy(init_stage)
            best_stage.edgesPlus()
            best_stage.greedyX()
            best_stage.mergePlusX()
            best_stage.countScore()

            updates = []
            for row in range(N):
                for col in range(N):
                    if best_stage.stage[row][col] == 'o':
                        if init_stage.stage[row][col] != 'o':
                            updates.append('o '+str(row+1)+' '+str(col+1)+'\n')
                    elif best_stage.stage[row][col] == '+':
                        if init_stage.stage[row][col] != '+':
                            updates.append('+ '+str(row+1)+' '+str(col+1)+'\n')
                    elif best_stage.stage[row][col] == 'x':
                        if init_stage.stage[row][col] != 'x':
                            updates.append('x '+str(row+1)+' '+str(col+1)+'\n')

            strtowrite = 'Case #'+str(casenum+1)+": "+str(best_stage.score)+" "+str(len(updates))+"\n"
            f.write(strtowrite)
            
##            for row in range(N):
##                f.write(''.join(init_stage.stage[row])+'\n')
##            f.write('----------'+'\n') 
##            for row in range(N):
##                f.write(''.join(best_stage.stage[row])+'\n')
            
            for u in updates:
                f.write(u)

