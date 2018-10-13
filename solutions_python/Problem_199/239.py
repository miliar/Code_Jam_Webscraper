def rflip(panlist,i):
    panlist[i] = "+" if panlist[i] == "-" else "-"
    
def flip(s,i,k):
    assert i+k <= len(s), "arg"
    for j in range(i,i+k):
        rflip(s,j)

T = int(input())
for case in range(T):
    vals = input().split()
    S,K = list(vals[0]),int(vals[1])
    
    flipcount = 0
    for c in range(len(S)-K+1):
        if S[c] == "-":
            #print(S)
            flip(S,c,K)
            flipcount += 1
    
    #print(S)
    outstr = "Case #{}: ".format(case+1)
    if all(c == "+" for c in S):
        outstr += str(flipcount)
    else:
        outstr += "IMPOSSIBLE"
    print(outstr)
    