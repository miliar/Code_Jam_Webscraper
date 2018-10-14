# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

p=[]
t = int(raw_input())  # read a line with a single integer
for a in range(1, t + 1):
    G=[]
    D, N=raw_input().split()
    for b in range(1, int(N) + 1):
        K, S=raw_input().split()
        R=(int(D)-int(K))/float(S)
        G.append(R)
    if max(G)!=0:
        Q=float(D)/max(G)
    p.append('Case #' + str(a) + ': ' + str(Q))
for g in p:
    print g
