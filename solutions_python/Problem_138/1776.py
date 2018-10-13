def Naomi(KK, NK):
    if len(KK) == 1:
        N = NK.pop()
        K = KK.pop()
        if N > K:
            NP = 1
        else:
            NP = 0
        return N, N, NP, K
    mk = max(KK)
    smk = max(KK - set([mk]))
    if mk > max(NK):
        NT = (mk + smk) / 2
        N = min(NK)
        NP = 0
        K = mk
    else:
        N = max(NK)
        N = min([x for x in NK if x > min(KK)])
        NT = N
        NP = 1
        K = min(KK)

    return NT, N, NP, K

def Ken(N, KK):
    vk = [x for x in KK if x > N]
    if len(vk) < 1:
        K = min(KK)
        KP = 0
    else:
        K = min(vk)
        KP = 1
    return K, KP

def War(NK, KK):
    TNP = 0
    TKP = 0
    while NK:
        N = NK.pop()
        K, KP = Ken(N, KK)
        KK = KK - set([K])
        TKP = TKP + KP
        TNP = TNP + 1 - KP
    return TNP

f = open("C:/Users/tadeo/Downloads/D-small-attempt0.in","r")
fw = open("C:/Users/tadeo/Downloads/D.out", "w")
T = int(f.readline())
for i in range(T):
    N = int(f.readline())
    NK = [float(x) for x in f.readline().split(" ")]
    KK = [float(x) for x in f.readline().split(" ")]
    w = War(set(NK), set(KK))
    dw = 0
    KK = set(KK); NK = set(NK)
    while NK:
        NT, N, NP, K = Naomi(KK, NK)
        dw = dw + NP
        NK = NK - set([N])
        KK = KK - set([K])
    fw.write("Case #"+str(i+1)+": "+str(dw)+" "+str(w)+"\n")
f.close()
fw.close()

