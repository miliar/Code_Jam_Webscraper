
cases = 0
total = 0

def mprint(cost):
    print "Case #%d: %f" % (total - cases + 1, cost) 

def get_win(cc, ff, xx):
    if xx == 2.0:
        mprint(xx/2.0)
        return

    farm = 0
    incr = 2.0
    
    pre_cost = xx / incr
    pre_cc_cost = 0.0

    while 1:
        farm += 1
        pre_incr = incr
        incr = 2.0 + float(farm) * ff
        
        pre_cc_cost = cc / pre_incr + pre_cc_cost
        cur_cost = xx / incr + pre_cc_cost

        if cur_cost > pre_cost:
            mprint(pre_cost)
            return
        pre_cost = cur_cost


while 1:
    try:
        raw = raw_input()
    except: break
    if not cases: 
        cases = int(raw)
        total = cases
        continue
    cc, ff, xx = [float(n) for n in raw.split()] 
    get_win(cc, ff, xx)
    cases -= 1
    
    
