# -*- coding: utf-8 -*-
from __future__ import division, print_function
from gurobipy import *

def parse(f):
    lst = []
    f.next()
    for l in f:
        t = l.split()
        N = int(t[0])
        M = int(t[1])
        initial_models = []
        for _ in xrange(M):
            line = f.next()
            char = line.split()[0]
            Ri = int(line.split()[1])-1
            Ci = int(line.split()[2])-1
            initial_models.append((char, (Ri, Ci)))

        lst.append((N, initial_models))
    return lst


def fashion_show(N, initial_models):
    M = len(initial_models)
    initial_positions = [_[1] for _ in initial_models]

    model = Model("CodeJam_fashion")

    
    
    # X : 1 s'il y a un x, 0 sinon
    # P : 1 s'il y a un +, 0 sinon
    # O : 1 s'il y a un o, 0 sinon
    print("Defining U... ")
    sys.stdout.flush()
    X = {}
    P = {}
    O = {}

    
    for k in range(N):
        for l in range(N):
            X[k, l] = model.addVar(
                vtype=GRB.BINARY, name="X["+str(k)+", "+str(l)+"]")
            P[k, l] = model.addVar(
                vtype=GRB.BINARY, name="P["+str(k)+", "+str(l)+"]")
            O[k, l] = model.addVar(
                vtype=GRB.BINARY, name="O["+str(k)+", "+str(l)+"]")

    # Update the model before defining constraints
    print("Updating model... ", end='')
    model.update()
    print("done.")

    # constraints
    print("Defining constraints... ", end='')
    # rows and columns
    for k in xrange(N):
        model.addConstr(quicksum([X[k, l] + O[k, l] for l in range(N)]) <= 1)
        model.addConstr(quicksum([X[l, k] + O[l, k] for l in range(N)]) <= 1)
        
    # diagonals
    for tot in xrange(-N+1, N):
        model.addConstr(quicksum([P[i, tot+i] + O[i, tot+i] for i in range(max(-tot, 0), min(N, N-tot))]) <= 1)
        model.addConstr(quicksum([P[tot+i, i] + O[tot+i, i] for i in range(max(-tot, 0), min(N, N-tot))]) <= 1)

    for tot in xrange(2*N):
        model.addConstr(quicksum([P[i, tot-i] + O[i, tot-i] for i in range(max(0,tot-N+1), min(N, tot+1))]) <= 1)
        model.addConstr(quicksum([P[tot-i, i] + O[tot-i, i] for i in range(max(0,tot-N+1), min(N, tot+1))]) <= 1)






    # un mannequin par case:
    for k in xrange(N):
        for l in xrange(N):
            model.addConstr(X[k, l] + O[k, l] + P[k, l] <= 1)

    # initial positions:
    for a in initial_models:
        (k, l) = a[1]
        if(a[0] == "+"):
            model.addConstr(P[k, l] + O[k, l] == 1)
        if(a[0] == "x"):
            model.addConstr(X[k, l] + O[k, l] == 1)
        if(a[0] == "o"):
            model.addConstr(O[k, l] == 1)
            

    print("Setting objective ... ", end='')
    sys.stdout.flush()
    model.setObjective(quicksum([X[k, l] + P[k, l] + 2*O[k, l] for k in range(N) for l in range(N)]), GRB.MAXIMIZE)
    print("done.")

    print("Optimizing (handing over to Gurobi)...")
    model.optimize()

    score = int(model.objVal)
    dict_imods = {}
    for a in initial_models:
        dict_imods[a[1]] = a[0]

    dict_nmods = {}
    for k in range(N):
        for l in range(N):
            if(P[k, l].x):
                dict_nmods[k, l] = "+"
            elif(X[k, l].x):
                dict_nmods[k, l] = "x"
            elif(O[k, l].x):
                dict_nmods[k, l] = "o"
            else:
                dict_nmods[k, l] = "."

    print(dict_imods)
    print(dict_nmods)
    
    changes = []
    for k in range(N):
        for l in range(N):
            if (k, l) in dict_imods:
                if(dict_imods[k, l] != dict_nmods[k, l]):
                    changes.append((dict_nmods[k, l], (k, l)))
            else:
                if(dict_nmods[k, l] != "."):
                    changes.append((dict_nmods[k, l], (k, l)))
    

    print("*"*60)
    print(N)
    print("Starting point...")
    for k in range(N):
        for l in range(N):
            if (k, l) not in initial_positions:
                print(".", end='')
            else:
                a = initial_models[initial_positions.index((k, l))]
                print(a[0], end='')
        print()

    print("Resultat : ")
    for k in range(N):
        for l in range(N):
            if(P[k, l].x):
                print("+", end='')
            elif(X[k, l].x):
                print("x", end='')
            elif(O[k, l].x):
                print("o", end='')
            else:
                print(".", end='')
        print()
    print("Score : ", score)
    print("*"*60)

    return (score, changes)


def output(fw, inlst):
    for i, a in enumerate(inlst):
        print(i, a)
        score, changes = fashion_show(*a)
        fw.write("Case #{}: {} {}\n".format(i+1, score, len(changes)))
        for a in changes:
            fw.write("{} {} {}\n".format(a[0], a[1][0]+1, a[1][1]+1))


f = open("D-large.in", 'r')
fw = open("D-large.out_test", 'w')
output(fw, parse(f))
