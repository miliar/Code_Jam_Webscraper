import fileinput
import sys

class DTNode:
    def __init__(self, weight, question, yeschild, nochild):
        self.weight = weight
        self.question = question
        self.yeschild = yeschild
        self.nochild = nochild

    def __init__(self, nodes):
        #print "__init__ called", nodes
        if not nodes:
            return

        line = nodes[0].replace("(","").replace(")","").split()
        self.weight = float(line[0])
        if len(line) >= 2:
            self.question = line[1]
            pars = 0
            for i, n in enumerate(nodes[1:]):
                pars += n.count("(") - n.count(")")
                if pars == 0:
                    self.yeschild = DTNode(nodes[1:i+2])
                    self.nochild = DTNode(nodes[i+2:])
                    break
        else:
            self.question = None
            return

    def isCute(self, animal):
        #print "isCute called. weight:", self.weight, "question:", self.question
        if self.question:
            if self.question in animal:
                return self.weight * self.yeschild.isCute(animal)
            else:
                return self.weight * self.nochild.isCute(animal)
        else:
            return self.weight

def processInput():
    tcIn = fileinput.input()
    tcCount = int(tcIn.readline())
    for i in range(tcCount):
        dt = getDt(tcIn)

        print "Case #%d:" % (i+1)
        animalCount = int(tcIn.readline())
        for j in range(animalCount):
            animalFeatures = tcIn.readline().split()[2:]
            print '%0.7f' % dt.isCute(animalFeatures)


def getDt(tcIn):
    dtCount = int(tcIn.readline())
    nodes = []
    for i in range(dtCount):
        nodes.append(tcIn.readline())
    return DTNode(nodes)

def main():
    processInput()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
