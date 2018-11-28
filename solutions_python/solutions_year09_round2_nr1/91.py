from sys import stdin
from sys import stdout
import string

class Node:
    def __init__(self):
        self.weight = 0.0
        self.feature = None
        self.yesNode = None
        self.noNode = Node

def parse(s, i = 0):
    j = i + 1
    while j < len(s) and (s[j] in string.digits or s[j] == "."): j=j+1
    node = Node()
    node.weight = float(s[i+1:j])
    if s[j] != ")":
        k = s.index("(", j)
        node.feature = s[j:k]
        (node.yesNode, t) = parse(s, k)
        (node.noNode, j) = parse(s, t)
    return [node, j + 1]

for case in range(1, int(stdin.readline()) + 1):
    l = int(stdin.readline())
    treeStr = "".join(stdin.readline().strip().replace(" ", "") for _ in range(l))

    root = parse(treeStr)[0]

    print "Case #%d:" % case

    a = int(stdin.readline())
    for i in range(a):
        animal = stdin.readline().split()[2:]
        p = 1.0
        node = root
        while True:
            p = p * node.weight
            if node.feature is None:
                break
            else:
                node = node.feature in animal and node.yesNode or node.noNode

        print "%.7f" % p
    
