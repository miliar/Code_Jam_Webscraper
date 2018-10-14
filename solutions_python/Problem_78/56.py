def Check(Nmax, WinD):
    if Nmax > 100:
        return "Possible"
    for d in range(1,Nmax+1):
        if (WinD*d)%100 == 0:
            return "Possible"
    return "Broken"



T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    [N, Pd, Pg] = map(int, raw_input().split());

    if ((Pg == 0) and (Pd > 0)) or ((Pg == 100) and (Pd < 100)):
        print "Broken"
    else:
        print Check(N, Pd);
    
#    print N, List;
    
