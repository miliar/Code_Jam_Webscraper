
# as part of the solution the function pre_process() must be run in advance!!
# before downloading the input and running main_run()


directory = 'C:/users/hai/my projects/google code jam/2013/qualification/C/'


import itertools
import time


def pre_process():
    fairs = set([1,2,3])
    for length in range(1,27):
        print(time.ctime(), length)
        digits = [[0,1] for i in range(length)]
        for comb in itertools.product(*digits):
            if sum(comb) > 5:
                continue
            comb1 = list(comb) + list(reversed(comb))
            comb2 = list(comb) + list(reversed(comb))[1:]

            fairs.add(int(''.join([str(x) for x in comb1])))
            fairs.add(int(''.join([str(x) for x in comb2])))

            for i in range(len(comb1)):
                c1 = list(comb1)
                c1[i] = 2
                c1[-i-1] = 2
                fairs.add(int(''.join([str(x) for x in c1])))
            
            for i in range(len(comb2)):
                c2 = list(comb2)
                c2[i] = 2
                c2[-i-1] = 2
                fairs.add(int(''.join([str(x) for x in c2])))

    fairs.remove(0)
    fairs = list(sorted(fairs))
    
    print (' len of fairs = ', len(fairs))
    f = open(directory + 'pre_process_fair_and_squares.txt', 'w')
    for n in fairs:
        if is_palindrome(n) and is_palindrome(n**2):
            f.write(str(n**2)+'\n')

    f.close()
    return


def is_palindrome (n):
    l = list(str(n))
    return list(reversed(l)) == l

  
def solve (f_in, f_out):
    print(time.ctime())
    global fair_and_squares
    f = open(directory + 'pre_process_fair_and_squares.txt')
    fair_and_squares = [int(x) for x in f.readlines()]
    f.close()
    print(time.ctime())
    print(len(fair_and_squares))
    
    T = int(f_in.readline())
    for testcase in range(1,T+1):
        A,B = [int(x) for x in f_in.readline().split()]
        count = len([x for x in fair_and_squares if (x>=A and x<=B)])
        f_out.write('Case #' + str(testcase) + ': ' + str(count) + '\n')



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
    solve(f_in,f_out)
    f_in.close()
    f_out.close()

    print ()
    print ('End : ', time.ctime())


#pre_process()
main_run()


