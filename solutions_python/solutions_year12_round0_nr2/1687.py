import math

def resolve(f):
    sl = open(f, 'r').readlines()
    f_out = open("output", "w")
    t, sl = int(sl[0]), sl[1:]
    for i in range(t):
        posible_s_triples = 0
        result = 0
        stp = sl[i].split()
        n = int(stp[0])
        s = int(stp[1])
        p = int(stp[2])
#        print "Caso", i + 1
        for j in stp[3:]:
            n = int(j)
            k = n/3
            if p <= k or ((n%3 != 0) and (p == k + 1) and (p <= n)):
#                print "sumo 1: n=", n, "p=",p, "k=", k, "mod=", n%3, "s=", s
                result += 1
                
            elif ((n%3 == 2) and (p == k+2)) or ((n%3 == 0) and (p == k + 1) and (p <= n)):
#                print "sumo 1 (s): n=", n, "p=",p, "k=", k, "mod=", n%3,"s=", s
                posible_s_triples += 1
                
        result = result + min(posible_s_triples, s)
        
        f_out.write("Case #" + str(i+1) + ": " + str(result) + "\n")
        
    f_out.flush()
    f_out.close()
        
