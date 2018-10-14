T = int(raw_input());
for q in range(T):
    [N, P] = map(int, raw_input().split());
    data = map(int, raw_input().split());

    mods = [0]*P;
    for d in data:
        mods[d%P] += 1;

    print "Case #%d:" % (q+1),
#    print "%.9f" % Solve(K, pancakes);

    Ans = mods[0];
    mods[0] = 0;

    if P == 2:
        Ans += (mods[1]+1)/2;
    if P == 3:
        common = min(mods[1], mods[2]);
        Ans += common;
        mods[1] -= common;
        mods[2] -= common;
        left = mods[1] + mods[2];
        Ans += (left+2)/3;

    if P == 4:
        Ans += mods[2]/2;
        mods[2] -= (mods[2]/2) * 2;

        common = min(mods[1], mods[3]);
        Ans += common;
        mods[1] -= common;
        mods[3] -= common;

        if (mods[2] == 1) and (max(mods) >= 2):
            mods[2] = 0
            mods[1] -= 2;
            mods[3] -= 2;
            Ans += 1;

        while (mods[1] > 4):
            Ans += 1;
            mods[1] -= 4;
        while (mods[3] > 4):
            mods[3] -= 4;
            Ans += 1;

        if max(mods) > 0:
            Ans += 1;
            
    print Ans
