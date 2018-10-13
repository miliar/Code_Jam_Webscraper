import sys
from pyparsing import *
from decimal import Decimal

lines = sys.stdin.readlines()
n = int(lines[0])
i = 1

def convertNumbers(s,l,toks):
    n = toks[0]
    return Decimal(n)


def run_test(node, value, feature_set):
    value*=node[0]
    if len(node)>1:
        if node[1] in feature_set:
            return run_test(node[2], value, feature_set)
        else:
            return run_test(node[3], value, feature_set)
    else:
        return value

for x in xrange(n):
    l = int(lines[i])
    i+=1
    tree_text = lines[i:i+l]
    i+=l
    n_animal = int(lines[i])
    i+=1
    animals = lines[i:i+n_animal]
    i+=n_animal
    #print "d", ''.join(tree_text).replace('\n',' '), "d", animals

    number = Word(nums + ".-").setParseAction( convertNumbers )
    feature = Word("abcdefghijklmnopqrstuvwxyz")
    node = Forward()
    node << Group(Suppress('(') + number + Optional(feature + node + node)+Suppress(')'))

    results = node.parseString(''.join(tree_text).replace('\n',' '))[0]

    print "Case #%s:" % (x + 1)
    for xx in xrange(n_animal):
        animal_str = animals[xx].split()
        animal_name = animal_str[0]
        animal_features_n = int(animal_str[1])
        animal_features = set(animal_str[2:])
        print run_test(results, Decimal(1), animal_features)
    #print "RESULTS", results
