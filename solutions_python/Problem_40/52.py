#!/usr/bin/python
import sys

class Node(object):
    def __init__(self):
        self.name = None
        self.p = None
        self.yes_son = None
        self.no_son = None

def eat_blanks(tree,c):
    while tree[c] in ("\n", "\r", " "):
        c+= 1
    return c

def parse_tree(tree, c):
    root = Node()
    c = eat_blanks(tree, c)
    if tree[c] != "(":
        print "ERROR"
        return None,None
    c += 1
    c = eat_blanks(tree, c)
    c1 = c
    while tree[c1] not in ("\r", "\n", " ", ")"):
        c1 += 1
    root.p = float(tree[c:c1])
    c = c1
    c = eat_blanks(tree, c)
    if tree[c] == ")":
        return c+1, root
    c1 = c
    while tree[c1] not in (" ", "\n", "\r"):
        c1 += 1
    root.name = tree[c:c1]
    c = c1
    c = c1
    c,root.yes_son = parse_tree(tree, c)
    c,root.no_son = parse_tree(tree, c)

    c = eat_blanks(tree, c)
    return c+1, root
    


def calc_ans(tree, animals):

    _,orig_root = parse_tree(tree, 0)

    answers = []
    for animal in animals:
        root = orig_root
        p = 1
        p *= root.p
        while root.yes_son is not None:
            if root.name in animal[1]:
                root = root.yes_son
            else:
                root = root.no_son
            p *= root.p

        answers.append(p)
    return "\n".join(map(lambda f: "%.06f" % f, answers))

def main():
   handle = file(sys.argv[1])
   lines_no = int(handle.readline())
   for line_no in xrange(1,lines_no+1):
      L = int(handle.readline())
      lines = []
      for i in range(L):
          lines.append(handle.readline())
      tree = "".join(lines)
      A = int(handle.readline())
      animals = []
      for i in range(A):
          raw = handle.readline().split()
          animals.append((raw[0], set(raw[2:])))

      print "Case #%d:\n%s" % (line_no, calc_ans(tree, animals))

main()
