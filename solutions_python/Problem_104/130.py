'''
Created on 05/05/2012

@author: Rachum
'''

from itertools import combinations

def compute_result(group):
    sums = {}
    for subset_size in range(1, len(group) - 1):
        for subset in combinations(group, subset_size):
            subset_sum = sum(subset)
            if subset_sum > sum(group) / 2.0:
                continue
            if subset_sum in sums:
                return (subset, sums[subset_sum])
            sums[subset_sum] = subset
    return None


with open('input.in', 'rt') as inputfile, open('output.txt', 'wt') as outputfile:
    num_of_testcases = int(inputfile.readline())
    for i, line in enumerate(inputfile.readlines()):
        group = [int(item) for item in line.split()[1:]]
        result = compute_result(group)
        if result is not None:
            print("Case #%d:\n%s\n%s" % (i+1, ' '.join(str(item) for item in result[0]), ' '.join(str(item) for item in result[1])))
            print("Case #%d:\n%s\n%s" % (i+1, ' '.join(str(item) for item in result[0]), ' '.join(str(item) for item in result[1])), file=outputfile)
        else:
            print("Case #%d:\nImpossible" % (i+1, ))
            print("Case #%d:\nImpossible" % (i+1, ), file=outputfile)
            
            
            
            