

in_file = open("B-small.in","r");
out_file = open("B.out","w");
casenum = 0;

for line in in_file:
    if (casenum == 0):
        casenum += 1
        continue
    splits = line.split(" ")
    scores = [];
    n = 0
    s = 0
    p = 0
    ans = 0
    for x in xrange(0,len(splits)):
        tmp = int(splits[x])
        if (x == 0):
            n = tmp
        elif (x == 1):
            s = tmp
        elif (x == 2):
            p = tmp
        else:
            scores.append(tmp)
    triplets = []
    for score in scores:
        q = score / 3
        r = score % 3
        tmp = [q,q,q]
        if (q >= p or (q+1 == p and r > 0)):
            ans += 1
            continue #don't need to run this case any more
        if (q+2 < p):
            continue #impossible to reach goal
        if (r == 1):
            continue #impossible to increase e.g. 7,8,7 can't have a 9
        if (q+2 == p and r == 2 and s > 0):
            ans += 1
            s -= 1
            continue # we can get a score using a surprise result
        if (q+1 == p and q > 0 and r == 0 and s > 0):
            ans += 1
            s -= 1
            continue # we can get a score using a surprise result
        # can't make it if you reach this case
    print ans
    out_file.write("Case #"+str(casenum)+": "+str(ans)+"\n")
    casenum += 1;

out_file.close()
