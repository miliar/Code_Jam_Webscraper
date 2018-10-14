import math
import copy

def test():
    solve("c:/temp/tree_test.txt")

def small():
    solve("c:/temp/A-small-attempt0.in")

def large():
    solve("c:/temp/A-large.in")

def solve(dataset):
    datafile = open(dataset, 'r')
    outfile = open("c:/temp/results.txt",'w')
    
    numberoftestcases = int(datafile.readline().strip())
    print "Number of Test Cases = %d" % (numberoftestcases)
    for testcasenumber in range(1,numberoftestcases+1):
        print "Test case #%d" % (testcasenumber)

        parameters = datafile.readline().strip().split()
        int_param = []
        for param in parameters:
            int_param.append(int(param))

        n,A,B,C,D,x0,y0,M = int_param

        answer = solvecase(n,A,B,C,D,x0,y0,M)

        answerline = "Case #%d: %d" % (testcasenumber, answer)
        print answerline
        outfile.write("%s\n" % answerline)

    outfile.close()

def solvecase(n,A,B,C,D,x0,y0,M):
    trees = []
    trees.append( (x0,y0) )

    X = x0
    Y = y0
    for i in xrange(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append( (X,Y) )
        
    mod_answers = []
    mods = [[0,0,0],[0,0,0],[0,0,0]]

    i = len(trees)-1
    while i>=0:
        modx = trees[i][0] % 3
        mody = trees[i][1] % 3

        mods[modx][mody] = mods[modx][mody]+1
        mod_answers.insert(0, copy.deepcopy(mods))
        
        i = i - 1  

    t2_mod_answers = [  [[0,0,0],[0,0,0],[0,0,0]]  ]
    twotreemods = [[0,0,0],[0,0,0],[0,0,0]]
    prev_two_tree = twotreemods

    i = len(trees)-2
    while i>=0:

        treex = trees[i][0]
        treey = trees[i][1]
        onetreemods = mod_answers[i+1]
        twotreemods = [[0,0,0],[0,0,0],[0,0,0]]

        for x in xrange(3):
            for y in xrange(3):
                twotreemods[ (x+treex) % 3 ][(y+treey) % 3]  =  onetreemods[x][y]
                
        for x in xrange(3):
            for y in xrange(3):
                twotreemods[x][y] = twotreemods[x][y] + prev_two_tree[x][y]

        t2_mod_answers.insert(0, copy.deepcopy(twotreemods))
        
        prev_two_tree = twotreemods
        i = i - 1
    
    t3_mod_answers = [  [[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]  ]
    threetreemods = [[0,0,0],[0,0,0],[0,0,0]]
    prev_three_tree = threetreemods

    i = len(trees)-3
    while i>=0:

        treex = trees[i][0]
        treey = trees[i][1]
        twotreemods = t2_mod_answers[i+1]
        threetreemods = [[0,0,0],[0,0,0],[0,0,0]]

        for x in xrange(3):
            for y in xrange(3):
                threetreemods[ (x+treex) % 3 ][(y+treey) % 3]  =  twotreemods[x][y]
                
        for x in xrange(3):
            for y in xrange(3):
                threetreemods[x][y] = threetreemods[x][y] + prev_three_tree[x][y]

        t3_mod_answers.insert(0, copy.deepcopy(threetreemods))
        
        prev_three_tree = threetreemods
        i = i - 1        

    #print "t1: %s" % str(mod_answers)
    #print "t2: %s" % str(t2_mod_answers)
    #print "t3: %s" % str(t3_mod_answers)

    return t3_mod_answers[0][0][0]
