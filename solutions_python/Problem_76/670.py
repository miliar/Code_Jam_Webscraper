'''
Created on 06/05/2011

@author: Shimi
'''

import sys
from test.test_iterlen import len

OUTPUT_FILEPATH = 'output_file_candy_split'

def compute_group_xor(numbers_ls):
    outcome = 0
    for num in numbers_ls:
        outcome = outcome ^ num
        
    return outcome

def k_subsets_i(n, k):
    '''
    Yield each subset of size k from the set of intergers 0 .. n - 1
    n -- an integer > 0
    k -- an integer > 0
    '''
    # Validate args
    if n < 0:
        raise ValueError('n must be > 0, got n=%d' % n)
    if k < 0:
        raise ValueError('k must be > 0, got k=%d' % k)
    # check base cases
    if k == 0 or n < k:
        yield set()
    elif n == k:
        yield set(range(n))

    else:
        # Use recursive formula based on binomial coeffecients:
        # choose(n, k) = choose(n - 1, k - 1) + choose(n - 1, k)
        for s in k_subsets_i(n - 1, k - 1):
            s.add(n - 1)
            yield s
        for s in k_subsets_i(n - 1, k):
            yield s

def k_subsets(s, k):
    '''
    Yield all subsets of size k from set (or list) s
    s -- a set or list (any iterable will suffice)
    k -- an integer > 0
    '''
    s = list(s)
    n = len(s)
    for k_set in k_subsets_i(n, k):
        yield set([s[i] for i in k_set])


def compute_max_pile(numbers_ls):
    # from str to int
    numbers_ls = map(int, numbers_ls)
    
    # compute the "global xor" = xor of all elements
    global_xor = compute_group_xor(numbers_ls)
    
    # real sum of all elements
    global_sum = sum(numbers_ls)
    
    # all condition fitting groups
    relevant_groups = []
    
    # for each size < length(numbers_ls) check if any of that size piles 
    # fit our condition
    for k in range(1, len(numbers_ls)/2 + 1):
        for subset in k_subsets(numbers_ls, k):
            group_xor = compute_group_xor(subset)
            if  group_xor ^ global_xor == group_xor:
                relevant_groups.append(subset)
                 
    # find max of appropriate groups, if any group exists
    if len(relevant_groups) == 0:
        return None
    
    max_group = 0;
    for group in relevant_groups:
        group_sum = sum(group)
        group_sum = max([group_sum, global_sum - group_sum])
        if group_sum > max_group:
            max_group = group_sum
            
    return max_group

        
def main():
    filepath = sys.argv[1]
    input_file = open(filepath, "rb")
    output_file = open(OUTPUT_FILEPATH, "wb")
    lines = input_file.readlines()[1:]
    input_file.close()
    
    relevant_lines = []
    for i, line in enumerate(lines):
        if i % 2 == 1:
            relevant_lines.append(line)
    lines = relevant_lines
    
    for i, line in enumerate(lines):
        return_val = compute_max_pile(line.split())
        if return_val is None:
            output_file.write("Case #%d: NO\n" % (i + 1, ))
        else:
            output_file.write("Case #%d: %d\n" % (i + 1, return_val));
    
    output_file.close()
    return
        
if __name__ == "__main__":
    main()