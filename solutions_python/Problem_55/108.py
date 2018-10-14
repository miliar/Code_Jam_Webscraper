SET_NAME = 'C-large'

def solve_case(infile):
    R, k, N = map(int, infile.readline().split())
    groups = map(int, infile.readline().split())
    print R, k, groups
    preamble, cycle = get_rider_sets(groups, k)
    print preamble, cycle
    if R < len(preamble):
        return sum(preamble[0: R])
    else:
        return sum(preamble) + sum(cycle) * ((R - len(preamble)) // len(cycle)) + \
                               sum(cycle[:(R - len(preamble)) % len(cycle)])

def get_rider_sets(groups, capacity):
    next_group = 0;
    rider_sets = []
    start_groups = [] 
    while True:
        if next_group in start_groups:
            index = start_groups.index(next_group)
            return rider_sets[:index], \
                   rider_sets[index:]
        else:
            start_group = next_group
            revenue_for_set = 0
            while (revenue_for_set + groups[next_group] <= capacity) and \
                  (revenue_for_set == 0 or next_group != start_group):
                revenue_for_set += groups[next_group]
                next_group = (next_group + 1) % len(groups)
            rider_sets.append(revenue_for_set)  
            start_groups.append(start_group)

def main():
    """
    Standard main method for all google code jam problems
    """
    infile = open('%s.in'%(SET_NAME))
    outfile = open('%s.out'%(SET_NAME), 'w')
    num_cases = int(infile.readline())
    for i in xrange(num_cases):
        print 'Solving case #%d...'%(i+1)
        output = 'Case #%d: %s\n'%(i+1, solve_case(infile))
        print output
        outfile.write(output)
    outfile.close()
               
if __name__ == '__main__':
    main()