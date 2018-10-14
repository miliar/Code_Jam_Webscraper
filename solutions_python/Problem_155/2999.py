#! /usr/bin/python3
import sys

def opera():
    st = input();
    lis = [i for i in st.split()];
    smax = int(lis[0]);
    slist =lis[1]


    

    invite = 0;
    standing = 0;
    for s in range(0,smax+1):
        
            
        if (s <= standing):
            standing = standing + int(slist[s]);
            if (int(slist[s]) == 0 and s >= standing):
                invite=invite+1;
                standing=standing+1;
            
        else :
            print ("entered else")
    return invite;
    


t = int(input());
for a in range(0,t):
    r = opera();
    print ("Case #"+str(a+1)+": "+str(r))
