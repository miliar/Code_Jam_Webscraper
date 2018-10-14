from decimal import Decimal
cases = int(input())
for case in range(1,cases+1):
    dn = input().split()
    d = int(dn[0])
    n = int(dn[1])
    positions = []
    horses = {}
    
    for i in range(n):
        ks = input().split()
        positions.append(int(ks[0]))
        horses[ks[0]] = int(ks[1])
        
    positions.sort()
    limit = -1
    for i in range(n-1):
        h1 = positions[i]
        h2 = positions[i+1]
        s1 = horses[str(h1)]
        s2 = horses[str(h2)]
        tmp = Decimal(h1*s1/(d-h1)) + Decimal(s1)
        if s1>s2:
            tmp1 = Decimal(h1*(s1-s2)/(h2-h1)) + Decimal(s1)
            if tmp1 > tmp:
                tmp = tmp1
            
        if limit == -1 or limit>tmp:
            limit = tmp
            
    h_last = positions[-1]
    s_last = horses[str(h_last)]
    tmp = Decimal(h_last*s_last/(d-h_last)) + Decimal(s_last)
    
    if limit == -1 or limit>tmp:
        limit = tmp
    print('Case #{0}: {1:.6f}'.format(case, limit))