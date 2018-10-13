import os
import sys
import math


def read_input(filename):
    f = open(filename)
    lines = f.readlines()
    curentLine = 0
    _T = int(lines[curentLine])
    for T in range(_T):
        curentLine +=1
        N, K = lines[curentLine].split()
        max, min = solver(int(N), int(K))
        print("Case #%d: %d %d" % (T+1, max, min))
    f.close()


def solver(N, K):
    pisoare = [N,]
    # print("PISOARE = ", pisoare)

    for i in range(1, K+1):

        # aflam care-i locul cel mai larg unde putem baga o noua persoana
        jMax = 0
        for j in range(len(pisoare)):
            if pisoare[j] > pisoare[jMax]:
                jMax = j

        # avem locul, bagam persoane
        liberS = math.floor((pisoare[jMax]-1) / 2)
        liberD = math.ceil((pisoare[jMax]-1) / 2)
        pisoare.insert(jMax, liberS)
        pisoare[jMax+1] = liberD
        # print("PISOARE = ", pisoare)

    return max(liberS, liberD), min(liberS, liberD)


if len(sys.argv)>1 and sys.argv[1]:
    inputFile = sys.argv[1]
else:
    inputFile = "test_input.txt"

read_input(inputFile)
