import heapq
import sys

class Terminal:
    def __init__(self):
        self.label = "NoneXXX"
        pass
    
    def probability(self, labels):
        return 1.0

    def label_matches(self, labels):
        return False
    
    def left_pct(self, labels):
        return 1.0
    
    def right_pct(self, labels):
        return 1.0
    
    def __repr__(self):
        return "%s: TERMINAL" % (self.label)
    

class Node:
    def __init__(self, label = "", value = 0.0):
        self.label = label
        self.left_child = Terminal()
        self.right_child = Terminal()
        self.value = value
        self.child_index = 0
    
    def probability(self, labels):
        if self.label_matches(labels):
            return self.value * self.left_pct(labels)
        return self.value * self.right_pct(labels)
    
    def add_child(self, node):
        if self.child_index == 0:
            self.add_left_child(node)
            self.child_index = 1
        else:
            self.add_right_child(node)
    
    def add_left_child(self, node):
        self.left_child = node
        
    def add_right_child(self, node):
        self.right_child = node

    def label_matches(self, labels):
        return self.label in labels
    
    def left_pct(self, labels):
        return self.left_child.probability(labels)
    
    def right_pct(self, labels):
        return self.right_child.probability(labels)
    
    def __repr__(self):
        return "%s %f: %s %s" % (self.label, self.value, self.left_child, self.right_child)

class Case:
    def __init__(self, s, caseNum):
        self.caseNum = caseNum
        tree_line_count = int(s.read())
        self.tree_lines = s.readList(tree_line_count)
        animal_count = int(s.read())
        self.animal_strings = s.readList(animal_count)

    def solve(self):
        tree_string = "".join(self.tree_lines)
        nodes = []
        head = None
        for x in xrange(len(tree_string)):            
            if tree_string[x] == '(':
                current = Node()
                nodes.insert(0, current)
                if head is None:
                    head = current
            elif tree_string[x] == ')':
                last = nodes[0]
                del[nodes[0]]
                last_string = last.label.split(" ")
                last_string = filter(lambda x: x != '', last_string)
                last.value = float(last_string[0])
                if len(last_string) > 1:
                    last.label = last_string[1]
                else:
                    last.label = "NoneXXX"
                if len(nodes) > 0:
                    current = nodes[0]
                    current.add_child(last)
                else:
                    break
            else:
                current.label = current.label + tree_string[x]                    
        result = []
        for animal_string in self.animal_strings:
            labels = animal_string.split(" ")[2:]
            value = 0.0            
            result.append("%.7f" % head.probability(labels))
        return "\n" + "\n".join(result)
    
    def __repr__(self):
        return "Problem A Case%d" % self.caseNum

class Contents:
    def __init__(self, f):
        self.data = [line.strip() for line in f]
        self.i = 0

    def read(self):
        return self.readList(1)[0]

    def readList(self, len):
        result = self.data[self.i : self.i + len]
        self.i += len
        return result
    
def read_header(s):
    numCases = int(s.read())
    return numCases

def run():
    import sys
    f = file(sys.argv[1])
    s = Contents(f)
    numCases = read_header(s)
    for caseNum in range(numCases):
        case = Case(s, caseNum)
        print "Case #%d: %s" % (caseNum + 1, case.solve())
        sys.stdout.flush()
        
if __name__ == "__main__":
    run()