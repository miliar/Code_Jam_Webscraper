INPUT = {
    'config': ('int', 'linearray')
}

TEST = ('''\
3
2 20 8 2 3 5
1 4 2 2 10 4
1 100 3 1 5
''','''\
Case #1: 54
Case #2: 20
Case #3: 30
''')

def memoized(fn):
    __mem = dict()
    def mem_fn(*args):
        v = None
        if (__mem.has_key(args)):
            #print 'from memory'
            v = __mem[args]
        else:
            v = fn(*args)
            __mem[args] = v
        return v
    return mem_fn

def main(config):
    L, t, N, C = config[0:4]
    a = config[4:]
    cycles = 0
    
    # compute L-bound
    n,x = 0,0
    while n < N and x <= t:
        x = x + a[n % C] * 2
        n = n + 1
    LBOUND = n - 1
    
    @memoized
    def travel_time(i,j):
        t = 0
        star = i
        while star < j:
            t = t + a[star % C] * 2
            star = star + 1
        return t
    
    def calculate_time(L_plan):
        star = LBOUND
        if star == N:
            #print "final star reached already"
            return total_time
            
        total_time = travel_time(0, LBOUND)
        #print "travel unboosted to", LBOUND, "taking",travel_time(0, LBOUND)
        time_left = t - total_time   # time left till finising light boosters
        #print L_plan
        if star in L_plan:
            #print time_left
            remaining_dist = a[star % C] - (time_left / 2)
            total_time = total_time + time_left + remaining_dist
            #print time_left + remaining_dist
            L_plan.remove(star)
            star = star + 1
            
        total_time = total_time + travel_time(star, N)
        for L_star in L_plan:
            total_time = total_time - a[L_star % C]
        return total_time
        
    
    # calculate!
    min = travel_time(0,N)
    if L == 2:
        for i in range(LBOUND,N):
            print i,
            for j in range(i+1, N):
                cycles = cycles + 1
                time = calculate_time([i,j])
                if min == None or time < min:
                    min = time
    elif L == 1:
        for i in range(LBOUND,N):
            cycles = cycles + 1
            time = calculate_time([i])
            if min == None or time < min:
                min = time
    elif L == 0:
        min = calculate_time([])
    
    print "cycles", cycles
    return min