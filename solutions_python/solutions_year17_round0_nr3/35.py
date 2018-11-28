from sys import stdin, stdout

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, self.K = (int(_) for _ in stdin.readline().split())

    def output(self, caseIndex) :
        stdout.write("Case #%d: %d %d\n" % (caseIndex, self.d1, self.d2))

    def calculate(self) :
        numLst = [self.N]
        numCnt = [1]
        totalCnt = 1
        remain = self.K
        while remain > totalCnt :
            remain -= totalCnt

            l = len(numLst)
            tmpNumLst = []
            tmpNumCnt = []
            tmpTotalCnt = 0
            for i in range(l) :
                num = numLst[i]
                count = numCnt[i]
                n2 = int((num - 1) / 2)
                n1 = num - 1 - n2
                if len(tmpNumLst) == 0 or tmpNumLst[-1] != n1 :
                    tmpNumLst.append(n1)
                    tmpNumCnt.append(count)
                else :
                    tmpNumCnt[-1] += count
                tmpTotalCnt += count

                if tmpNumLst[-1] != n2 :
                    tmpNumLst.append(n2)
                    tmpNumCnt.append(count)
                else :
                    tmpNumCnt[-1] += count
                tmpTotalCnt += count

            numLst = tmpNumLst
            numCnt = tmpNumCnt
            totalCnt = tmpTotalCnt

        l = len(numLst)
        for i in range(l) :
            if remain <= numCnt[i] :
                choosen = numLst[i]
                break
            remain -= numCnt[i]

        self.d2 = int((choosen - 1) / 2)
        self.d1 = choosen - 1 - self.d2

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)


