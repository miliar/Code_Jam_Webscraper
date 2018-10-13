T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    naomi_l = sorted(map(float, raw_input().split()), reverse=True, key=float)
    ken_l = sorted(map(float, raw_input().split()), reverse=True, key=float)    

    naomi_l2 = list(naomi_l)
    ken_l2 = list(ken_l)
    # Play Deceitful War optimally
    score_dw = 0
    while len(naomi_l)!=0:
        if naomi_l[0]>ken_l[0]:
            score_dw += 1
            naomi_l.pop(0)
            ken_l.pop(0)
        else:
            naomi_l.pop()
            ken_l.pop(0)
            
    # Play War optimally
    score_w = 0
    while len(naomi_l2)!=0:
        if ken_l2[0]<naomi_l2[0]:
            score_w += 1
            ken_l2.pop()
            naomi_l2.pop(0)
        else:
            ken_l2.pop(0)
            naomi_l2.pop(0)
    print "Case #"+str(i+1)+": "+str(score_dw)+" "+str(score_w)
