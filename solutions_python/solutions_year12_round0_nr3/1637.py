ls=open("C-small-attempt0.in").readlines()
T = int(ls[0])
for i in range(1,T+1):
    n_pairs=0
    sols = []
    line = ls[i].split()
    A = line[0]
    B = line[1]
    if len(A) == 1 and len(B) == 1:
        print "Case #%d: %d" % (i, n_pairs)
        continue
    for n in range(int(A), int(B)):
        str_n = str(n)
        for l in range(1,len(str_n)):
            test_str_n = str_n[l:len(str_n)] + str_n[0:l]
            test_n = int(test_str_n)
            if test_n <= int(B) and n < test_n and not (n,test_n) in sols:
                sols.append((n,test_n))
                n_pairs += 1
    print "Case #%d: %d" % (i, n_pairs)
