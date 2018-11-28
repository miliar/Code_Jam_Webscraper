#!/usr/bin/env python
# encoding: utf-8

from optparse import OptionParser

def cycle_cost(capacity, groups):
    count = 0
    queue = groups[:] 
    for i, group_size in enumerate(groups):
        required = count + group_size
        if capacity < required:
            break
        count = required
        queue.pop(0)
        queue.append(group_size)
    groups[:] = queue
    return count

def get_cost(cycles_num, capacity, groups):
    total_cost = 0
    for i in xrange(1, cycles_num+1):
        total_cost += cycle_cost(capacity, groups) 
    return total_cost

def main():
    """Main function code. Implementing:
        1. parsig args (-i, --in-file)
        2. iterating and transorming input data (results stored in table)
        3. printing out results in required format
    """
    parser = OptionParser(usage="usage: %prog [options] arg") 
    parser.add_option("-i", "--in-file", dest="in_filename", help="provide input data by specifing filename")
    (options, args) = parser.parse_args() 
    if options.in_filename is None:
        parser.print_usage()
        exit(0)
    results = [] 
    for cycles_num, capacity, groups in gen_next_case(options.in_filename):
        results.append(get_cost(cycles_num, capacity, groups))   
    for i, result in enumerate(results):    
        print "Case #%i: %i" % (i+1, result)  

def gen_next_case(filename):
    """Wrap the imput file format and return cycles_num, capacity, groups. 
    It uses generator to return them one by one."""
    next_line = lambda f: f.readline().rstrip()
    with open(filename, "r") as f:
        num_of_cases = int(next_line(f))
        data = next_line(f)
        while data:
            cycles_num, capacity, groups_count = data.split(' ')
            cycles_num = int(cycles_num)
            capacity = int(capacity)
            groups = [int(x) for x in next_line(f).split(' ')]
            data = next_line(f)
            yield cycles_num, capacity, groups           

if __name__ == '__main__':
    main()

