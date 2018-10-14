import math
class TestCase():
    def __init__(self, s, k):
        self.s = s
        self.k = k

    def solve(self):
        boolLst = []
        for c in self.s:
            if c == "-":
                boolLst.append(True)
            elif c == "+":
                boolLst.append(False)
        flipcount = 0
        for i in range(len(boolLst)):
            if boolLst[i]:
                if i + self.k > len(boolLst):
                    return "IMPOSSIBLE"
                self.flip(boolLst, i)
                flipcount += 1
        return str(flipcount)

    def flip(self, boolLst, pos):
        for i in range(pos, pos+self.k):
            boolLst[i] = not boolLst[i]
            
            

def loadTestCases(path):
    out = []
    input_file = open(path)
    for i in range(int(input_file.readline())):
        lst = input_file.readline().split()
        out.append(TestCase(lst[0], int(lst[1])))
    input_file.close()
    return out

def solveAtest():
    path = "A-test.in"
    tcs = loadTestCases(path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        print(str(count)+"solved")
        count += 1
    output_file.close()

def solveAsmall():
    path = "A-small-attempt0.in"
    tcs = loadTestCases(path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        print(str(count)+"solved")
        count += 1
    output_file.close()

def solveAlarge():
    path = "A-large.in"
    tcs = loadTestCases(path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        print(str(count)+"solved")
        count += 1
    output_file.close()
        
solveAlarge()
