def Evaluate(comb, kill, data):
    ANS = [];
    Ret = "";
    
    for char in data:
        combined = False;
        cleared  = False;
        if len(ANS) == 0:
            ANS.append(char);
        else:
            prev = ANS[-1];
            for trip in comb:
                if ((prev == trip[0]) and (char == trip[1])) or ((prev == trip[1]) and (char == trip[0])):
                    ANS[-1] = trip[2];
                    combined = True;
            if not combined:
                for killer in kill:
                    if char in killer:
                        other = killer[0];
                        if other == char:
                            other = killer[1];
                        if other in ANS:
                            cleared = True;
                            ANS = [];
            if not combined and not cleared:
                ANS.append(char);

#    print ANS;
    for i in str(ANS):
        if i != "'":
            Ret += i;
    print Ret
    return;

T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    List = raw_input().split();

    Nc = int(List.pop(0));      com = [];
    for i in range(Nc):
        com.append( List.pop(0) );
    Nk = int(List.pop(0));      kil = [];
    for i in range(Nk):
        kil.append( List.pop(0) );
#    print Nc, com, Nk, kil, List
    Evaluate(com, kil, List[1]);    
    
