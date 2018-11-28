import sys
from math import *
from pprint import pprint

def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        L = int(sys.stdin.readline().strip())
        tree = parse_tree(sys.stdin)
        line = sys.stdin.readline().strip()
        while line.startswith(")"):
            line = sys.stdin.readline().strip()
        A = int(line)
        print 'Case #%d:' % (i+1)
        for j in xrange(A):
            animal = sys.stdin.readline().strip().split()
            animal = (animal[0], set(animal[2:]))
            print decide(tree, animal[1])

def parse_tree(input):
    line = input.readline().strip()
    if line.startswith("("):
        if line.endswith(")"):
            i = line.find(")")
            y = tuple( [float(line[1:i].strip())] )
            return y
        else:
            (w, feature) = tuple(line[1:].split())
            w = float(w)
            return (w, feature, parse_tree(input), parse_tree(input))
    if line.startswith(")"):
        return parse_tree(input)

def decide(tree, features, p=1):
    if len(tree) == 1: # leaf
        return p * tree[0]
    else:
        if tree[1] in features:
            return decide(tree[2], features, p * tree[0])
        else:
            return decide(tree[3], features, p * tree[0])

if __name__ == "__main__":
    main()
