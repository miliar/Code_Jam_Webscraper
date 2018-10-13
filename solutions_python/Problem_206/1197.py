class horse:
    def __init__(self, position ,velocity, finishLine):
        self._pos = position
        self._vel = velocity
        self._fl = finishLine
        self._time = (finishLine-position)/velocity
    def __repr__(self):
        return "#"+str(self._pos) + "'" + str(self._vel) + "'" + str(self._time) + "#" 

def solve(horses, finishLine):
    maxTime = horses[0]._time
    for i in horses:
        if i._time > maxTime:
            maxTime = i._time
    return finishLine/maxTime

def horsesLines(lines, finish):
    horses = ()
    for i in lines:
        info = i.split()
        pos = eval(i[0])
        vel = eval(i[1])
        horses = horses + (horse(pos, vel, finish),)
        

def openFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()  
    return lines

def do(filename):
    lines = openFile(filename)
    sol = solvelines(lines)
    file = open("solution" + filename, "w")
    file.write(sol)
    file.close
    
def solvelines(lines):
    n = eval(lines[0])
    lines = lines[1:]
    count = len(lines)
    string = ""
    for i in range(n):
        head = lines[0].split()
        finish = eval(head[0])
        horsenum = eval(head[1])
        lines = lines[1:]
        horses = horsesLines(lines[:horsenum], finish)
        lines = lines[horsenum:]
        string = string + "Case #" + str(i+1) + ": " + str(solve(horses, finish)) + "\n"
        print((i/count)*100)
    return string

