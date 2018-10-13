import sys

# https://code.google.com/codejam/contest/3264486/dashboard

def oversized_pancake_flipper(S, K):
    D = [-1 if s == '-' else 1 for s in S]
    count = 0
    for i in range(len(D)):
        if D[i] < 0:
            count += 1
            for j in range(K):
                if i+j >= len(D):
                    return 'IMPOSSIBLE'
                D[i+j] *= -1
    return count

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        T = int(f.readline().strip())
        for i in range(T):
            S, K = f.readline().strip().split()
            K = int(K)
            print "Case #"+str(i+1)+": "+str(oversized_pancake_flipper(S, K))
