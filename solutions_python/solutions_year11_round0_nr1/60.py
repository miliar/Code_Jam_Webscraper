def Run(order, blue, orange):
    posO = 1;       posB = 1;
    Time = 0;
    blue.append(0);
    orange.append(0);
    while True:
        Time += 1;
        Pushed = False;
        movedO = False;
        movedB = False;

        if (posO != orange[0]):
            posO += (orange[0]-posO)/abs(orange[0]-posO);
            movedO = True;
        if (posB != blue[0]):
            posB += (blue[0]-posB)/abs(blue[0]-posB);
            movedB = True;

        if (order[0] == 'O') and (movedO == False):
            Pushed = True;
            orange.pop(0);
            order.pop(0);
            if len(order) == 0:
                return Time
        if (order[0] == 'B') and (movedB == False) and not Pushed:
            blue.pop(0);
            order.pop(0);
            if len(order) == 0:
                return Time

    

T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    List = raw_input().split();
    N = int(List.pop(0))
    Atlas = [];
    Pbody = [];
    Glados= [];
#    print " "
    for n in range(N):
        Glados.append( List.pop(0) );
        if Glados[-1] == "O":
            Pbody.append( int(List.pop(0)) );
        else:
            Atlas.append( int(List.pop(0)) );
    print Run (Glados, Atlas, Pbody)
#    print N, List;
    
