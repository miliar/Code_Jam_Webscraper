import psyco
psyco.full()

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
      if args not in self.memoized:
        self.memoized[args] = self.function(*args)
      return self.memoized[args]

from pyparsing import *
import pprint

def solve(tree, animals):
    #.pprint(tree.asList())
    ans=""
    for animal in animals:
        features=set(animal[2:])
        node=tree[0]
        #print features
        p=1.0
        while len(node)>1:
            #print p, node
            p*=float(node[0])
            if node[1] in features:
                node=node[2]
            else:
                node=node[3]
        p*=float(node[0])
        #print node
        #print "%f\n" % p
        ans+="%f\n" % p
    return ans

from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, data.readline().rstrip('\n').split(' '))
    start_time=time()
    output = open('d:/gcj/output', 'w')
    data = open("d:/gcj/in", "r")
    Cases = int(data.readline())
    parser = nestedExpr()
    for case in range(1, Cases + 1):
        L = int(data.readline().rstrip('\n'))
        tree=parser.parseString("".join(data.readline() for _ in range(L)))
        A = int(data.readline().rstrip('\n'))
        animals=[data.readline().rstrip('\n').split(' ') for _ in range(A)]
        s="Case #%d:\n%s" % (case, solve(tree, animals))
        print(s)
        output.write(s+"\n")
    print time()-start_time

    