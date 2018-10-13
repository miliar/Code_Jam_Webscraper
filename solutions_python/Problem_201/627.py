# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for tt in xrange(1, t + 1):
    
    s = (raw_input())
    [N,x]= (s.split(" "))
    N = int(N)
    x = int(x)
    l=(N)/2
    lc = 1
    r = (N-1)/2
    rc = 1
    if(x == 1):
        print "Case #{}: {} {}".format(tt, l, r)
   
    else:
        x = x-1
        while(l!=0 and r!=0 and x!=1 and x > lc + rc):
            x = x - lc -rc;
            l1 = (l-1)/2;
            l1c = lc;
            l2  = (l)/2;
            l2c = lc;
            r1 = (r-1)/2;
            r1c = rc;
            r2 = r/2;
            r2c = rc;
            l = l1;
            lc = l1c;
            rc = 0;
            if(l1 == l2):
                lc = lc +l2c;
            else:
                r = l2;
                rc = rc+ l2c;
                
                
            if(l1 == r1):
                lc = lc +r1c
            else:
                r = r1;
                rc = rc + r1c;
                
            if(l1 == r2):
                lc = lc +r2c;
            else:
                r = r2;
                rc = rc + r2c;
                
            if(rc == 0):
                rc = lc/2;
                r = l;
                lc  = lc/2;
            if(l<r):
                temp = l
                l = r
                r = temp
                temp = rc
                rc = lc
                lc = temp

                
#printf("X : %d L: %d LC: %d, R: %d, RC: %d\n",x,l,lc,r,rc);

        if(x <= lc ):
            print "Case #{}: {} {}".format(tt, l/2, max(0,(l-1)/2))
            # cout<<l/2<<" "<<max(0,(l-1)/2)<<endl;
        else:
             print "Case #{}: {} {}".format(tt, r/2, max(0,(r-1)/2))
#                cout<<r/2<<" "<<max(0,(r-1)/2)<<endl;

# check out .format's specification for more formatting options
