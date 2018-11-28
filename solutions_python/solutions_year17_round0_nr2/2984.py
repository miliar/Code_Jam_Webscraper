def outNiz(i, odg):
    return "Case #{}: {}".format(i, odg)

def zadnje(n):
    # lahko ima isto mest kot n ali pa eno manj
    # ce isto mest:
    #      43242 ---> 4... 43 ne 3..3x 22222 ok
    #      132 ---> 1..3x 1..2..9
    # ce manj: 99999
    def pomo(sez, kakManjsi):
        # delna resitev: sez je trenutni seznam
        i = len(sez) # kam postavlas
        if i == len(n):
            return sez
        mini = 1 if i == 0 else sez[-1]
        maxi = 9 if kakManjsi else n[i]
        for j in range(maxi, mini - 1, -1):
            podaljsan = pomo(sez + [j], kakManjsi or j < maxi)
            if podaljsan is not None:
                return podaljsan
        return None
        
    if len(n) == 1:
        return n[0]
    elif 0 in n:
        maksi = 0
        for t in n:
            if t == 0:
                if maksi == 1:
                    # print(n, "vracam")
                    return "9" * (len(n) - 1)
                else:
                    break
            else:
                maksi = max(maksi, t)
        # return "{}{}".format(n[0] - 1 if n[0] > 1 else "", "9" * (len(n) - 1)) 
    u = pomo([], False)
    try:
        return "".join(str(t) for t in u)
    except:
        print(n)

def brute(n):
    def isok(i):
        a = [x for x in str(i)]
        return sorted(a) == a
    n = int("".join(str(t) for t in n))
    for i in range(n, 0, -1):
        if isok(i):
            return i


F = "B-large"
inF = F + ".in"
outF = F + ".out"
with open(inF) as f:
    T = int(f.readline().strip())
    with open(outF, "w") as g:
        for i in range(T):
            primer = i + 1
            # print(primer)
            N = [int(stevka) for stevka in f.readline().strip()]
            odg = zadnje(N)
            print(outNiz(primer, odg), file=g)
