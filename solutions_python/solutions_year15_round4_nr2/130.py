import numpy as np

def solveB(V, X, R, C) :
    if np.min(C) > X: return -1
    if np.max(C) < X : return -1

    N = len(R)
    if N == 1:
        t0 = V/R[0]
        x0 = C[0] * t0
        return t0

    A = np.zeros((2, N), dtype = np.float64)
    for i in range(N):
        A[0, i] = R[i]
        A[1, i] = (C[i]*R[i])

    if np.linalg.det(A) != 0:
        x = np.linalg.pinv(A)
        y = np.array([[V],[X*V]])
        x = np.dot(x, y)
        return np.max(x)
    else :
        if C[0] == C[1]:
            return V/(R[0] + R[1])
        if R[1] > R[0] and C[1] == X:
            return V/R[1]
        if R[0] > R[1] and C[0] == X:
            return V/R[0]
        if C[0] == X:
            return V/R[0]
        if C[1] == X:
            return V/R[1]
        else :
            return -1

def solve(in_filename, out_filename):
    with open(in_filename, 'r') as file, open(out_filename, 'w') as ofile :
        T = int(file.next())
        for case in range(0, T) :

            line = file.next()
            tok = line.split()
            N = int(tok[0])
            V = float(tok[1])
            X = float(tok[2])

            R = []
            C = []
            for i in range(N):
                line = file.next()
                tok = line.split()
                R.append(float(tok[0]))
                C.append(float(tok[1]))

            if case + 1 == 4 :
                print V, X, R, C

            sol = solveB(V, X, R, C)
            if sol == -1 :
                ofile.write("Case #%d: IMPOSSIBLE\n"%(case+1))
            else:
                ofile.write("Case #%d: %.9f\n"%(case+1, sol))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '.out'
    solve(input, output)
