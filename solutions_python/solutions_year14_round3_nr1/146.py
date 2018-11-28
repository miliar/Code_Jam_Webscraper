import copy
import math
import bisect

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
    fz, fm = map(int, in_f.readline().rstrip('\n').split("/"))
    print fz, fm
    # get the solution 
    is_imp = False
    result = -1
    is_pow2, ll = is_pow_2(fm)
    if not is_pow2 and fz%ll != 0:
        is_imp = True
    else:
        if ll > 0:
            fz, fm = fz/ll, fm/ll
        fz, fm = divide2(fz, fm)
        result = bisect.bisect_left(twos, fm*1.0/fz*1.0)
        if result > 40: # pow(2,40)
            is_imp = True

    # write the solution  
    if is_imp:
        out_f.write("Case #{}: {}\n".format(case_index, "impossible"))
        print 'impossible'
    else:
        out_f.write("Case #{}: {}\n".format(case_index, result))
        print result
    

def is_pow_2(x):
    """return the factor, used to check if the fenmu has it"""
    if x == 2:
        return (True, 0)
    if x % 2 !=0:
        return (False, x)
    return is_pow_2(x/2)

# todo: test
def is_impossible(fz, fm):
    if fz > fm:
        return True
    is_pow2, ll = is_pow_2(fm)
    if not is_pow2 and fz%ll != 0:
        return True
    fz, fm = fz/ll, fm/ll
    if fm > 1099511627776: # pow(2,40)
        return True
    return False

def divide2(fz, fm):
    while fz % 2 == 0:
        fz = fz/2
        fm = fm/2
    return fz, fm

#t = ""
#for x in xrange(1, 41):
#    t += ","+str(pow(2,x))
#print t

twos = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944,549755813888,1099511627776]
#    result = bisect.bisect_left(tt, left)
#    rr = bisect.bisect_right(fair_list, right)

#for x, y in ((1,4))
run()
