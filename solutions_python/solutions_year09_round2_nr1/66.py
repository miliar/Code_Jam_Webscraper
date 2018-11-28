from sys import stdin, stderr

'''(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
'''

def remove_empty(tokens):
    new_tokens = []
    for i in tokens:
        if i != '':
            new_tokens.append(i)
    return new_tokens

def read_next_subtree(tokens, start):
    #print >> stderr, "read next subtree from", tokens
    subtree_tokens = []
    
    open = 0
    for i in range(start, len(tokens)):
        #print >> stderr, "reading token", i, tokens[i]
        subtree_tokens.append(tokens[i])
        if tokens[i] == '(':
            open += 1
        if tokens[i] == ')':
            open -= 1
            if open == 0:
                #print >> stderr, "subtree is:", subtree_tokens, "next is", (i + 1)
                return (subtree_tokens, i+1)

def compute_prob(root, features):
    node = root
    prob = root.weight
    while node.question != '':
        #print >> stderr, "asking:", node.question, prob
        if node.question in features:
            node = node.children[0]
            prob *= node.weight
        else:
            node = node.children[1]
            prob *= node.weight
    return prob

class Node:
    def __init__(self, descr):
        #print >> stderr, "parsing", descr
        if descr[0] == '(':
            #print >> stderr, "ok"
            pass
        self.weight = float(descr[1])
        #print >> stderr, "weight", self.weight
        self.question = ''
        self.children = []
        if descr[2] == ')':
            #print >> stderr, "done"
            pass
        else:
            self.question = descr[2]
            #print >> stderr, "question", self.question
            next = 3
            while next < len(descr) - 1:
                #print >> stderr, "giving", next, descr
                (subtree, next) = read_next_subtree(descr, next)
                #print >> stderr, "got next", next, "subtree", subtree
                if len(subtree) > 0:
                    self.children.append(Node(subtree))

    def print_tree(self):
        print >> stderr, "(", self.weight, self.question
        for child in self.children:
            child.print_tree()
        print >> stderr, ")"

def read_line():
    return stdin.readline().rstrip('\r\n')

def read_ints():
    line = read_line()
    return map(int,
               line.rstrip('\r\n').split(' '))

def read_strings():
    line = read_line()
    return line.rstrip('\r\n').split(' ')

if __name__ == '__main__':
    no_cases = read_ints()[0]
    print >> stderr, "No of cases: %d" % no_cases
    for case in xrange(no_cases):
        no_lines = read_ints()[0]
        tree_description = []
        for line_i in range(no_lines):
            line = read_line()
            #print >> stderr, "read line", line
            line = line.replace('(', ' ( ')
            line = line.replace(')', ' ) ')
            tokens = line.split(' ')
            tree_description += tokens

        #print >> stderr, "tree tokens:", tree_description
        root = Node(remove_empty(tree_description))
        #root.print_tree()

        print >> stderr, "Solving case %d" % (case + 1)
        print "Case #%d: " % (case + 1)

        no_animals = read_ints()[0]
        for animal_i in range(no_animals):
            animal_description = read_strings()
            name = animal_description[0]
            no_features = int(animal_description[1])
            if len(animal_description) > 2:
                features = set(animal_description[2:])
            else:
                features = set()
            prob = compute_prob(root, features)
            print "%f" % prob

        #print >> stderr, "%d %d %d %s" % (a, b, c, d)

        


