T = int(raw_input())
for q in range(T):
    need = 0
    stand = 0
    smax, aud = raw_input().split()
    aud = map(int, list(aud))
    k = 0
    for shy in aud:
        if stand < k and shy: 
            need += k - stand
            stand += k - stand
        stand += shy
        k += 1
    print "Case #"+str(q+1)+":", need
