from numpy import *

T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    N = int(raw_input());
    List = map(int, raw_input().split());
    XOR = 0;
    for el in List:
        XOR = XOR^el;
    if (XOR == 0):
#        Slist = sort(List); 
#        for i in range(N-1):
#            if Slist[i] == Slist[i+1]:
#                List.append(0);             # Sean gets everything            
        print sum(List)-min(List);
    else:
        print "NO"
