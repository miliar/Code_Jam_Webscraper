import sys,re 
from itertools import *

def parser(lines):
    x = " ".join(l.strip() for l in lines)
    x = re.sub(r' \s+',' ', x)
    x = re.sub(r'([a-z]+)', r'"\1"', x)
    x = re.sub(r'\(\s*', r'[', x)
    x = re.sub(r'\s*\)', r']', x)
    return eval(",".join(x.split()))

def read_tree(input):
    lcount = int(input.next().strip())
    tree = parser(islice(input, lcount))
    return tree

def read_animals(input):
    n = int(input.next().strip())
    animals = []
    for a in islice(input, n):
        x = a.split()
        animals.append((x[0], set(x[2:])))
    return animals

def calc_coolnest(p, tree, features):
    weight = tree[0]

    p *= weight
    
    if len(tree) == 1:
        return p
    
    if type(tree[1]) == str:
        feature = tree[1]
        strees = tree[2:]
    else:
        feature = None
        strees = tree[1:]
    
    if feature is not None and feature not in features and strees:
        strees = strees[1:] 
    if strees:
        return calc_coolnest(p, strees[0], features)
    return p
        
def solve(input, case_no):
    print "solving ", case_no
    tree = read_tree(input)
    animals = read_animals(input)
    
    print tree, animals
    out = [""]+["%.7f"%calc_coolnest(1, tree, animal[1]) for animal in animals]
        
    print out
    return "\n".join(out)
    
input = iter(open(sys.argv[1], 'r'))
output = open(sys.argv[1].replace('.in', '.out'), 'w')

N = int(input.next().strip())

for case_no in range(N):
    solution = solve(input, case_no)
    print >>output, "Case #%d: %s"  % (case_no+1, solution) 