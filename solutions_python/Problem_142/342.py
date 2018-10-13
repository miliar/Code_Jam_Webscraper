
PROBLEM_ID = "A" # A B or C
PROBLEM_SIZE = "small"

def run():
    """I/O handler"""
    file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
    in_f = open('{}.txt'.format(file_name), 'r')
    out_f = open('{}.out'.format(file_name), 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)

def solve_case(in_f, out_f, case_index):
    """problem solver"""
    print "case #{}:".format(case_index)
    N = int(in_f.readline().rstrip('\n'))
    sl = [] # string list
    for x in xrange(N):
        sl.append(in_f.readline().rstrip('\n'))
    
    basel = [] # base structure list
    dl = [] # duplications sum
    for st in sl:
        # find the base structure of string: aabbccc->abc
        # also record the appearance of each duplicates.
        leng = len(st)
        index = 1
        cur_l = st[0]
        cur_sum = 1 
        dl_c = []
        basel_c = []
        while index < leng:
            if st[index] == cur_l:
                cur_sum += 1
            else:# change, need to record
                dl_c.append(cur_sum)
                cur_sum = 1
                basel_c.append(cur_l)
                cur_l = st[index]
            index += 1
        #
        basel_c.append(cur_l)
        dl_c.append(cur_sum)
        basel.append("".join(basel_c))
        dl.append(dl_c)

#    print sl
#    print basel
#    print dl
    
    if len(set(basel)) != 1:
        print "Fegla Won"
        out_f.write("Case #{}: {}\n".format(case_index, "Fegla Won"))
        return
    
    step_sum = 0
    leng = len(basel[0])
    for ii in xrange(leng):
        x = [row[ii] for row in dl]
        median = sorted(x)[len(x)//2]
#        print median
        for xx in x:
            step_sum += abs(xx-median)
#        print step_sum

    out_f.write("Case #{}: {}\n".format(case_index, step_sum))
    

run()
