import random
import time

def gen(l=1000,x=1000):
    L = random.randint(1, l)
    X = random.randint(1, x)
    s = ""
    whatever = ["i", "j", "k"]
    for i in range(L):
        s += whatever[random.randint(0, 2)]
    return s * X

quatTab = { "1":  {"1" : "1",  "-1" : "-1", "i" : "i",  "-i" : "-i", "j" : "j",  "-j" : "-j", "k" : "k",  "-k" : "-k"},
            "-1": {"1" : "-1", "-1" : "1",  "i" : "-i", "-i" : "i",  "j" : "-j", "-j" : "j",  "k" : "-k", "-k" : "k"},
            "i":  {"1" : "i",  "-1" : "-i", "i" : "-1", "-i" : "1",  "j" : "k",  "-j" : "-k", "k" : "-j", "-k" : "j"},
            "-i": {"1" : "-i", "-1" : "i",  "i" : "1",  "-i" : "-1", "j" : "-k", "-j" : "k",  "k" : "j",  "-k" : "-j"},
            "j":  {"1" : "j",  "-1" : "-j", "i" : "-k", "-i" : "k",  "j" : "-1", "-j" : "1",  "k" : "i",  "-k" : "-i"},
            "-j": {"1" : "-j", "-1" : "j",  "i" : "k",  "-i" : "-k", "j" : "1",  "-j" : "-1", "k" : "-i", "-k" : "i"},
            "k":  {"1" : "k",  "-1" : "-k", "i" : "j", "-i" : "-j",  "j" : "-i", "-j" : "i",  "k" : "-1", "-k" : "1"},
            "-k": {"1" : "-k", "-1" : "k",  "i" : "-j",  "-i" : "j", "j" : "i",  "-j" : "-i", "k" : "1",  "-k" : "-1"}
    }

def quat(q):
    prod = "1"
    for n in q:
        prod = quatTab[prod][n]
    return prod

def isCorrect(s):
    correct = False
    if quat(s) != "-1":
        return False
    
    for split1 in range(1, len(s)):
        for split2 in range(split1+1, len(s)):
            i = s[:split1]
            if quat(i) == "i":
                j = s[split1:split2]
                if quat(j) == "j":
                    k = s[split2:]
                    if quat(k) == "k":
                        return True
                
    return False


def do_stuff(inp, i, X):
    a = ""
    if len(inp) == 1:
        a = "NO"

    elif inp == inp[0] * len(inp):
        a = "NO"

    else:
        s = inp * X
        if isCorrect(s):
            a = "YES"

        else:
            a = "NO"

    print("Case #%d: %s" % (i, a))

inp = """INPUT_HERE""".split('\n')
T = int(inp[0])
inp = inp[1:]

for i in range(0, len(inp), 2):
    X = int(inp[i].split(' ')[1])
    s = inp[i+1]
    do_stuff(s, (i / 2) + 1, X)

s = "k" * 6466



























