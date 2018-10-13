import numpy as np
import cvxpy
from sys import *
import random
from functools import reduce


def buildProblem(N, MLigne, MDiag):

    #Cost of problem
    ML = cvxpy.Bool(N,N)
    MD = cvxpy.Bool(N,N)

    cost = cvxpy.sum_entries(ML) + cvxpy.sum_entries(MD)

    costObject = cvxpy.Maximize(cost)

    constraints = []
    constraints.append(ML >= MLigne)
    constraints.append(MD >= MDiag)

    inveye = np.fliplr(np.eye(N,N))

    for i in range(N):
        inveye2 = np.fliplr(np.eye(i+1, i+1))

        constraints.append(cvxpy.sum_entries(ML[i,:]) <= 1)
        constraints.append(cvxpy.sum_entries(ML[:,i]) <= 1)

        if i>= 1:
            #constraints.append(cvxpy.trace(MD[:i+1, :i+1])  <= 1)
            constraints.append(cvxpy.trace(MD[:i+1, :i+1] * inveye2) <= 1)
            #constraints.append(cvxpy.trace(inveye * MD[:i+1, :i+1] * inveye)  <= 1)
            constraints.append(cvxpy.trace((inveye * MD)[:i+1, :i+1] * inveye2) <= 1)
            constraints.append(cvxpy.trace((MD * inveye)[:i+1, :i+1] * inveye2) <= 1)
            constraints.append(cvxpy.trace((inveye * MD * inveye)[:i+1, :i+1] * inveye2) <= 1)


    problem = cvxpy.Problem(costObject,constraints)
    val = problem.solve(solver = cvxpy.GLPK_MI)

    return int(np.round(val)), np.round(ML.value), np.round(MD.value)


T = int(input())
for j in range(T):
    N,K = input().split()
    N = int(N)
    K = int(K)
    MLigne = np.zeros((N,N))
    MDiag = np.zeros((N,N))


    for k in range(K):
        # ATTENTION INDICES
        s,u,v = input().split()
        u = int(u) - 1
        v = int(v) - 1
        if s == 'o':
            MLigne[u,v] = 1
            MDiag[u,v] = 1
        if s == '+':
            MDiag[u,v] = 1
        if s == 'x':
            MLigne[u,v] = 1


    val, ML, MD = buildProblem(N, MLigne, MDiag)

    Aprint = []

    if N == 1:
        if MLigne[0,0] != ML or MDiag[0,0] != MD:
            Aprint += [("o", 1, 1)]
    else:
        for i1 in range(N):
            for i2 in range(N):
                if MLigne[i1, i2] != ML[i1, i2] or MDiag[i1, i2] != MD[i1, i2]:
                    if ML[i1, i2] == 1 and MD[i1, i2] == 1:
                        Aprint += [("o", i1 + 1, i2 + 1)]
                    else:
                        if ML[i1, i2] == 1:
                            Aprint += [("x", i1 + 1, i2 + 1)]
                        if MD[i1, i2] == 1:
                            Aprint += [("+", i1 + 1, i2 + 1)]


    print("Case #{}:".format(j+1), val, len(Aprint))

    for a,b,c in Aprint:
        print(a,b,c)
