# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import sqrt, ceil, floor
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from gurobipy import *


def parse(f):
    lst = []
    f.next()
    for l in f:
        R = int(l.split()[1])
        O = int(l.split()[2])
        Y = int(l.split()[3])
        G = int(l.split()[4])
        B = int(l.split()[5])
        V = int(l.split()[6])
        lst.append((R, O, Y, G, B, V))
    return lst


def unicorns(R, O, Y, G, B, V):
    model = Model("unicorns")
    #     model.Params.numericfocus = 3
    N = R + O + Y + G + B + V
    Rs = {}
    Os = {}
    Ys = {}
    Gs = {}
    Bs = {}
    Vs = {}
    for n in range(N):
        Rs[n] = model.addVar(
            vtype=GRB.BINARY, name="Rs["+str(n)+"]")
        Os[n] = model.addVar(
            vtype=GRB.BINARY, name="Os["+str(n)+"]")
        Ys[n] = model.addVar(
            vtype=GRB.BINARY, name="Ys["+str(n)+"]")
        Gs[n] = model.addVar(
            vtype=GRB.BINARY, name="Gs["+str(n)+"]")
        Bs[n] = model.addVar(
            vtype=GRB.BINARY, name="Bs["+str(n)+"]")
        Vs[n] = model.addVar(
            vtype=GRB.BINARY, name="Vs["+str(n)+"]")


    # Update the model before defining constraints
    print("Updating model... ", end='')
    sys.stdout.flush()
    model.update()
    print("done.")

    # constraints
    print("Defining constraints... ", end='')
    sys.stdout.flush()
    model.addConstr(quicksum([Rs[n] for n in xrange(N)]) == R)
    model.addConstr(quicksum([Os[n] for n in xrange(N)]) == O)
    model.addConstr(quicksum([Ys[n] for n in xrange(N)]) == Y)
    model.addConstr(quicksum([Gs[n] for n in xrange(N)]) == G)
    model.addConstr(quicksum([Bs[n] for n in xrange(N)]) == B)
    model.addConstr(quicksum([Vs[n] for n in xrange(N)]) == V)

    for n in xrange(N):
        model.addConstr(Rs[n] + Os[n] + Ys[n] + Gs[n] + Bs[n] + Vs[n] == 1)
    
    for n in xrange(N):
        model.addConstr(Rs[n]*Rs[(n+1) % N] == 0)
        model.addConstr(Rs[n]*Os[(n+1) % N] == 0)
        model.addConstr(Rs[n]*Vs[(n+1) % N] == 0)
        
        model.addConstr(Os[n]*Rs[(n+1) % N] == 0)
        model.addConstr(Os[n]*Os[(n+1) % N] == 0)
        model.addConstr(Os[n]*Ys[(n+1) % N] == 0)
        model.addConstr(Os[n]*Gs[(n+1) % N] == 0)
        model.addConstr(Os[n]*Vs[(n+1) % N] == 0)
        
        model.addConstr(Ys[n]*Os[(n+1) % N] == 0)
        model.addConstr(Ys[n]*Ys[(n+1) % N] == 0)
        model.addConstr(Ys[n]*Gs[(n+1) % N] == 0)

        model.addConstr(Gs[n]*Ys[(n+1) % N] == 0)
        model.addConstr(Gs[n]*Bs[(n+1) % N] == 0)
        model.addConstr(Gs[n]*Os[(n+1) % N] == 0)
        model.addConstr(Gs[n]*Gs[(n+1) % N] == 0)
        model.addConstr(Gs[n]*Vs[(n+1) % N] == 0)

        model.addConstr(Bs[n]*Bs[(n+1) % N] == 0)
        model.addConstr(Bs[n]*Gs[(n+1) % N] == 0)
        model.addConstr(Bs[n]*Vs[(n+1) % N] == 0)

        model.addConstr(Vs[n]*Rs[(n+1) % N] == 0)
        model.addConstr(Vs[n]*Bs[(n+1) % N] == 0)
        model.addConstr(Vs[n]*Os[(n+1) % N] == 0)
        model.addConstr(Vs[n]*Gs[(n+1) % N] == 0)
        model.addConstr(Vs[n]*Vs[(n+1) % N] == 0)



    print("Setting objective ... ", end='')
    sys.stdout.flush()
    model.setObjective(quicksum([Rs[n] for n in xrange(N)]), GRB.MAXIMIZE)
    #     model.setObjective(quicksum([U[n]*vs[n] for n in range(N)]), GRB.MAXIMIZE)
    print("done.")

    print("Optimizing (handing over to Gurobi)...")
    model.optimize()

    if model.status == GRB.Status.OPTIMAL:
        string = ""
        for n in xrange(N):
            if(Rs[n].x):
                string += "R"
            if(Os[n].x):
                string += "O"
            if(Ys[n].x):
                string += "Y"
            if(Gs[n].x):
                string += "G"
            if(Bs[n].x):
                string += "B"
            if(Vs[n].x):
                string += "V"
        return string
    else:
        return "IMPOSSIBLE"


def output(fw, inlst):
    for i, a in enumerate(inlst):
        ret = unicorns(*a)
        print(i, ret)
        fw.write("Case #" + str(i+1) + ": " + ret+ "\n")


f = open("B.in", 'r')
fw = open("B.out", 'w')
output(fw, parse(f))
