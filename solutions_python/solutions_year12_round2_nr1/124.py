'''
Created on 05/05/2012

@author: Rachum
'''


def uniform(results):
    num = results[0]
    for i in results:
        if i != num:
            return False
    return True


def compute_result(points):
    """points is a list of contestent's results."""
    ptsum = float(sum(points))
    results = [0]*len(points)
    total_score = 1.0
    while not uniform(points):
        min_pts = min(points)
        lowest = []
        for i in range(len(points)):
            if points[i] == min_pts:
                lowest += [i]
        next_num = min(pt for pt in points if pt > min_pts)
        
        to_sub = (((next_num - float(min_pts)) / ptsum)) * len(lowest)
        if total_score - to_sub < 0:
            for i in lowest:
                results[i] += (total_score) / len(lowest)
                points[i] = ((total_score) / len(lowest)) * ptsum
            return [float(item)*100.0 for item in results]
        else:
            for i in lowest:
                results[i] += (next_num - float(min_pts)) / ptsum
                points[i] = next_num
            total_score -= to_sub
    sum_percentage = sum(results)
    return [((float(item)+ ((1.0-sum_percentage) / len(results))))*100.0 for item in results]

with open('input.in', 'rt') as inputfile, open('output.txt', 'wt') as outputfile:
    num_of_testcases = int(inputfile.readline())
    for i, line in enumerate(inputfile.readlines()):
        points = [int(item) for item in line.split()[1:]]
        result = ' '.join(str(item) for item in compute_result(points))
        print("Case #%d: %s" % (i+1, result), file=outputfile)
