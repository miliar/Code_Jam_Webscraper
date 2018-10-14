'''
Created on 06/05/2011

@author: Shinjidev
'''
class RobotMove():
    
    def __init__(self, robot, pos):
        self.robot = robot
        self.pos = pos
        
    def __eq__(self,other):
        return (self.robot == other.robot) and (self.pos == other.pos)
    
    def __repr__(self):
        return 'RobotMove(%s,%d)' % (self.robot, self.pos)
        
def findNextMoveRobot(lRobots, kind, start):
    i = start
    while i < len(lRobots):
        if lRobots[i].robot == kind:
            return lRobots[i]
        i+=1
    return None

lRobotMove = []
f = open("A-large.in")
salida = open("outputTestRobot3.txt", "w")
blue = "B"
orange = "O"
nLinea = 0
for line in f:
    print line
    if nLinea > 0:
        times = int(line[:line.find(" ")])
        line = line[line.find(" ") + 1:]
        indice = 1
        while indice < times:
            indice+=1
            robot = line[:line.find(" ")]
            line = line[line.find(" ") + 1:]
            pos = int(line[:line.find(" ")])
            line = line[line.find(" ") + 1:]
            lRobotMove.append(RobotMove(robot,pos))
        robot = line[:line.find(" ")]
        line = line[line.find(" ") + 1:]
        pos = int(line)
        lRobotMove.append(RobotMove(robot,pos))
        #terminamos de agregar los movimientos de los robots
        indiceBlue = 0
        indiceOrange = 0
        posBlue = 1
        posOrange = 1
        tiempo = 0
        while True:
            nextPosBlue = findNextMoveRobot(lRobotMove, blue, indiceBlue) 
            nextPosOrange = findNextMoveRobot(lRobotMove, orange, indiceOrange)
#            print posBlue, nextPosBlue, posOrange, nextPosOrange
            if (not nextPosBlue is None) and (not nextPosOrange is None):
                indexRobotBlue = lRobotMove.index(nextPosBlue, indiceBlue)
                indexRobotOrange = lRobotMove.index(nextPosOrange, indiceOrange)
                if indexRobotBlue < indexRobotOrange:
                    while True:
                        tiempo+=1
                        if posBlue != nextPosBlue.pos:
                            if posBlue < nextPosBlue.pos:
                                posBlue+=1
                            else:
                                posBlue-=1
                        else:
                            #presiona el boton
                            if posOrange != nextPosOrange.pos:
                                if posOrange < nextPosOrange.pos:
                                    posOrange+=1
                                else:
                                    posOrange-=1
                            break
                        if posOrange != nextPosOrange.pos:
                            if posOrange < nextPosOrange.pos:
                                posOrange+=1
                            else:
                                posOrange-=1
                    indiceBlue = indexRobotBlue + 1
                else:
                    while True:
                        tiempo+=1
                        if posOrange != nextPosOrange.pos:
                            if posOrange < nextPosOrange.pos:
                                posOrange+=1
                            else:
                                posOrange-=1
                        else:
                            #presiona el boton
                            if posBlue != nextPosBlue.pos:
                                if posBlue < nextPosBlue.pos:
                                    posBlue+=1
                                else:
                                    posBlue-=1
                            break
                        if posBlue != nextPosBlue.pos:
                            if posBlue < nextPosBlue.pos:
                                posBlue+=1
                            else:
                                posBlue-=1
                    indiceOrange = indexRobotOrange + 1
            elif nextPosOrange is None and (not nextPosBlue is None):
                indexRobotBlue = lRobotMove.index(nextPosBlue, indiceBlue)
                while True:
                    tiempo+=1
                    if posBlue != nextPosBlue.pos:
                        if posBlue < nextPosBlue.pos:
                            posBlue+=1
                        else:
                            posBlue-=1
                    else:
                        break
                indiceBlue = indexRobotBlue + 1
            elif nextPosBlue is None and (not nextPosOrange is None):
                indexRobotOrange = lRobotMove.index(nextPosOrange, indiceOrange)
                while True:
                    tiempo+=1
                    if posOrange != nextPosOrange.pos:
                        if posOrange < nextPosOrange.pos:
                            posOrange+=1
                        else:
                            posOrange-=1
                    else:
                        break
                indiceOrange = indexRobotOrange + 1
            else:
                break
        output = "Case #" + str(nLinea) + ": "  + str(tiempo) + "\n"
        salida.write(output)
    nLinea +=1
    lRobotMove = []
f.close()
salida.close()