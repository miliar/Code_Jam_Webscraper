T = int(raw_input())

def solve(N, Naomi, Ken):

    N2 = N
    Naomi2 = Naomi[:]
    Ken2 = Ken[:]
    
    WarN = 0
    DWarN = 0
    
#### WAR ####

    while N > 0:
        #print Naomi
        #print Ken
        if Naomi[0] > Ken[N-1]:
            WarN = WarN + N
            break
        else:
            for block in Ken:
                if block > Naomi[0]:
                    Naomi.remove(Naomi[0])
                    Ken.remove(block)
                    break
        N = N - 1

#### END WAR ####

#### DECEITFUL WAR ####


    while N2 > 0:
        #print N2
        #print Naomi2
        #print Ken2
        if Naomi2[N2-1] < Ken2[0]:
            break
        for block in Naomi2:
            if block > Ken2[0]:
                DWarN = DWarN + 1
                Naomi2.remove(block)
                Ken2.remove(Ken2[0])
                break
        N2 = N2 - 1

#### END DECEITFUL WAR ####
        
    return str(DWarN) + ' ' + str(WarN)

for i in xrange(1, T+1):

    N = int(raw_input())
    Naomi = sorted(map(float, raw_input().split()))
    Ken = sorted(map(float, raw_input().split()))
    N2 = N
    Naomi2 = Naomi
    Ken2 = Ken
    
    print 'Case #' + str(i) + ': ' + str(solve(N, Naomi, Ken))
