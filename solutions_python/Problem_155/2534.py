
tc = int(raw_input())

for t in range(0, tc):
    s = raw_input().split()
    smax = int(s[0])
    s_table = map(int, list(s[1]))
    
    cur_shy = s_table[0]
    req_f = 0
    if cur_shy == 0:
        req_f = 1
        cur_shy = 1
    for a in range(1, len(s_table)):
        if cur_shy < a and s_table[a]:
            req_f += (a - cur_shy)
            cur_shy = a
        cur_shy += s_table[a]
        
    print "Case #%d: %d" %(t+1, req_f)
