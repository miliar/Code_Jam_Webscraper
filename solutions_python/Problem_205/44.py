#from collections import Deque
def fight(Hd, Ad, Hk, Ak, B, D):
    q = []#collections.Deque();
    q.append((Hd, Ad, Hk, Ak, 0))
    exist = set()#.append((Hd, Ad, Hk, Ak))
    while q:
        current = q.pop(0)
        Hdc = current[0]  
        Adc = current[1] 
        Hkc = current[2] 
        Akc = current[3]
        turn = current[4]
        if ((Hdc,Adc,Hkc,Akc) in exist):
            continue
        else:
            exist.add((Hdc,Adc,Hkc,Akc))
        if (Hkc <= Adc):
            return turn + 1
        if (Hdc > Akc):
            q.append((Hdc - Akc, Adc, Hkc - Adc, Akc, turn + 1))
            if B > 0:
                q.append((Hdc - Akc, Adc + B, Hkc, Akc, turn + 1))
            if D > 0:
                att = max(Akc - D, 0);
                q.append((Hdc - att, Adc, Hkc, att, turn + 1))
        else:
            q.append((Hd - Akc, Adc, Hkc, Akc, turn + 1))
            if D > 0:
                att = max(Akc - D, 0);
                if (Hdc > att):
                    q.append((Hdc - att, Adc, Hkc, att, turn + 1))
    return -1









T = int(raw_input())  

for K in xrange (T):
    Hd, Ad, Hk, Ak, B, D= [int(g) for g in raw_input().split(" ")]

    ans = fight(Hd, Ad, Hk, Ak, B, D)
    if ans > 0:
        print "Case #{}: {}".format(K+1, ans)
    else:
        print "Case #{}: {}".format(K+1, 'IMPOSSIBLE')

