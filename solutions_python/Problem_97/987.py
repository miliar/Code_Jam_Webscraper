# Sample
sample_inp = '''4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21'''
sample_outp = '''Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3'''

# open input file
inp_name = raw_input("What's the input file name?\n")
inp = open(inp_name)

# initialize output file
outp = open('output.out','w')

# get N
T_str = inp.readline().replace('\n','')
T = int(T_str)

# helping procedures
    
# line by line
for i in xrange(1,T+1):
    line_lst = map(int, inp.readline().replace('\n','').split(' '))
    A = line_lst[0]
    B = line_lst[1]
    pairs = set()
    # counter = 0
    
    # loop over possible ns
    for n in xrange(A,B+1):
        ns = str(n)
        for shift in xrange(1,len(ns)):
            ms = ns[shift:] + ns[:shift]
            m = int(ms)
            if ms[0] != '0' and ms != ns and A<=m<=B:
                pairs.add(frozenset([n,m]))
                # counter += 1
                #print '(n,m) = (' + ns + ',' + ms + ')' 

    count = len(pairs)  # counter/2     
    result = 'Case #' + str(i) + ': ' + str(count)
    print result
    outp.write(result)
    outp.write('\n')

# close input/output files    
inp.close()
outp.close()
