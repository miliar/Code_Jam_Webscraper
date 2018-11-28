import math

# dp[1440][721][who_start][who]

def upt(m, cm, who_start, who, w):
    '''
    global dp, ans, pre, ppp
    '''
    global dp, ans, ppp
    if m == 1440-1:
        w = (who!=who_start)+w
        if w < ans:
            ans = w
            '''
            ppp = (m, cm, who_start, w)
            pppp = pp
            '''
    elif dp[m][cm][who_start][who] > w:
        dp[m][cm][who_start][who] = w
        '''
        pre[m][cm][who_start][who] = pp
        '''

def cal(m, cm, who_start, who):
    global dp, ans
    if dp[m][cm][who_start][who] >= 2000:
        return
    w = dp[m][cm][who_start][who]
    if m == 1440-1:
        return
    else:
        if cm < 720 and em[m+1] != who:
            '''
            upt(m+1, cm+1, who_start, who, w, (m, cm, who_start, who, True))
            '''
            upt(m+1, cm+1, who_start, who, w)
        if m+1-cm < 720 and em[m+1] != (not who):
            #upt(m+1, m+1-cm+1, who_start, not who, w+1, (m, cm, who_start, who, False))
            upt(m+1, m+1-cm+1, who_start, not who, w+1)


for case in range(1, int(raw_input())+1):
    print "Case #%d: "%case, 
    ac, aj = map(int, raw_input().split())
    c = [map(int, raw_input().split()) for _ in range(ac)]
    j = [map(int, raw_input().split()) for _ in range(aj)]
    em = [2]*1440
    for a, b in c:
        for x in range(a, b):
            em[x] = 0
    for a, b in j:
        for x in range(a, b):
            em[x] = 1
    cc = 0
    dp = [[[[2000, 2000], [2000, 2000]] for k in range(721)] for i in range(1440)]
    #pre = [[[[2000, 2000], [2000, 2000]] for k in range(721)] for i in range(1440)]
    dp[0][1][0][0] = dp[0][1][1][1] = 0
    '''
    pre[0][1][0][0] = pre[0][1][1][1] = 0
    '''
    ans = 2000
    ppp = 0
    pppp = 0
    if em[0] != 2:
        who = em[0]
        dp[0][1][who][who] = 2000
    for i in range(1440):
        for j in range(721):
            cal(i, j, 0, 0)
            cal(i, j, 1, 0)
            cal(i, j, 0, 1)
            cal(i, j, 1, 1)

    print ans
    '''
    m, cm, who_start, who = ppp
    print pppp
    while pppp:
        if pppp[4] == True:
            pass
        else:
            print "%s %d %d" %(("C" if pppp[4] == 0 else 'J'), pppp[m]+1, m+1)
            m = pppp[0]-1
            who = pppp[3]
        pppp = pre[pppp[0]][pppp[1]][pppp[2]][pppp[3]]
    print "%s %d %d" %(("C" if who else 'J'), 0, m+1)
    '''







        
