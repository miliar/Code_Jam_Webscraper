import fileinput
import sys

def process_input():
    tc_in = fileinput.input()
    tc_count = int(tc_in.readline())
    for i in range(tc_count):
        N, K, B, T = (int(x) for x in tc_in.readline().split())
        X = [B-int(x) for x in tc_in.readline().split()]
        V = [int(x) for x in tc_in.readline().split()]
        print "Case #%d: %s" % (i+1, solve(N,K,B,T,X,V))

def solve(N, K, B, T, X, V):
    no_chance = []
    has_chance = []
    for i in range(N):
        if (T * V[i]) < X[i]:
            no_chance.append(i)
        else:
            has_chance.append(i)
    if len(has_chance) < K:
        return "IMPOSSIBLE"

    swaps = 0
    for i in has_chance[-K:]:
        for j in range(i,N):
            if j in no_chance:
                swaps+=1
    return str(swaps)

def main():
    process_input()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
