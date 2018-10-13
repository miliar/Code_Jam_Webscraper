#!/usr/bin/env python

import string

T = int(raw_input())

for t in range(1, T+1):
    print "Case #%d:" % t
    
    In = raw_input()
    data = In.split(" ");

    C = int(data.pop(0))
    CL = []
    for i in range(C):
        CL += [data.pop(0)]

    D = int(data.pop(0))
    DL = []
    for i in range(D):
        DL += [data.pop(0)]

    N = int(data.pop(0))
    myStr = data.pop(0)    
    result =[]
    

    for ch in myStr:
        T = True
        if len(result)!=0:
            for com in CL:            
                cc = result.pop()
                if (cc+ch in com) or (ch+cc in com):
                    result.append(com[2])
                    T = False
                    break
                else:    
                    result.append(cc)
            if T:
                for opp in DL:
                    if ch==opp[0]:
                        if opp[1] in result:
                            T = False
                            del result[:]
                            break
                    elif ch==opp[1]:
                        if opp[0] in result:
                            T = False
                            del result[:]
                            break
                    else:
                        pass
    
                if T:
                    result.append(ch)
            print result
        else:
            result.append(ch)
        print result    





