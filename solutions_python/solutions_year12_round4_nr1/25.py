directory = 'C:/users/hai/my projects/google code jam/2012/2/A/'



def solve_one_testcase (f_in, f_out, testcase):
    N  = int(f_in.readline())
    lst = []
    for i in range(N):
        d, l = [int(x) for x in f_in.readline().split()]
        lst.append((i,d,l))
        #print ('input:   ',i,d,l)
    D = int(f_in.readline())
    lst.append((len(lst),D,0))
    #print ('input : ', D)
    

    visited = [False]*len(lst)
    visited[0] = True

    visited_details = {}

    S = [(0,lst[0][1],lst[0][1])]
    while S:
        #print ('visiting : ', S[0])
        w, place, length = S[0]
        S = S[1:]
        neighbors = find_next_vines (lst, w, place, length)
        for u in neighbors:
            if not visited[u[0]] or visited_details[u[0]] < u[2]:
                visited[u[0]] = True
                visited_details[u[0]] = u[2]
                S = S + [u]

    if visited[-1]:
        f_out.write ('Case #' + str(testcase) + ': YES\n')
        #print ('out : yes')
    else:
        f_out.write ('Case #' + str(testcase) + ': NO\n')
        #print ('out : no')
        


def find_next_vines (lst, vine, place, length):
    l = []
    for i in range (vine+1, len(lst)):
        if lst[i][1] <= place + length:
            l.append((i,lst[i][1],min(lst[i][2],lst[i][1]-place)))
        else:
            break
    return l




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


