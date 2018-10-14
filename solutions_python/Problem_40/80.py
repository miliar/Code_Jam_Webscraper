#import numpy
#import scipy
import sys
import csv
#from numpy import zeros
#from numpy import size

def __main__():
    input = sys.argv[1]

    r = csv.reader(open(input),delimiter=' ',quoting=csv.QUOTE_NONE)
    N = int(r.next()[0])
    for i in range(0,N):
        [l] = r.next(); l = int(l)
        treetxt = []
        for j in range(0,l):
            linestr = r.next()
            for k in range(0,len(linestr)):
                linestr[k] = linestr[k].replace('(','')
                linestr[k] = linestr[k].replace(')','')
            while linestr.count('')>0:
                linestr.remove('')
            if (len(linestr)>0):
                treetxt.append(linestr)
        [tree, lines] = construct_tree(treetxt,0)

        print "Case #"+str(i+1)+":"
        [a] = r.next(); a = int(a)
        for j in range(0,a):
            animal = r.next()[2:]
            print '%8.7f' % prediction(tree, animal)

def construct_tree(treetxt, line):
    if (len(treetxt[line])==1): # leaf
        str1 = treetxt[line][0]
        p = float(str1)
        tree = [p, '', [], []]
        return([tree, line+1])
    else:
        str1 = treetxt[line][0]
#        print(treetxt[line])
        p = float(str1)
        attr = treetxt[line][1]
        [yes, yesend] = construct_tree(treetxt, line+1)
        [no, noend] = construct_tree(treetxt, yesend)
        tree = [p, attr, yes, no]
        return([tree, noend])
    
def prediction(tree, animal):
    p = 1; node = tree
    finished = False
    while not finished:
        p = p * node[0]
        if (node[1] == ''):
            finished = True
        else:
            if animal.count(node[1])>0:
                node = node[2]
            else:
                node = node[3]
#    p = str(round(p * 1E7))
    return(p)
        
if __name__ == '__main__': __main__()