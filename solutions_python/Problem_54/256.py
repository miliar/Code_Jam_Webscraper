def gcd(a,b):
    while b: a,b = b, a%b
    return a

def calculate_t(events):    
    subtractions = []
    
    for idx in xrange(len(events)):
        for idx2 in xrange(idx+1, len(events)):
            subtractions.append(events[idx] - events[idx2])
    
    return reduce(gcd, subtractions, 0)        

def calculate(events):
    t = calculate_t(events)
    
    if (events[0] % t) == 0:
        return 0
    
    return (t - (events[0] % t)) % t

#print calculate(list(reversed(sorted([800000000000000000001, 900000000000000000001]))))

for case_number in xrange(int(raw_input())):
    events = map(int, raw_input().split())
    
    number_of_events, events = events[0], events[1:]
    
    result = calculate(list(reversed(sorted(events))))
    print 'Case #%d: %s' % (case_number+1, result)