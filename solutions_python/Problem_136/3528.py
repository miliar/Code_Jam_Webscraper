from __future__ import division
import numpy as np

datafile = "B-small-attempt0.in"
outfile = "ccout.txt"

def fileread(filename):
    f = open(filename, "r")
    mainline = f.read()
    data = np.fromstring(mainline.replace("\n", " "), dtype = "float64", sep = ' ')
    foo = data[1:]
    return foo.reshape((data[0],3))

def filewrite(string, filename):
    f = open(filename, "a")
    f.write(string)
    f.close()

samplelist = fileread(datafile)
index = 0


for factories in samplelist:
    R = 2
    index += 1
    C, F, X = factories
    instep = 10000
    minn = 0
    maxn = instep
    solution = False
    while solution == False:
        enns = np.arange(minn, maxn)
        wint = X/(R+enns*F)
        Tns = C/(R+enns[:-1]*F)
        cumTns = np.cumsum(Tns)
        cumTns = np.insert(cumTns, 0, 0)
        totime = wint + cumTns
        winner = np.amin(totime)
        if winner != totime[-1]:
            solution = True
            filewrite("Case #"+str(index)+": "+str(winner)+"\n", outfile)
        else:
            minn += instep-1
            maxn += instep-1