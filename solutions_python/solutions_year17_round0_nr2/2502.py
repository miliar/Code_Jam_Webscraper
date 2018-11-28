import numpy as np

def isCorrect(N):
    for i in range(1, len(N)):
        if N[i - 1] > N[i]:
            return False

    return True

def fix(N):
    for i in range(len(N) - 1, 0, -1):
        if (N[i] == 9):
             continue
        else:
            N[i] = 9
            N[i - 1] = N[i - 1] - 1
            break

    return N

def main():
    """B"""

    name = "B/B-large"

    fin = open(name + ".in", "r")
    fout = open(name + ".out", "w")

    T = int(fin.readline())
    
    for i in range(0, T):
        
        N = int(fin.readline())
        
        Nstr = list(map(lambda x: int(x), list(str(N))))
        while not isCorrect(Nstr):
            fix(Nstr)
        
        fout.write("Case #{0}: {1}\n".format(i + 1, int("".join(list(map(str, Nstr))))))
                
main()