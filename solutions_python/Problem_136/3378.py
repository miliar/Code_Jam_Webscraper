


"""
INPUT
num of test cases
C F X
.....

Normal rate = 2 per second
C = Cost of farm
F = Additional cookies per second for farm
X = Number of cookies to win
"""
fd = open("B-small-attempt0.in","r")

lines = fd.readlines()

T = int(lines[0])

pos = 1;
for prob_num in range(T):
    print("Case #" + str(prob_num+1) + ": ",end="")
    parts = lines[pos].split(' ')
    C = float(parts[0]);
    F = float(parts[1]);
    X = float(parts[2]);
    pos += 1
    #print("C:"+str(C)+"\tF:"+str(F) + "\tX:"+str(X))

    #every branch has a rate, and a value, and a time
    #lowest rate stored first
    branch_pos = 0;
    active_branches = 1;
    branches = [(2.0, 0, 0)]
    active = True;
    lowest = 1000000;
    while(active):
        active = False;
        #print("Looping out");
        #set up
        for i in range(0, len(branches)):
            (rate,value,time) = branches[i];
            if (value >= X):
                continue;
            if (time > lowest):
                continue;
            active = True;
            #direct time
            direct_t = (X-value)/rate;
            #factory time
            factory_t = (C-value)/rate;
            #print("ID:" + str(i) + "\tTime:" + str(time) + "\tDetect:" + str(direct_t) + "\tFactory:" + str(factory_t))
            branches[i] = (rate, X, time + direct_t);
            if (factory_t < direct_t):
                branches.append((rate+F,0,time + factory_t));

            if (time + direct_t < lowest):
                lowest = time + direct_t;

    print("%0.7f" % lowest);         

fd.close()
