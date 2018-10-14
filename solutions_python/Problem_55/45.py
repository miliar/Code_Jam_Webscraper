def next(i, n) :
    if n==i+1 :
        return 0
    return i+1

#def addex(a, b, n) :
#    return (a+b)%n

def scan_groups(groups, k) :
    assert len(groups) > 0
    cap = []
    
    n = len(groups)
    
    sum = 0
    start = 0
    curr_count = 0

    while start < n :
        next_end = (start+curr_count)%n
        
        advance_start = False
        if curr_count == n :
            advance_start = True
        if sum + groups[next_end] > k :
            advance_start = True
        if advance_start :
            assert curr_count > 0
            curr_end = (start+curr_count-1)%n
            cap.append( (start, curr_end, sum) )
            sum -= groups[start]
            start += 1
            curr_count -= 1
            continue
        
        if sum + groups[next_end] <= k :
            sum += groups[next_end]
            curr_count += 1
        
    return cap

def process_case() :
    r, k, n = map(int, raw_input().split())
    groups = map(int, raw_input().split())
    assert n==len(groups)
    
    for g in groups :
        assert g <= k

    caps = scan_groups(groups, k)
    traversed = [None] * n
    rotation = []
    
    curr = 0
    while True :
        if traversed[curr] != None :
            break
        traversed[curr] = len(rotation)
        
        rotation.append(caps[curr])
        curr, end, euro = caps[curr]
        #rot_euro += euro
        
        curr = next(end, n)
        
    #if rotation[-1][1]==n-1 :
    #    print "OK"
    #else : 
    #    print "OH NO"
    
    rot_start = rotation[-1][1]
    rot_start = next(rot_start, n)
    rot_split = traversed[rot_start]
    
    #print rotation
    pre_seq = rotation[0:rot_split]
    rotation = rotation[rot_split:]
    #print pre_seq, rotation
    
    rot_euro = 0
    for a, b, e in rotation :
        rot_euro += e
    
    ps_earned = 0
    
    if r > len(pre_seq) :
        rr = r - len(pre_seq) 
        ps_earned = len(pre_seq)
    else :
        rr = 0
        ps_earned = r
    
    euro_from_pre = 0
    
    for i in range(0, ps_earned) :
        euro_from_pre += pre_seq[i][2]
        
    rot_num = rr // len(rotation)
    rem = rr % len(rotation)
    
    euro_from_rot = rot_num * rot_euro
    euro_from_rem = 0
    for i in range(0, rem) :
        euro_from_rem += rotation[i][2]

    #print "r=%d, k=%d, n=%d" % (r,k,n)
    #print groups
    #print "PreSeq: %s, count=%d" % (pre_seq, len(pre_seq))
    #print "Rotation: %s, count=%d, rot_euro=%d" % (rotation, len(rotation), rot_euro)
    #print "pre_earned=%d, rot_num=%d, rem=%d" % (ps_earned, rot_num, rem)
    #print euro_from_pre, euro_from_rot, euro_from_rem
    result = euro_from_pre + euro_from_rot + euro_from_rem
    
    return "%d" % result
    
    

case_num = int(raw_input())
for i in range(case_num) :
    result = process_case()
    print "Case #%d: %s" % (i+1, result)