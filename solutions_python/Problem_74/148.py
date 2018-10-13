class robot:
    def __init__(self):
        self.pos = 1
        self.time = 0
    def moveforward(self):
        self.pos += 1
        self.time += 1
    def moveback(self):
        self.pos -= 1
        self.time += 1
    def stay(self):
        self.time += 1
    def push(self):
        self.time += 1

def processcase(inlist):
    index = 1
    blue = robot()
    orange = robot()
    while index < len(inlist):
        if inlist[index] == 'O':
            robot1 =orange
            robot2 =blue
        else:
            robot1 = blue 
            robot2 = orange
        butt = int(inlist[index+1])
        while butt != robot1.pos:
            if butt > robot1.pos:
                if robot1.time < robot2.time:
                    t = robot2.time - robot1.time
                    d = butt - robot1.pos
                    if t > d:
                        robot1.pos = butt
                        robot1.time = robot2.time
                        break
                    elif t == d:
                        robot1.pos = butt
                        robot1.time = robot2.time
                        break
                    else:
                        robot1.pos = robot1.pos + t
                        robot1.time = robot2.time
                robot1.moveforward()
            else:
                if robot1.time < robot2.time:
                    t = robot2.time - robot1.time
                    d = robot1.pos - butt
                    if t > d:
                        robot1.pos = butt
                        robot1.time = robot2.time
                        break
                    elif t == d:
                        robot1.pos = butt
                        robot1.time = robot2.time
                        break
                    else:
                        robot1.pos = robot1.pos - t
                        robot1.time = robot2.time
                robot1.moveback()
        if robot1.time < robot2.time:
            robot1.time = robot2.time
            robot1.push()
            index += 2
        else:
            robot1.push()
            index += 2
    return robot1.time   

def inputfilter(filename):
    finput = open(filename,'r')
    fout = open("out.txt",'w')
    casenum = int(finput.readline())
    for i in range(1,casenum+1):
        inlist = finput.readline().split()
        fout.write("Case #"+str(i)+": "+str(processcase(inlist))+'\n')
    finput.close()
    fout.close()
    return None
    
if __name__=="__main__":
    inputfilter("A-large.in")