### Google code jam 2015
### Round 2
### Problem B: kiddie pool


Cases = int(raw_input());
for i in range(Cases):
    print "Case #%d:" % (i+1),

    Taps = [];
    [N, V, X] = map(float, raw_input().split());
    N = int(N);
    V = float(V*10000);
    X = float(X*10000);

    nHot = 0;
    nCold = 0;
    nExact = 0;
    rExact = 0;
    
    for j in range(N):
        data = map(float, raw_input().split());
        Taps.append([data[0]*10000, data[1]*10000 - X]);

        if (Taps[-1][1] > 0):
            nHot += 1;
        if (Taps[-1][1] < 0):
            nCold += 1;
        if (Taps[-1][1] == 0):
            rExact += Taps[-1][0];
            nExact += 1;

    if (nHot == N) or (nCold == N):     # All too hot or too cold;
        print "IMPOSSIBLE";
        continue;
    if (nHot == 0) or (nCold == 0):     # Use just exact taps
        print V / rExact;
        continue;

    ### Simple case, 2 taps left, 1 hot, 1 cold
    if Taps[0][1] > 0:
        rHot = Taps[0][0];
        tHot = Taps[0][1];
        rCold = Taps[1][0];
        tCold = Taps[1][1];
    else:
        rHot = Taps[1][0];
        tHot = Taps[1][1];
        rCold = Taps[0][0];
        tCold = Taps[0][1];

    timeH = V / rHot / (1 - tHot/tCold);
    timeC = V / rCold / (1 - tCold/tHot);

    print max(timeH, timeC);
        
    

