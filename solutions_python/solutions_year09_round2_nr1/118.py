#!/usr/bin/env python

import sys
import re


def debug(str):
    #pass
    print >> sys.stderr, str

class DecisionTree:
    def __init__(self, lines):
        debug("building tree for %s" % lines[0])
        debug("".join(lines))
        parts = re.search('([0-9.]+) ?([a-z]+)?', lines[0].strip())
        self.weight = float(parts.group(1))
        self.feature = parts.group(2)
        self.left = None
        self.right = None
        if self.feature:
            close_count = 0
            depth = 0
            tree1_lines = []
            tree2_lines = []
            for line in lines[1:]:
                depth += line.count("(")
                #debug("Descending through %s, depth = %d" % (line.strip(), depth))

                if close_count == 0:
                    tree1_lines.append(line)
                elif close_count == 1:
                    tree2_lines.append(line)

                depth -= line.count(")")

                if depth == 0:
                    close_count += 1
                if depth == -1:
                    break

            if len(tree1_lines) > 0:
                self.left = DecisionTree(tree1_lines)
            if len(tree2_lines) > 0:
                self.right = DecisionTree(tree2_lines)

    def is_leaf(self):
        return not self.feature

    def dump(self, indent):
        debug((" "*indent) + "("+str(self.weight)+" "+(self.feature or ""))
        if self.left:
            self.left.dump(indent+2)
        if self.right:
            self.right.dump(indent+2)
        debug((" "*indent) + ")")

    def score(self, animal, p):
        parts = animal.split(" ")[2:]
        p *= self.weight
        if self.is_leaf():
            return p
        else:
            if(self.feature in parts):
                return self.left.score(animal, p)
            else:
                return self.right.score(animal, p)





data = sys.stdin.readlines()
current_line = 0
num_test_cases = int(data[current_line])
current_line = current_line+1
cute = None

for i in range(num_test_cases):
    print("Case #"+str(i+1)+":")
    num_lines = int(data[current_line])
    current_line = current_line+1
    tree_lines = []
    for j in range(num_lines):
        tree_lines.append(data[current_line])
        current_line = current_line+1
    cute = DecisionTree(tree_lines)
    cute.dump(0)
    num_animals = int(data[current_line])
    current_line = current_line+1
    for j in range(num_animals):
        print "%.7f" % cute.score(data[current_line].strip(), 1.0)
        current_line = current_line+1


