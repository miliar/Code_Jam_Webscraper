import fileinput

def solve(P, C, F, X):
    t = 0.0
    t0 = X / P
    t1 = C / P + X / (P + F)
    while t0 > t1:
        t += C / P
        P += F
        t0 = X / P
        t1 = C / P + X / (P + F)
    return t + t0

if __name__ == '__main__':
    stdin = fileinput.input()
    nprobs = int(stdin.next())
    for n in range(1, nprobs + 1):
        C, F, X = [float(c) for c in stdin.next().split()]
        print "Case #%d:" % n, solve(2.0, C, F, X)
