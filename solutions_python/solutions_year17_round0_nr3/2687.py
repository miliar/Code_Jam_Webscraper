for T in range(1, int(raw_input()) + 1):
    m1 = 0
    m2 = 0
    sn, p = map(int,(raw_input().split()))
    s = [sn]   
    i=0
    while i < p:
        ss = max(s)
        id = s.index(ss)        
        if ss%2 == 1:
            m1 = ss//2
            m2 = ss - m1 - 1
        else:
            m1 = ss//2 - 1
            m2 = ss - m1 - 1        
        if m1 == 0:
            s = s[:id] + [m2] + s[id + 1:]
        elif m2 == 0:
            s = s[:id] + [m1] + s[id + 1:]
        else:
            s = s[:id] + [m1] + [m2] + s[id + 1:] 
        i += 1
    print('Case #'+str(T)+': '+ str(m2) + ' '+ str(m1))