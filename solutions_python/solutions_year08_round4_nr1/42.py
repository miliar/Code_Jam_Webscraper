import math
import copy
import sys
import time
from bisect import bisect
from heapq import heappush, heappop

#large number support
#dmath is a freely available Python library for arbitrary precision math
#it can be downloaded from: http://code.google.com/p/dmath/
#from dmath import *
#from decimal import Decimal as D, getcontext


problem_name = "A"

def test():
    global problem_name
    solve("c:/temp/"+problem_name+"-test.txt")

def small():
    global problem_name
    solve("c:/temp/"+problem_name+"-small-attempt0.in")

def large():
    global problem_name
    solve("c:/temp/"+problem_name+"-large.in")

def solve(dataset):
    global problem_name
    datafile = open(dataset, 'r')
    outfile = open("c:/temp/"+problem_name+"results.txt",'w')
    
    numberoftestcases = int(datafile.readline().strip())
    print "Number of Test Cases = %d" % (numberoftestcases)
    for testcasenumber in range(1,numberoftestcases+1):
        print "Test case #%d" % (testcasenumber)

        #Get parameters
        parameters = datafile.readline().strip().split()
        int_params = [int(x) for x in parameters]
        M, V = int_params

        nlist = []
        for i in xrange(M):
            parameters = datafile.readline().strip().split()
            int_params = [int(x) for x in parameters]
            nlist.append( int_params  )

        t1 = time.time()
        answer = solvecase(nlist, 0)
        answer = answer[V]
        if answer == "imp":
            answer = "IMPOSSIBLE"
        t2 = time.time()

        answerline = "Case #%d: %s" % (testcasenumber, str(answer))
        print answerline + " (solved in %.3fs)" % ((t2-t1))
        outfile.write("%s\n" % answerline)

    outfile.close()

## PROBLEM SPECIFIC FUNCTIONS ##############################

def solvecase(nlist, i):
    best_sol = 0

    me = nlist[i]

    if len(me) == 1:
        #leaf node
        if me[0] == 0:
            return (0, "imp")
        else:
            return ("imp",0)

    assert(len(nlist) > 2*i+2)

    lchild = solvecase(nlist,2*i+1)
    rchild = solvecase(nlist,2*i+2)
    
    if me[1] == 1:
        #changeable
        if lchild[0] == "imp" or rchild[0] == "imp":
            orvals= ("imp", min(lchild[1],rchild[1]))
        else:
            orvals= (lchild[0]+rchild[0], min(lchild[1],rchild[1]))

        if lchild[1] == "imp" or rchild[1] == "imp":
            andvals= (min(lchild[0],rchild[0]), "imp")
        else:
            andvals= (min(lchild[0],rchild[0]), lchild[1]+rchild[1])

        myvals = orvals
        ovals = andvals

        if me[0] == 1:
            myvals = andvals
            ovals = orvals

        a,b,c,d = "imp","imp","imp","imp"

        if ovals[0] != "imp":
            b = ovals[0]+1
        if ovals[1] != "imp":
            d = ovals[1]+1

        return (min(myvals[0],b),min(myvals[1],d))

    if me[0] == 0:
        #OR gate
        if lchild[0] == "imp" or rchild[0] == "imp":
            return ("imp", min(lchild[1],rchild[1]))
        else:
            return (lchild[0]+rchild[0], min(lchild[1],rchild[1]))
    else:
        #AND gate
        if lchild[1] == "imp" or rchild[1] == "imp":
            return (min(lchild[0],rchild[0]), "imp")
        else:
            return (min(lchild[0],rchild[0]), lchild[1]+rchild[1])
        

## HELPER FUNCTIONS ########################################
# Not necessarily used, but I don't want to have to reinvent the
# wheel in 2 hours like I've been doing for all the previous rounds

# Undirected graph
##class graph_node:
##    def __init__(self,setidnum):
##        self.idnum = setidnum
##        self.edges = []
##    def 
##
##class undirected_graph:
##    def __init__(self):
##        self.nodes = []
##        self.mapping = {}
        

# Binary tree
class bst_node:
    def __init__(self, parent = None, left = None, right = None, key = None, data = None):
        self.lchild = left
        self.rchild = right
        self.key = key
        self.data = data
        self.parent = None
    def __cmp__(self,other):
        return cmp(self.key,other.key)
    def __str__(self):
        return "%s=>%s" % (str(self.key),str(self.data))
    def isLeaf(self):
        if self.lchild is None and self.rchild is None:
            return True
        return False
    
class binary_search_tree:
    def __init__(self):
        self.root = None

    #returns True on duplicate addition
    def add(self, addkey, adddata):
        if self.root is None:
            self.root = bst_node(key = addkey, data = adddata)
            return False
        else:
            cn = self.root
            dup = False
            while True:
                if cn.key > addkey:
                    if cn.lchild is None:
                        cn.lchild = bst_node(parent = cn, key = addkey, data = adddata)
                        return dup
                    else:
                        cn = cn.lchild
                else:
                    if cn.key == addkey:
                        dup = True
                    
                    if cn.rchild is None:
                        cn.rchild = bst_node(parent = cn, key = addkey, data = adddata)
                        return dup
                    else:
                        cn = cn.rchild
 
    def find(self, findkey):
        cn = self.root
        if cn is None:
            return None
 
        while True:
            if cn.key > findkey:
                if cn.lchild is None:
                    return None
                else:
                    cn = cn.lchild
            elif cn.key == findkey:
                return cn
            else:
                if cn.rchild is None:
                    return None
                else:
                    cn = cn.rchild

    def findAll(self, findkey):
        results = []

        cn = self.root
        if cn is None:
            return None

        while True:
            if cn.key > findkey:
                if cn.lchild is None:
                    return results
                else:
                    cn = cn.lchild
            elif cn.key == findkey:
                results.append(cn)
                cn = cn.rchild
                if cn is None:
                    return results
            else:
                if cn.rchild is None:
                    return results
                else:
                    cn = cn.rchild
 
    def remove(self, findkey):
        #don't use if contains duplicates
        if self.root.key == findkey:
            if self.root.rchild is None:
                if self.root.lchild is None:
                    self.root = None
                else:
                    self.root = self.root.lchild
                    self.root.parent = None
            else:
                self.root.rchild.lchild = self.root.lchild
                self.root = self.root.rchild
                self.root.parent = None
            return True
        cn = self.root
        while True:
            if cn.key > findkey:
                if cn.lchild is None:
                    return False
                elif cn.lchild.key == findkey:
                    if cn.lchild.lchild is None and cn.lchild.rchild is None:
                        cn.lchild = None
                    elif cn.lchild.rchild is None:
                        cn.lchild = cn.lchild.lchild
                        cn.lchild.parent = cn
                    else:
                        cn.lchild = cn.lchild.rchild
                        cn.lchild.parent = cn
                    return True
                else:
                    cn = cn.lchild
            if cn.key < findkey:
                if cn.rchild is None:
                    return False
                elif cn.rchild.key == findkey:
                    if cn.rchild.lchild is None and cn.rchild.rchild is None:
                        cn.rchild = None
                    elif cn.rchild.rchild is None:
                        cn.rchild = cn.rchild.lchild
                        cn.rchild.parent = cn
                    else:
                        cn.rchild = cn.rchild.rchild
                        cn.rchild.parent = cn

                    return True
                else:
                    cn = cn.rchild
        return False

# Ordered leaf tree. The leaf nodes are alllll in order stored in an array
# Good for keeping track on sums of values to the left or right of nodes....
# or something

# move up and to the left (or to 0 if left child):
# cursor = cursor - (cursor & -cursor)

# move down and to the right:
# cursor = cursor | ((cursor & -cursor) >> 1)

# move down and to the left:
# cursor = (cursor & (cursor-1)) | ((cursor & -cursor) >> 1)

# move up and to the right (or to the least high parent that IS to the right)
# cursor = cursor + (cursor & -cursor)

def get_node_value(node,tree):
    return tree[node]

def set_node_value(value,node,tree):
    tree[node] = value

def is_leaf_node(node,tree):
    return (node & 1) == 1

def get_parent_of(node,tree):
    n = node - (node & -node)
    if n == 0:
        n = node + (node & -node)
    return n

def add_cascade_all_the_way_up(num,node,tree):
    node = node+1
    
    while node > 0 and node < len(tree):
        set_node_value(get_node_value(node, tree) + num, node, tree)
        node = get_parent_of(node,tree)

def add_cascade_up_and_left_of_node(num,node,tree):
    node = node+1
    
    while node > 0:
        n = get_node_value(node,tree)
        set_node_value(n+num, node, tree)
        node = node - (node & -node)

def get_cascade_sum_of_up_and_right_of_node(node, tree):
    node = node+1
    
    num = 0
    while node < len(tree):
        num = num + get_node_value(node,tree)
        node = node + (node & -node)

    return num

def print_tree(tree):
    tree_height = math.log(len(tree)) / math.log(2)

    for i in xrange(tree_height,-1,-1):
        level_bit = 2 ** i
        line = ""
        for num in xrange(1, len(tree)):
            if (num & level_bit == level_bit) and (num & level_bit-1 == 0):
                line = line + "%s%4d" % ( ( (num-1)*4 - len(line))*" " ,get_node_value(num,tree))
       
        print line

    print "-" * len(line)
    for i in xrange(1, len(tree)):
        sys.stdout.write( "%4d" % (i%100) )
    print

class prime_util:
    def __init__(self, maxprime):
        self.primelist = []

        while self.findNextPrime() < maxprime:
            #do nothing
            continue

    def isPrimeSlow(self,num):
        upto = math.sqrt(num)
        for prime in self.primelist:
            if prime > upto:
                return True
            if num % prime == 0:
                return False
        return True
    
    def findNextPrime(self):
        greatest = 0
        if len(self.primelist) > 0:
            greatest = self.primelist[len(self.primelist) - 1]

        if greatest < 2:
            self.primelist.append(2)
            return 2

        if greatest == 2:
            self.primelist.append(3)
            return 3
        
        number = greatest + 2
        while self.isPrimeSlow(number) == False:
            number = number + 2

        self.primelist.append(number)

        return number

    def isPrime(self,number):
        point = bisect(self.primelist, number) - 1

        if point < 0:
            return False

        if self.primelist[point] == number:
            return True
        else:
            return False
