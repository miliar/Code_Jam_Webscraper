import sys

T = int(sys.stdin.readline())

for t in range(T):
    C, F, X = sys.stdin.readline().split()
    C = float(C)
    F = float(F)
    X = float(X)

    A = float("inf")
    current_T = 0.0
    n_f = 0
    while current_T < A:
        output = n_f * F + 2.0
        A = min(A, current_T + X / output)
        current_T += C / output
        n_f += 1
    print "Case #%d: %.7f"%(t+1, A)
