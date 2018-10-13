#!/usr/bin/python

def subseq(elt, lst):
    for i in range(len(lst)):
        if lst[i] == elt:
            return lst[(i+1):]        
    return []

N = input()

for case in range(N):
    case_string = raw_input()
    case_data = case_string.split()
    case_data = map(eval,case_data)
    n,A,B,C,D,x0,y0,M = case_data 


    X = x0
    Y = y0
    trees = []
    trees.append((X,Y))
    for i in range(n)[1:]:
        X = (A*X+B) % M
        Y = (C*Y+D) % M
        trees.append((X,Y))
    #print trees

    triangles = 0

    for tree1 in trees:
        xa,ya = tree1
        for tree2 in subseq(tree1, trees): 
            xb,yb = tree2
            for tree3 in subseq(tree2, trees):
                xc,yc = tree3
                xmid = (xa+xb+xc)/3.0
                ymid = (ya+yb+yc)/3.0
                if (xmid,ymid) == (int(xmid), int(ymid)):
                    #print xmid,ymid
                    triangles+=1

    print "Case #"+str(case+1)+": "+str(triangles)



