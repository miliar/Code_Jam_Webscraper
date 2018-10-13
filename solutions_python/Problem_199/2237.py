from sys import argv

f = open(argv[1])
out = open(argv[2], "w")

for T in range(int(f.readline().strip())):
    S, K = f.readline().strip().split(" ")
    K = int(K)
    S = map({"-": 0, "+": 1}.get, S) 
    l = len(S)
    flipps = 0
    for pos in range(l-K+1):
        if S[pos] == 0:
            flipps += 1
            for k in range(K):
                S[pos + k] ^= 1
                
    print S
    if all([s==1 for s in S]):
        res = flipps
    else:
        res = "IMPOSSIBLE"
    out.write("Case #{}: {}\n".format(T+1, res))

    
