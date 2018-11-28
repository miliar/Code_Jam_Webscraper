# Simpleparse URL: http://simpleparse.sourceforge.net

from simpleparse.common import numbers, strings
from simpleparse.parser import Parser

grammar = '''
root := tree
tree := "(", [ \t\n]*, weight, [ \t\n]*, subtree?, [ \t\n]*, ")"
subtree := feature, [ \t\n]*, l_tree, [ \t\n]*, r_tree
l_tree := tree
r_tree := tree
feature := [a-z]*
weight := number
'''

from simpleparse.dispatchprocessor import *

class Tree(object):
    def __init__(self):
        self.weight = None
        self.feature = None
        self.left = None
        self.right = None

    def __repr__(self):
        return '(%f %s %s %s)' % (self.weight, self.feature, repr(self.left), repr(self.right))

    def cuteness(self, features):
        if self.feature is None:
            return self.weight
        elif self.feature in features:
            return self.weight * self.left.cuteness(features)
        else:
            return self.weight * self.right.cuteness(features)

nodeStack = []

class TreeProcessor(DispatchProcessor):
    def __init__(self):
        nodeStack = []
        
    def tree(self, (tag,start,stop,subtags), buffer ):
        tree = Tree()
        nodeStack.append(tree)
        dispatchList(self, subtags, buffer)

    def l_tree(self, (tag,start,stop,subtags), buffer ):
        dispatchList(self, subtags, buffer)

    def r_tree(self, (tag,start,stop,subtags), buffer ):
        dispatchList(self, subtags, buffer)

    def subtree(self, (tag,start,stop,subtags), buffer ):
        for subtag in subtags:
            if subtag[0] == 'feature':
                dispatch(self, subtag, buffer)
            elif subtag[0] == 'l_tree':
                dispatch(self, subtag, buffer)
                l_tree = nodeStack.pop()
                nodeStack[-1].left = l_tree
            elif subtag[0] == 'r_tree':
                dispatch(self, subtag, buffer)
                r_tree = nodeStack.pop()
                nodeStack[-1].right = r_tree

    def weight(self, (tag,start,stop,subtags), buffer ):
        nodeStack[-1].weight = float(getString((tag,start,stop,subtags), buffer ))

    def feature(self, (tag,start,stop,subtags), buffer ):
        nodeStack[-1].feature = getString((tag,start,stop,subtags), buffer )

class TreeParser(Parser):
    def buildProcessor(self):
        return TreeProcessor()

def process(in_file):
    parser = TreeParser(grammar)
    in_file = open(in_file)
    N = int(in_file.readline().strip())
    for test_num in range(N):
        L = int(in_file.readline().strip())
        tree_string = []
        for i in range(L):
            tree_string.append(in_file.readline().strip())
        tree_string = ' '.join(tree_string)
        parser.parse(tree_string)
        tree = nodeStack.pop()
        A = int(in_file.readline().strip())
        print 'Case #%d:' % (test_num + 1)
        for i in range(A):
            animal_data = in_file.readline().strip().split()
            animal_features = set(animal_data[2:])
            print '%.7f' % tree.cuteness(animal_features)

if __name__ == '__main__':
    import sys
    #test = '(0.5 cool ( 1.000) (0.5 ))'
    #parser = TreeParser(grammar)
    #parser.parse(test)
    #print nodeStack
    process(sys.argv[1])
        
