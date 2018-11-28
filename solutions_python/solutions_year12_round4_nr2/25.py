directory = 'C:/users/hai/my projects/google code jam/2012/2/B/'



def solve_one_testcase (f_in, f_out, testcase):
    line = f_in.readline()
    print (line)
    N,W,L = [int(x) for x in line.split()]
    r = [int(x) for x in f_in.readline().split()]
    assert len(r) == N

    print ('TESTCASE ', testcase)
    #print ('input : ', N,W,L)
    #print ('input : ',r)
    
    ordd = order_r (r)
    curr_row = 0
    next_col = 0
    next_row = 0
    positions = {}
    
    while len(ordd) != 0:
        arms, idd = ordd[0]
        ordd = ordd[1:]
        next_row = max (next_row, curr_row + arms)
        if next_col +arms > W:
            curr_row = next_row + arms
            next_col = 0
            next_row = curr_row+arms
        if next_col == 0:
            next_col = -arms
        assert curr_row >=0
        assert curr_row <=L
        assert next_col+arms >= 0
        assert next_col+arms <=W
        positions[idd] = (next_col+arms, curr_row)
        next_col = next_col + 2*arms

    f_out.write ('Case #' + str(testcase) + ': ')
    for k in sorted(positions):
        x,y = positions[k]
        #print (k, ' : ', x,y)
        f_out.write (str(x) +' ' + str(y) + ' ')
    f_out.write('\n')

    
    


def order_r (r):
    r2 = r[:]
    o = []
    while (sum(r2)):
        arms = max(r2)
        index = r2.index(arms)
        r2[index] = 0
        o.append((arms,index))
    return o

##    skyline = [(0,W,0)]
##    positions = []
##    while sum(r) != 0:
##        place_next (W, L, skyline, positions, r)
##
##
##
##
##    f_out.write('Case #' + str(testcase) + ' :')
##    
##
##def place_next (W,L, skyline, positions, r):
##    arms = max(r)
##    index = r.find(arms)
##    r[index] = 0
##    for next_location in sorted_skyline(skyline):
##        if next_location[1] == 0:
##            next_location[1] == -arms
##            
##
##
##def is_valid_location (W,L,skyline,arms,x,y):
##    left_x = max(0,x-arms)
##    right_x = min(W,x+arms)
##    for t i in skyline:
##        if t[0]<=left_x and t[1] >=right_x
##def sorted_skyline (skyline):
##    c = []
##    for s in skyline:
##        ttt = [s[2],s[0],s[1]]
##        c.append(ttt)
##    c.sort()
##    return c
##
##    
def solve_all_testcases (f_in, f_out):
    T = int(f_in.readline())
    for testcase in range(1,T+1):
        print ('*****  Testcase ', testcase)
        solve_one_testcase(f_in, f_out, testcase)
   




def main_run():
    import os
    import time
    filenames = [x for x in os.listdir (directory)]
    filenames = [x for x in filenames if x.endswith('.in')]
    l1 = [(os.stat(directory+x).st_ctime, x) for x in filenames]
    chosen_filename =  sorted(l1)[-1][1][:-3]

    print ('Directory : ', directory)
    print ('Chosen Filename : ',chosen_filename)
    print()
    print ('Start : ', time.ctime())
    print()
    
    f_in = open(directory+chosen_filename+'.in')
    f_out = open(directory+chosen_filename+'.out', 'w')
    solve_all_testcases(f_in,f_out)
    f_in.close()
    f_out.close()

    print ()
    print ('End : ', time.ctime())


main_run()


