from sys import stdin as sin
import re
from StringIO import StringIO

class Leaf(object):
    def __init__(self, weight):
        self.weight = weight

    def traverse(self, animal, p=1):
        return p * self.weight

    def printt(self):
        print '( %s ) ' % str(self.weight)

class Tree(Leaf):
    def __init__(self, weight, feat, left, right):
        super(Tree, self).__init__(weight)
        self.feat = feat
        self.left = left
        self.right = right

    def traverse(self, animal, p=1):
        p = super(Tree, self).traverse(animal, p)

        if self.feat in animal:
            return self.left.traverse(animal, p)
        else:
            return self.right.traverse(animal, p)

    def printt(self):
        print '( %s %s ' % (str(self.weight), self.feat)
        self.left.printt()
        self.right.printt()
        print ') '

# not motivated enough to go for lex/yacc
def read_tree(buffer):
    # read the parenthesis
    read_token(buffer, '(')
    weight = float(read_regex(buffer, '[0-9.]'))

    try:
        read_token(buffer, ')')
        return Leaf(weight)
    except ValueError:
        feature = read_regex(buffer, '\w')
        left = read_tree(buffer)
        right = read_tree(buffer)
        tree = Tree(weight, feature, left, right)
        read_token(buffer, ')')
        return tree

def read_token(buffer, token):
    t = buffer.read(1)
    if token != t:
        buffer.seek(-1, mode=1)
        raise ValueError
    read_space(buffer)
    
def read_regex(buffer, pat):
    val = buffer.read(1)
    string = ''
    while re.match(pat,val):
        string += val
        val = buffer.read(1)
    buffer.seek(-1, mode=1)
    read_space(buffer)

    return string

def read_space(buffer):
    val = buffer.read(1)
    while val in [' ','\t','\n']:
        val = buffer.read(1)
    buffer.seek(-1, mode=1)


for c in range(int(sin.readline())):
    tree = ''
    for l in range(int(sin.readline())):
        tree += sin.readline()
    animals = []
    for a in range(int(sin.readline())):
        line = sin.readline().strip().split(' ')
        animals.append(set(line[2:]))

    tree = read_tree(StringIO(tree))

    print "Case #%d:" % (c+1)
    for a in animals:
        print "%.7f" % tree.traverse(a)
