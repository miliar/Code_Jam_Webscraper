#!/usr/bin/python
import math;

def is_a_palin(n):
    string = str(n);
    flg = True;
    for i in range(len(string)):
        if(string[i] != string[len(string)-i-1]):
            flg = False;
            break;
    return flg;
            
def main():
    t = int(raw_input(),10);
    for k in range(t):
        #READING INPUT
        inpt = raw_input().split(' ');
        #ASSIGN FROM inpt
        inpt1 = int(inpt[0],10)
        inpt2 = int(inpt[1],10);

        p = int(math.sqrt(inpt1)-1);
        q = int(math.sqrt(inpt2)+1);
        r = 0;

        for n in range(p,q):
            if is_a_palin(n):
                m = n*n;
                if(is_a_palin(m)):
                    if((m >= inpt1) and (m <= inpt2)):
                        r = r+1;
        fp = open('fairsquare_output.txt','a')
#        print "Case #" + str(k+1) + ": " + str(r);
        fp.write("Case #" + str(k+1) + ": " + str(r)+"\n");
        
if __name__:
    main();
