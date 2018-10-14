"""
Google Code Jam 2014 Round 2 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""

class IOHandlerObject(object):
    source = "a.in"
    target = "a.out"
    sfile = None
    tfile = None

    def __init__(self):
        self.sfile = open(self.source, "a+")
        self.sfile.seek(0)
        self.tfile = open(self.target, "w+")

    def getInput(self, mode=2):
        # 0: String
        # 1: List of strings
        # 2: List of integers
        inputs = self.sfile.readline().strip()
        if mode == 0:
            return inputs
        if mode == 1:
            return inputs.split()
        if mode == 2:
            return [int(x) for x in inputs.split()]

    def writeOutput(self, s="\n"):
        if isinstance(s, list): s = " ".join(s)
        s = str(s)
        self.tfile.write(s)

IOHandler = IOHandlerObject()
g = IOHandler.getInput
w = IOHandler.writeOutput

############################## SOLUTION ##############################
t = int(g(0))
for i in range(t):
    w("Case #" + str(i+1) + ": ")
    n,s = g()
    a = g()
    a.sort()
    st = 0
    ct = n-1
    while ct > st:
        while a[ct] + a[st] > s and ct > st:
            ct -= 1
        if ct > st:
            st += 1
            ct -= 1
    w(n-st)
    w()