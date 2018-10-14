
import re

from helper_functions import *


def solve_problem(input, output):
    n_cases = getnum(input)
    for case in xrange(n_cases):
        n_lines = getnum(input)
        treestring = ''
        for n in xrange(n_lines):
            treestring = treestring + getline(input).replace(' ', '')
        tree = gettree(treestring)
        n_animals = getnum(input)
        ps = []
        for n in xrange(n_animals):
            animaldetails = getwords(input)
            name = animaldetails.pop(0)
            try:
                ndetails_ = animaldetails.pop(0)
            except:
                pass
            properties = animaldetails
            p = get_probability(properties, tree, 1)
            ps.append(str(p))
        answer('\n'+'\n'.join(ps), output)
def get_probability(properties, tree, p):
    while True:
        if len(tree) == 1:
            return p * tree[0]
        else:
            weight, feature, ltree, rtree = tree
            p *= weight
            if feature in properties:
                tree = ltree
            else:
                tree = rtree
        
    

def gettree(treestring):
    treestring = treestring.replace(')', ',),')
    treestring, n_ = re.subn(r'([a-z]+)', r',"\1",', treestring)
    treestring = treestring.replace(',,', ',')
    
    tree =  eval(treestring)
    return tree[0]

def get_path_length(queries, names):
    n_swallowed = 0
    cost = 0
    while queries:
        for name in names:
            try:
                n_swallowed = max(n_swallowed, queries.index(name))
            except ValueError:
                return  cost#no need for any changes: we have a name which doesn't conflict
    
        cost = cost+1
        queries = queries[n_swallowed:]
        n_swallowed = 0
    
    
    

if __name__ == "__main__":
    test_input = """
2
3
(0.5 cool
  ( 1.000)
  (0.5 ))
2
anteater 1 cool
cockroach 0
13
(0.2 furry
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
3
beaver 2 furry freshwater
trout 4 fast freshwater fishy rainbowy
dodo 1 extinct
    """
    test_output = """
Case #1:
0.5000000
0.2500000
Case #2:
0.0324000
0.0000600
0.0020000
    """
    
    #do_test(solve_problem, test_input, test_output)
    
    do_real(solve_problem)