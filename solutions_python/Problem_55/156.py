INPUT = {
    'config' : ('int', 'linearray'),
    'people' : ('int', 'linearray')
}

INPUT_ORDER = ['config', 'people']

TEST = ('''\
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
''','''\
Case #1: 21
Case #2: 100
Case #3: 20
''')

def main(config, people):
    R, k, N = config
    
    # initialize all vars
    pointer = 0
    next_pointer = 0
    next_ride = 0
    ride = 0
    euros = 0
    # riiiide
    for r in xrange(R):
        ride = 0 # number of people on this ride
        q = 0 # number of groups picked up, cannot exceed N
        adding = True
        while adding:
            next_pointer = (pointer + 1) % N
            next_ride = ride + people[pointer % N]
            q += 1
            if next_ride > k or q > N:
                # bail
                adding = False
            else:
                ride = next_ride
                pointer = next_pointer
                
        euros += ride
        
    return euros