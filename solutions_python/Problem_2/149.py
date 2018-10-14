import sys, datetime, pdb

def arr_compare(x, y):
    if x['arr'] < y['arr']:
        return -1
    elif x['arr'] == y['arr']:
        return 0
    else:
        return 1
    
def dep_compare(x, y):
    if x['dep'] < y['dep']:
        return -1
    elif x['dep'] == y['dep']:
        return 0
    else:
        return 1

def input_case():
    case = {}
    case['turn_time'] = datetime.timedelta(minutes=int(f.readline()))
    
    num_trips = f.readline().split(None, 2)
    na = int(num_trips[0], 10)
    nb = int(num_trips[1], 10)
    
    case['atrips'] = input_trips(na)
    case['btrips'] = input_trips(nb)
    
    return case

def input_trips(n):
    trips = []
    for i in xrange(int(n)):
         trip_times = f.readline().split(None, 2)
         dh, dm = trip_times[0].split(':')
         ah, am = trip_times[1].split(':')
         trips.append({ 'dep' : datetime.datetime(2008, 7, 16, int(dh), int(dm)), 'arr' : datetime.datetime(2008, 7, 16, int(ah), int(am)) })
    return trips

def solve_case(case):
    return solve_station(case['atrips'], case['btrips'], case['turn_time']) + ' ' + solve_station(case['btrips'], case['atrips'], case['turn_time'])

def solve_station(stn, dest, tt):
    needed = 0
    present = 0
    istn = idest = 0
    
    stn.sort(dep_compare)
    dest.sort(arr_compare)
    
    # corner cases
    if len(stn) == 0 or len(dest) == 0:
        return str(len(stn))
    
    # count departures before any trains arrive
    while istn < len(stn) and stn[istn]['dep'] < dest[idest]['arr'] + tt:
        needed += 1
        istn += 1
    
    # calculate 
    while idest < len(dest) and istn < len(stn):
        if stn[istn]['dep'] >= dest[idest]['arr'] + tt:
            present += 1
            idest += 1
        else:
            present -= 1
            istn += 1
        
        if present < 0:
            present = 0
            needed += 1
    
    # count departures after all trains have arrived
    while istn < len(stn):
        present -= 1
        istn += 1
        
        if present < 0:
            present = 0
            needed += 1
    
    return str(needed)

f = open(sys.argv[-1], 'r')
numCases = int(f.readline())

for i in xrange(int(numCases)):
    case = input_case()
    print 'Case #' + str(i + 1) + ': ' + solve_case(case)