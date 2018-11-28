def compute_count(case):
    hops = int(case[0])
    hop = 1
    total_time = 0
    pos = {'O':1,
           'B':1}
    available_time = 0
    consumed_time = {'robot':'O',
                     'time': 0}
    while hop<hops*2+1:
 
        time_taken = abs(int(case[hop+1]) - pos[case[hop]]) +1
        #print "time_taken=%s"%time_taken
        actual_time = time_taken
        
        if consumed_time['robot'] == case[hop]:
            consumed_time['time'] += actual_time
        else:
            consumed_time['robot'] = case[hop]
            actual_time = time_taken - consumed_time['time']
            actual_time = actual_time if actual_time>1 else 1
            consumed_time['time'] = actual_time

        total_time += actual_time
        pos[case[hop]] = int(case[hop+1])
        hop+=2
    return total_time
        
def test_cases():
    with open("sample3.txt") as f:
        size = f.readline()
        print 'size=%s'%size
        for i,line in enumerate(f):
            #print "line=%s"%line
            print "Case #%s: %s"%(i+1,compute_count(line.split()))
test_cases()