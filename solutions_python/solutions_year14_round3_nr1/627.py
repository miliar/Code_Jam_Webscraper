import math;
str = "A-small-attempt0.in";
fo = open(str,"r");
T = int(fo.readline());
for m in range(T):
    p, q = fo.readline().strip().split("/");
    p = int(p);
    q = int(q);
    if q % p == 0:
        q = q/p;
        p = 1;
    if (q & (q-1)==0) and (q!=0):
        if p % 2 == 0:
            print "re"
            print "Case #%d: impossible" % (m+1);  
        else:
            x = math.ceil(float(q)/p);
            result = math.ceil(math.log(x,2));
            print "Case #%d:" % (m+1), int(result);
    else:
        print "Case #%d: impossible" % (m+1);
