lines = []

with open(r'e:\temp\C-small-attempt0.in', 'r') as f:
    lines = f.readlines()

num_cases = int(lines[0])
cases = []

for i in xrange(num_cases):
    r, k, n = map(int, lines[2*i+1].split())
    groups = map(int, lines[2*i+2].split())
    cases.append((r, k, groups))
    
for i, case in enumerate(cases):
    queue = case[2]
    riding = []
    euros = 0

    for n in xrange(0, case[0]):
        num_riding = 0
        idx = 0
        for group in queue:
            if num_riding + group <= case[1]:
                riding.append(group)
                num_riding += group
                idx += 1
            else:
                break
        riding = queue[0:idx]
        queue = queue[idx:]
        euros += num_riding

        queue = queue + riding

    print "Case #%d: %d" % (i+1, euros)
    
        
