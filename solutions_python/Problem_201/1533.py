import math

def ratioList(lst):
    out = {}
    for i in lst:
        val = i
        count = lst[i]
        if val%2 == 0:
            v1 = val//2
            v2 = v1-1
            if v1 in out:
                out[v1]+= count
            else:
                out[v1] = count
            if v2 in out:
                out[v2]+= count
            else:
                out[v2] = count
        else:
            v1 = val//2
            if v1 in out:
                out[v1]+= count*2
            else:
                out[v1] = count*2
    return out

class TestCase():
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def solve(self):
        base = self.n
        n = self.k
        dct = []
        olddct = {base:1}
        for i in range(int(math.log(base, 2))+2):
            olddct = ratioList(olddct)
            dct += [olddct]


        pos = n - 2**int(math.log(n, 2) )

        dct = dct[int(math.log(n, 2))]
        vals = []
        for i in dct:
            vals.append(i)
        vals.sort()
        if len(vals) == 1:
            return str(vals[0]) + " " + str(vals[0])
        big = 0
        small = 0
        if dct[vals[1]] > pos:
            big = vals[1]
            if dct[vals[1]] > pos + 2**int(math.log(n, 2) ):
                small = vals[1]
            else:
                small = vals[0]
        else:
            big = vals[0]
            small = vals[0]
        return str(big) + " " + str(small)
            

def loadTestCases(path):
    out = []
    input_file = open(path)
    for i in range(int(input_file.readline())):
        lst = input_file.readline().split()
        out.append(TestCase(int(lst[0]), int(lst[1])))
    input_file.close()
    return out

def solveC():
    path = "C-small-2-attempt0.in"
    tcs = loadTestCases(path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        print(str(count)+"solved")
        count += 1
    output_file.close()

solveC()
