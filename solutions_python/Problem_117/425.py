from collections import Counter
import IPython


def check(a1, a2):
    return a1 == a2

def check_row(a1, a2, i):
    return a1[i] == a2[i]
    
def check_column(a1, a2, j):
    for i in range(len(a1)):
        if a1[i][j] != a2[i][j]: return False
    return True

def max_in_row(a, i):
    return max(a[i]) 

def max_in_column(a, j):
    return max(a[i][j] for i in range(len(a)))

def cut_row(a, i, n):
    is_cut = False
    for j in range(len(a[0])):
        if a[i][j] > n:
            is_cut = True
            a[i][j] = n
    return is_cut

def cut_column(a, j, n):
    is_cut = False
    for i in range(len(a)):
        if a[i][j] > n: 
            is_cut = True
            a[i][j] = n
    return is_cut


# TODO do not check if done
        
def solve(N, M, target):

    lawn = [[100 for j in range(M)] for i in range(N)]

    i_to_check = range(N)
    j_to_check = range(M)

    is_continue = True
    while is_continue:
        is_continue = False

        if check(lawn, target): return 'YES'

        for i in i_to_check:
            if not check_row(lawn, target, i):
                n = max_in_row(target, i)
                if cut_row(lawn, i, n):
                    is_continue = True
            else:
                i_to_check.remove(i)

        for j in j_to_check:
            if not check_column(lawn, target, j):
                n = max_in_column(target, j)
                print n

                ret = cut_column(lawn, j, n)
                print ret
                if ret:
                    is_continue = True
            else:
                j_to_check.remove(j)
             
    #for row in lawn:
    #    print row
    return 'NO'


if __name__ == '__main__':

    import sys
    
    input_file = sys.argv[1]
    output_file = input_file[:].replace('.in', '.out')


    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')

    T, = [int(x) for x in f_in.readline().split()]

    for case in range(1, T+1):
        print 
        print '====================='
        print '    ' + str(case)
        print '====================='

        target = []
        N, M = [int(x) for x in f_in.readline().split()]
        for i in range(N):
            target.append([int(x) for x in f_in.readline().split()])
        print target



        # Solve
        ans = solve(N, M, target)
        print ans

        ## Output
        f_out.write('Case #%d: %s\n' % (case, ans))

        

