

class TicTacToeTomek(object):
    def __init__(self, lst):
        self.lst = lst

    def getVertical(self, index):
        return [row[index] for row in self.lst]

    def getHorizontal(self, index):
        return self.lst[index]

    def getDiagLT(self):
        return [self.lst[i][i] for i in range(4)]

    def getDiagRT(self):
        return [self.lst[i][3 - i] for i in range(4)]

    def harvestCheckup(self, l):
        tc = l.count("T")
        oc = l.count("O")
        xc = l.count("X")
        if (oc + tc == 4):
            return "O"
        elif (xc + tc == 4):
            return "X"
        else:
            return None

    def analyse(self):
        for i in xrange(4):
            res = self.harvestCheckup(self.getVertical(i))
            if res: return "{0} won".format(res)
            res = self.harvestCheckup(self.getHorizontal(i))
            if res: return "{0} won".format(res)
        res = self.harvestCheckup(self.getDiagRT())
        if res: return "{0} won".format(res)
        res = self.harvestCheckup(self.getDiagLT())
        if res: return "{0} won".format(res)
        for l in self.lst:
            if l.count("."): return "Game has not completed"
        else:
            return "Draw"



def main(filename):
    q = open(filename, "r")
    cases = int(q.readline().strip())
    result = open("tictactoe_answer.txt", "w")
    for i in xrange(cases):
        lst = []
        for j in xrange(4):
            lst.append(list(q.readline().strip()))
        q.readline()
        ans = TicTacToeTomek(lst).analyse()
        print "Case #{0}: {1}".format(i + 1, ans)
        result.write("Case #{0}: {1}\n".format(i + 1, ans))
    result.close()
    q.close()

import cProfile
cProfile.run("main('tictactoe.txt')")