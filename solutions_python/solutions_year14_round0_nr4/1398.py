__author__ = 'ml'
import numpy as np


def calccookieRate(F, numFarms):
    return 2 + numFarms * F

def solve(fname):

    lines = []
    with open(fname, "r") as myfile:
            lines = myfile.readlines()
    numCases = int(lines[0])
    baseIndex = 2



    outFileName = fname + '.results.txt'
    with open(outFileName, "w") as myfile:
            myfile.write("")
    for case in range(0,numCases):
        naomi = np.fromstring(lines[baseIndex], sep=' ')
        ken   = np.fromstring(lines[baseIndex+1], sep=' ')

        naomi = np.sort(naomi).tolist()
        ken   = np.sort(ken).tolist()

        n_w = 0
        k_w = 0
        for i in range(0,len(naomi)):
            n = naomi[i]
            mini = 0
            for k in range(0,len(ken)):
                if ken[k] > n:
                    mini = k
                    break
            k = ken[mini]
            ken.remove(k)
            if k > n:
                k_w += 1
            else:
                n_w += 1

        naomi = np.fromstring(lines[baseIndex], sep=' ')
        ken   = np.fromstring(lines[baseIndex+1], sep=' ')
        naomi = np.sort(naomi).tolist()
        ken   = np.sort(ken).tolist()
        dn_w = 0
        dk_w = 0
        #ken takes the weight least above
        #ChosenNaomi > ChosenKen if, and only if, ToldNaomi > ChosenKen
        epsilon = 0.0001
        for i in range(0,len(naomi)):
            if naomi[i] > ken[0]:
                n = ken[len(ken)-1] + epsilon
            else:
                n = ken[len(ken)-1] - epsilon
            mini = 0
            for k in range(0,len(ken)):
                if ken[k] > n:
                    mini = k
                    break
            k = ken[mini]
            ken.remove(k)
            if k > n:
                dk_w += 1
            else:
                dn_w += 1

        print(dn_w, ' ',n_w)


        with open(outFileName, "a") as myfile:
            resultString =  "Case #" + str((case+1)) +": " + str(dn_w) + ' '+ str(n_w) + '\n'
            myfile.write(resultString)
        baseIndex += 3


def solveWar():
    files = ['D-large.in','D-small-attempt0.in', 'warTest.txt']
    for file in files:
        solution = solve(file)
        print(file, ' solved!')
    return 0


solveWar()
