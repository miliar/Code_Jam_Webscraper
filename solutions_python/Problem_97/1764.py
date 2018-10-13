test = int(raw_input())
for tc in range(1, test+1):
    inpt = raw_input()
    inpt = inpt.split()
    S = int(inpt[0])
    T = int(inpt[1])
    c = []
    for j in range(S, T):
        n = str(j)
        l = len(n)
        for x in range(1,l):
                m = n[x:]+n[:x]
                if len(m) != len(n):
                    continue
                if int(m)==int(n):
                    continue
            
                if int(m)>int(n) and int(m)<=T:
                    if [int(n), int(m)] not in c:
                        c.append([int(n), int(m)])     

    print 'Case #{0}: {1}'.format(tc, len(c))
