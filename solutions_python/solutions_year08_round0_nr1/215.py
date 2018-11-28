#!/usr/bin/python

def solve(se_list, query_list):
    available_set = set(se_list)
    switch = 0
    for i in range(len(query_list)):
        query = query_list[i]
        se_set = set([se for se in se_list if se != query])
        intersection_set = available_set.intersection(se_set)
        if not len(intersection_set):
            switch = switch + 1
            available_set = se_set
        else:
            available_set = intersection_set
#        print query, se_set, available_set, switch

    return switch 
            

def parse_test(data):
    line = 0
    num_se = int(data[line])
    line = line + 1
    se_list = []
    query_list = []
    for i in range(num_se):
        se_name = data[line]
        se_list.append(se_name)
        line = line + 1
    num_query = int(data[line])
    line = line + 1
    for i in range(num_query):
        query = data[line]
        query_list.append(query)
        line = line + 1
    return (line, [se_list, query_list]) 

def main():
    import sys
    filename = sys.argv[1]
    input = open(filename)
    data = [line.strip() for line in input.readlines()]
    num_testcases = int(data[0])
    line = 1
    for i in range(1, num_testcases+1):
        (lines, test) = parse_test(data[line:])
#        print test
        answer = apply(solve, test)
        print "Case #%d: %d" % (i, answer)
        line = line + lines
    input.close()

if __name__ == "__main__":
    main()


