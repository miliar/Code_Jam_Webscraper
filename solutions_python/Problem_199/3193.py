class pancake:
    _status = "+"
    def __init__(self, status="+"):
        if not status in ("+", "-"):
            raise ValueError("not a pancake")
        self._status = status
        
    def __repr__(self):
        return self._status
    
    def flip(self):
        if (self._status == "+"):
            self._status = "-"
        else:
            self._status = "+"
            
class stove:
    _size = 0
    _pancakes = ()
    def __init__(self, size):
        self._size = size
        for i in range(size):
            self._pancakes = self._pancakes + (pancake(),)
            
    def __repr__(self):
        return self.toString()

    def toString(self):
        ret = ""
        for i in range(self._size):
            ret = ret+ self._pancakes[i]._status
        return ret        
    
    def setPancake(self, pos, stat):
        self._pancakes[pos]._status = stat
        
    def flip(self, position, size):
        if(position + size > self._size):
            raise ValueError("spatula too big or out of place")
        for i in range(size):
            j = i+position
            self._pancakes[j].flip()
            
    def isSolved(self):
        return self.toString() == "+"*self._size

def solvelines(lines):
    n = eval(lines[0])
    lines = lines[1:]
    string = ""
    for i in range(len(lines)):
        string = string + "Case #" + str(i+1) + ": " + solutionText(lines[i]) + "\n"
    return string

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

def solutionText(line):
    if line[-1] == "\n":
        line = line[:-1]
    new = "('"
    for i in line:
        if (i==" "):
            new = new + "', "
        else:
            new = new + i
    new = new + ")"
    r = eval(new)
    stringS = r[0]
    spatula = r[1]
    return str(solve(stringS, spatula))


def stringStove(string):
    s = stove(len(string))
    for i in range(len(string)):
        s.setPancake(i, string[i])
    return s

def copyStove(stov):
    return stringStove(stov.toString())

def solve(string, spatula):
    stov = stringStove(string)
    return bestOf(stov, spatula, 0, 0)

def bestOf(stov, spatula, position, pastmovs):
    if(position+spatula > stov._size):
        return "IMPOSSIBLE"
    s1 = copyStove(stov)
    s2 = copyStove(stov)
    s1.flip(position, spatula)
    if s2.isSolved():
        return pastmovs
    if s1.isSolved():
        return pastmovs+1
    sol1 = bestOf(s1, spatula, position+1, pastmovs+1)
    sol2 = bestOf(s2, spatula, position+1, pastmovs)
    if sol1 == "IMPOSSIBLE":
        return sol2
    elif sol2 == "IMPOSSIBLE":
        return sol1
    else:
        return min(sol1, sol2)