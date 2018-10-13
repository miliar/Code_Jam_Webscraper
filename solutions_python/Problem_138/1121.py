def war(naomi, ken):
    naomi, ken = naomi[::-1], ken[::-1]
    point = 0
    for naomi_val in naomi:
        if naomi_val > ken[0]:
            point += 1
        else:
            ken.pop(0)
    return point 
def deceitful(naomi, ken):
    point = 0
    for naomi_val in naomi:
        if naomi_val >= ken[0]:
            ken.pop(0)
            point += 1
    return point
def play():
    T = int(raw_input())
    for t in range(1, T+1):
        N = int(raw_input())
        naomi = sorted(map(float, raw_input().split()))
        ken   = sorted(map(float, raw_input().split()))
        war_point = war(naomi, ken)
        deceitful_point = deceitful(naomi, ken)        
        print "Case #%d: %d %d" % (t, deceitful_point, war_point)
play()
