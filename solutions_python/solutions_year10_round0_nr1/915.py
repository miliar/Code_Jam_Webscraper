cases = input()

def index(l, v):
    for k in range(len(l)):
        if (l[k]==v):
            return k
    return -1

for c in range(cases):
    n, k = map(int, raw_input().split())
    state = [False for l in range(n)]
    power = [False for l in range(n)]
    power[0] = True

    #print "state", state
    #print "power",power
    #print "--"
    
    for snap in range(k):

        no_power_index = index(power, False)
        if (no_power_index == -1): no_power_index = len(power)
        #print "got power until:", no_power_index
        for l in range(no_power_index):
            state[l] = not state[l]

        off_index = index(state, False)
        if (off_index == -1): off_index = len(state)
        #print "go on until:", off_index
        for l in range(len(state)):
            power[l] = (l <= off_index)
                
                
        #print "state", state
        #print "power",power
        #print "--"
        
    #print "state", state
    #print "power",power

    if (all(power) and all(state)):
        final = "ON"
    else:
        final = "OFF"
        
    print "Case #" + str(c+1) + ":", final

