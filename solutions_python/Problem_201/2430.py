class bathroom:
    _size=0
    _intervals=((0,0),)
    
    def __init__(self, size):
        self._size = size
        self._intervals = ((1,size),)
        
    def sit(self):
        i = self.largeIntervalIndex()
        interval = self._intervals[i]
        isize = interval[1] - interval[0] + 1
        lspace = ((isize/2)-0.5)//1
        rspace = (isize/2)//1
        if(lspace>0 and rspace>0):
            linterval = (interval[0], interval[0]+(lspace-1))
            rinterval = (interval[1]-(rspace-1), interval[1])
            self._intervals = self._intervals[:i] + (linterval,) + (rinterval,) + self._intervals[(i+1):]
        elif(lspace>0):
            linterval = (interval[0], interval[0]+(lspace-1))
            self._intervals = self._intervals[:i] + (linterval,) + self._intervals[(i+1):]
        elif(rspace>0):
            rinterval = (interval[1]-(rspace-1), interval[1])
            self._intervals = self._intervals[:i] + (rinterval,) + self._intervals[(i+1):]
        else:
            self._intervals = self._intervals[:i] + self._intervals[(i+1):]
        return(rspace, lspace)
        
    def largeIntervalIndex(self):
        maxi = 0
        index = 0
        for i in range(len(self._intervals)):
            interval = self._intervals[i]
            if (interval[1] - interval[0]) > maxi:
                maxi = interval[1] - interval[0]
                index = i
        return index

def solve(stalls, guys):
    b = bathroom(stalls)
    for i in range(guys):
        solution = b.sit()
    return solution

def solveline(line):
    if line[-1] == "\n":
        line = line[:-1]
    new = "("
    for i in line:
        if (i==" "):
            new = new + ", "
        else:
            new = new + i
    new = new + ")"
    r = eval(new)
    stalls = r[0]
    guys = r[1]
    solution = solve(stalls, guys)
    return str(int(solution[0])) + " " + str(int(solution[1]))    

def openFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()  
    return lines

def solution(filename):
    lines = openFile(filename)
    n = eval(lines[0])
    lines = lines[1:]   
    count = len(lines)
    string = ""
    for i in range(len(lines)):
        string = string + "Case #" + str(i+1) + ": " + solveline(lines[i]) + "\n"
        print((i/count)*100)  
    file = open("solution" + filename, "w")
    file.write(string)
    file.close