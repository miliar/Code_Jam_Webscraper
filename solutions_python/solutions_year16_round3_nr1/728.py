import string

def solve(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        data = []
        for i in xrange(1, cases + 1):
            num_parties = int(f.readline().strip())
            parties = f.readline().strip().split()
            print 'Case #{}: {}'.format(i, evacuation_plan(parties))

def evacuation_step(parties, sum_senators):
    # Take the two most represented parties (it may be the same)
    parties.sort(key=lambda x: x[1], reverse=True)
    selected = parties[0]
    selected[1] -= 1    
    parties.sort(key=lambda x: x[1], reverse=True)
    selected2 = parties[0]

    # Test removing both
    selected2[1] -= 1
    sum_senators -= 2

    # See if the new senate have mayority
    parties.sort(key=lambda x: x[1], reverse=True)
    if parties[0][1] and (parties[0][1] > (sum_senators / 2)):
        # Revert the second substraction
        selected2[1] += 1
        sum_senators += 1
        return [selected[0]], sum_senators, parties
    return [selected[0], selected2[0]], sum_senators, parties
    
def evacuation_plan(parties_senators):
    evacuation = []
    sum_senators = 0
    letters = iter(string.ascii_uppercase)
    parties = []
    for senators in parties_senators:
        senators = int(senators)
        parties.append([(letters).next(), senators])
        sum_senators += senators
    while sum_senators > 0:
        selected, sum_senators, parties = evacuation_step(parties, sum_senators)
        evacuation.append(''.join(selected))
        
    return ' '.join(evacuation)
    
if __name__ == '__main__':
    solve('A-large.in')
