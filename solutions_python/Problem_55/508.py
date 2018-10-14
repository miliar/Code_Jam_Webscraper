#!/usr/bin/python

def calc_sum(st_index, k, g):
    #print "Calculating"
    #print st_index, k, g,
    sum = 0
    len_g = len(g)
    num_g = 0
    while sum + g[st_index] <= k and num_g < len_g:
        sum = sum + g[st_index]
        st_index = (st_index + 1) % len_g
        num_g = num_g + 1
    #print sum, num_g
    return (sum, num_g)      

def solve(r, k, g):
    sum = 0
    st_index = 0
    stored = {} 
    len_g = len(g)
    for i in xrange(r):
        x = stored.get(st_index, None)
        if not x:
            stored[st_index] = calc_sum(st_index, k, g)
            x = stored[st_index]
        #print x
        sum = sum + x[0]
        st_index = (st_index + x[1]) % len_g
    return sum     

def main():
    """docstring for main"""
    input = open("problem")
    ilines = [l.strip() for l in input.readlines()]
    num_tests = int(ilines[0], 0)
    line_num = 1
    for test in xrange(num_tests):
        line = ilines[line_num]
        line_num = line_num + 1
        (r, k, n) = [int(x, 0) for x in line.split()]
        line = ilines[line_num]
        line_num = line_num + 1
        g = [int(x, 0) for x in line.split()]
        print "Case #%d: %d" % (test + 1, solve(r, k, g))

if __name__ == '__main__':
    main()        
