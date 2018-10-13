def outNiz(i, odg):
    return "Case #{}: {}".format(i, odg)

def obrati(sez, K):
    # ni vazn vrstni red ---> grem od leve proti desni
    # flipnem pri prvem -, ponavljam
    # ce vsi +, ok, ce je na konc kak - prevec desno ... imposibru
    k = 0
    i = 0
    while i <= len(sez) - K:
        if not sez[i]:
            sez[i:i + K] = [1 - sez[t] for t in range(i, i + K)]
            k += 1
        i += 1
    if min(sez[i:]) == 0:
        return "IMPOSSIBLE"
    else:
        return k
            

F = "A-large"
inF = F + ".in"
outF = F + ".out"
with open(inF) as f:
    T = int(f.readline().strip())
    with open(outF, "w") as g:
        for i in range(T):
            primer = i + 1
            niz, K = f.readline().strip().split(" ")
            K = int(K)
            sez = [0 if x == "-" else 1 for x in niz]
            odg = obrati(sez, K)
            print(outNiz(primer, odg), file=g)
            
        
