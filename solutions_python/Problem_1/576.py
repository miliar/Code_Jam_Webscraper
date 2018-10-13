# Cases
N = input()
for i in range(1,N+1):
    # Number of servers
    S = input()
    # Read the list of servers
    dic = {}
    for j in range(0,S):
        s = raw_input()
        dic[s] = False
    # Number of requests
    Q = input()
    # Counters
    switches = 0
    servers = 0
    for k in range(0,Q):
        request = raw_input()
        if not dic[request]:
            servers = servers + 1            
            if servers == S:
                switches = switches +1
                servers = 1
                for r in dic.keys():
                    dic[r] = False
            dic[request] = True
    
    print "Case #" + str(i) + ": " + str(switches)

