import sys

def pancakeflip(stri,n):
    k = len(stri)
    stri = list(stri)
    i = 0
    res = 0
    print(k)
    while i < k-n+1:
        nakonc = 1
        if stri[i] == "-":
            nakonc = None
            res += 1
            kolk = 0
            for j in range(n):
                if stri[i+j] == "-":
                    stri[i+j] = "+"
                    kolk+=1
                else:
                    stri[i+j] = "-"
                    if nakonc is None:
                        nakonc = kolk
            if nakonc is None:
                nakonc = kolk
            print(stri)
        i+=nakonc
    for i in range(1,n+1):
        if stri[-i] == "-":
            return "IMPOSSIBLE"
    return str(res)

#print(pancakeflip("--++-++--",5))


T = int(sys.stdin.readline())
res = ""
for k in range(T):
    i,j = sys.stdin.readline().split()
    j = int(j)
    res1 = pancakeflip(i,j)
    res1 = "Case #{0}: {1}".format(k+1,res1)
    print(res1)
    res+= (res1+"\n")
with open("fliper_A_LARGE.out","w") as izhod:
    izhod.write(res)