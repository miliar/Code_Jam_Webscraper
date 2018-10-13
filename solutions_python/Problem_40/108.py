import sys
import re #regular expressions, string pattern matching
import math #math stuff
import array #more efficient lists (type constraint)

class Dtree:
    weight = 0
    feature = ""
    first = None
    second = None
    def __init__(self):
        self.weight = 0
        self.feature = ""
        self.first = None
        self.second = None


def parseTree(input):
    result = Dtree()
    ws,space,rest = input.strip()[1:].strip().partition(" ")
    if space == "":
        result.weight = float(ws[:-1])
        rest += ")"
    else:
        result.weight = float(ws)
    #print result.weight,
    if rest.strip()[0] == ')':
        #were done
        return result
    else:
        # get trait and children
        ft,openpar,r2 = rest.partition("(")
        result.feature = ft.strip()
        #get the starting pos of the first subtree
        parcount = 1
        pos = 0
        while not (parcount == 0):
            chr = r2[pos]
            if chr == ")":
                parcount -= 1
            elif chr == "(":
                parcount += 1
            pos +=1
        tree1in = "("+r2[:pos].strip()
        tree2in = r2[pos:-1].strip()
        result.first = parseTree(tree1in)
        result.second = parseTree(tree2in)
        return result


def solve(name, features,p,tree):
    newp = p * tree.weight
    if tree.first == None:
        return newp
    else:
        if tree.feature in features:
            return solve (name, features, newp, tree.first)
        else:
            return solve (name, features, newp, tree.second)


if __name__ == "__main__":
    cases = int(sys.stdin.readline().strip())
    for case in range(1,cases+1):
        print "Case #{0}:".format(case)
        #read and format input here
        animals = []
        treelines = int(sys.stdin.readline().strip())
        #print treelines
        treeinput = ""
        for line in range(0,treelines):
            treeinput += sys.stdin.readline().strip()
        tree = parseTree(treeinput)
        numpets = int(sys.stdin.readline().strip())
        for pet in range(0,numpets):
            animalline = sys.stdin.readline().strip().split()
            #print solution
            print solve(animalline[0], set(animalline[2:]), 1.0, tree);