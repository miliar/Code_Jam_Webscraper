T = input()
for i in xrange(T):
    N = input()
    Naomi = [float(j) for j in raw_input().split()]
    Ken = [float(j) for j in raw_input().split()]
    Naomi.append(2)
    Ken.append(2)
    Naomi.sort()
    Ken.sort()
    k = 0
    l = 0
    Naomi_win = 0
    Ken_win = 0
    Naomi_store = 0
    Ken_store = 0
    while (k<N) or (l<N):
        if (Naomi[k] > Ken[l]):
            Naomi_store += 1
            if Ken_store > 0:
                Ken_store -= 1
                Ken_win += 1
        else:
            Ken_store += 1
            if Naomi_store > 0:
                Naomi_store -= 1
                Naomi_win += 1

        if ((Naomi[k] > Ken[l]) and (l < N)) or (k == N):
            l += 1
        else:
            k += 1

    print 'Case #'+str(i+1)+': '+str(Naomi_win)+' '+str(N - Ken_win)

