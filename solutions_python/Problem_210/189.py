T = int(raw_input())

for t in range(1, T+1):
    AC, AJ = map(int, raw_input().split())
    C = []
    J = []
    for c in range(AC):
        C.append(map(int, raw_input().split()))
    for j in range(AJ):
        J.append(map(int, raw_input().split()))
    
    # print C, J
    
    if AC < 2 and AJ < 2:
        ans = 2
    else:
        if AJ == 2:
            C, J = J, C
            AC, AJ = AJ, AC
        
        # now AC == 2
        # print C
        ans = 4
        for i in range(2):
            # print (C[i][1] - C[1-i][0] + 1440) % 1440
            if (C[i][1] - C[1-i][0] + 1440) % 1440 <= 720:
                ans = 2
        
    
    print 'Case #%d: %d' % (t, ans)
