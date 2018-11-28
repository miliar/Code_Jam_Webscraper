
class TestCase():
    def __init__(self):
        pass

    
class TestCaseB(TestCase):
    def __init__(self, n):
        self.n = n

    def solve(self):
        s = str(self.n)
        for i in range(1, len(s)):
            
            if(not s[-1-i] == "0"):
                if self.isTidy(int(s)):
                    return int(s)
                s = s[:-1-i] + chr(ord(s[-1-i])-1) + i*"9"
        return int(s)
            
    def isTidy(self, n):
        s = str(n)
        if(len(s)==1):
            return True
        for i in range(1, len(s)):
            if ord(s[i]) < ord(s[i-1]):
                return False
        return True
            


def loadTestCases(taskChar, path):
    out = []
    input_file = open(path)
    for i in range(int(input_file.readline())):
        if(taskChar == "A"):
            pass
        elif(taskChar == "B"):
            out.append(TestCaseB(int(input_file.readline())))
        elif(taskChar == "C"):
            pass
        elif(taskChar == "D"):
            pass
        else:
            print("Error!")
    input_file.close()
    return out

def solveBtest():
    path = "B_test.in"
    tcs = loadTestCases("B", path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        count += 1
        
    output_file.close()

def solveBsmall():
    path = "B-small-attempt0.in"
    tcs = loadTestCases("B", path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        count += 1
        
    output_file.close()
        

def solveBlarge():
    path = "B-large.in"
    tcs = loadTestCases("B", path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        count += 1
        
    output_file.close()
        
solveBlarge()

    
