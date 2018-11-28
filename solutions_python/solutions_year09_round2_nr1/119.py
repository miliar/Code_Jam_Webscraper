
import sys
import re

def gentree(tree):
    otree = tree
    regx = re.compile("[a-z]+")
    regx2 = re.compile(",+")
    for word in sorted(set(regx.findall(tree)), key=lambda w: len(w), reverse=True):
        tree = tree.replace(" " + word, ',"%s",' % word)
    tree = tree.replace(')', ',),').replace('\n', '').replace(' ', '')
    for comma in regx2.findall(tree): tree = tree.replace(comma, ',')
    tree = eval(tree[:-1])
    return tree



# parse tree
with open(sys.argv[1]) as input:
    trees = input.readline().strip()
    for i in xrange(int(trees)):
        tree = ''.join(input.readline() for j in xrange(int(input.readline().strip())))
        tree = gentree(tree)
        print "Case #%s:" % (i+1)
        for j in xrange(int(input.readline().strip())):
            case = input.readline().strip().split(' ')
            animal = case.pop(0).strip()
            ncases = int(case.pop(0))

            #eval cases
            score = 1
            wtree = tree
            while True:
                try:
                    mult, feature, ttree, ftree = wtree
                except ValueError:
                    mult = wtree[0]
                    feature, ttree, ftree = None, None, None

                score *= float(mult)

                if feature is None: break

                if feature in case:
                    wtree = ttree
                else:
                    wtree = ftree
                
            print "%.7f" % score


