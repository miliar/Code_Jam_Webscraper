def compute(case):
    hops = int(case[0])
    hop = 1
    total_time = 0
    pos = {'O':1,
           'B':1}
    available_time = 0
    consumed = {'robot':'O',
                     'time': 0}
    while hop<hops*2+1:
 
        time = abs(int(case[hop+1]) - pos[case[hop]]) +1
        actual_time = time
        
        if consumed['robot'] == case[hop]:
            consumed['time'] += actual_time
        else:
            consumed['robot'] = case[hop]
            actual_time = time - consumed['time']
            actual_time = actual_time if actual_time>1 else 1
            consumed['time'] = actual_time

        total_time += actual_time
        pos[case[hop]] = int(case[hop+1])
        hop+=2
    return total_time
        
def test_cases():
    with open("sample3.txt") as f:
        size = f.readline()
        print 'size=%s'%size
        for i,line in enumerate(f):
            print "Case #%s: %s"%(i+1,compute(line.split()))
test_cases()
