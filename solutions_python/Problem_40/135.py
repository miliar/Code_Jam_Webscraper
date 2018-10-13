import sys, time

class Tree:
    def __init__(self, f):
        c = f.read(1)
        while c.isspace():
            c = f.read(1)
        line = c if c.isdigit() else ''
        c = f.read(1)
        while c != '(' and c != ')':
            line += c
            c = f.read(1)
        line += c
        if line[-1] == ')':
            self.weight = float(line[:-1])
            self.feature, self.lTree, self.rTree = None, None, None
        else:
            self.weight = float(line.split()[0])
            self.feature = line.split()[1]
            self.lTree = Tree(f)
            self.rTree = Tree(f)
            while (f.read(1) != ')'):
                pass
        #print line
        #self.printNode()
        
    def isLeaf(self):
        return self.lTree is None and self.rTree is None
    
    def walk(self, features):
        if self.isLeaf():
            return self.weight
        if self.feature in features:
            return self.weight * self.lTree.walk(features)
        else:
            return self.weight * self.rTree.walk(features)
    
    def printNode(self):
        print "start node"
        print "weight, feature", self.weight, self.feature
        print "end node"
        
def main():
    f = open(sys.argv[1], 'r')
    cases = int(f.readline())
    for case in xrange(1, cases + 1):
        noOfLines = int(f.readline())
        decisionTree = Tree(f)
        l = f.readline()
        noOfAnimals = int(l if not l.isspace() else f.readline())
        print "Case #%d:" % (case)
        for i in xrange(noOfAnimals):
            line = f.readline()
            animal = line.split()[0]
            features = [feature.strip() for feature in line.split()[2:]]
            print "%.7f" % (1.0 * decisionTree.walk(features))

main()
