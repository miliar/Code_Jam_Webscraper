def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(xrange(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in xrange(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)        
        
def patrick_sum(candies):
    result = 0
    for candy in candies:
        result = result ^ candy
    return result

def process(s):
    all_candies = map(int, s.split(' '))
    number_of_candies = len(all_candies)

    best_possible_score = sum(all_candies)
    
    solutions_to_analyse = {}

    for i in xrange(1, number_of_candies):
        patrick_candy_perms = combinations(all_candies, i)
        for patrick_candy_perm in patrick_candy_perms:
            sean_good_sum = best_possible_score - sum(patrick_candy_perm)
        
            try:
                solutions_to_analyse[sean_good_sum].append( patrick_candy_perm )
            except:
                solutions_to_analyse[sean_good_sum] = [patrick_candy_perm]
            
    sorted_sums = sorted(solutions_to_analyse.keys(), reverse=True)
    
    for sean_good_sum in sorted_sums:
        for patrick_candy_perm in solutions_to_analyse[sean_good_sum]:
            sean_candies = all_candies[:]
            for i in patrick_candy_perm: sean_candies.remove(i)
        
            patrick_perm_sum = patrick_sum(patrick_candy_perm)
            sean_sum =         patrick_sum(sean_candies)
            
            if patrick_perm_sum == sean_sum:
                return sean_good_sum
    else:
        return None
    

number_of_cases = int(raw_input())
for case_number in xrange(1, number_of_cases+1):
    _ = raw_input()
    s = raw_input()
    #s = '5 5'
    
    result = process(s)
    if result is None:
        result = 'NO'
    print "Case #%d: %s" % (case_number, result)
    case_number += 1
    
#print process('5 5')