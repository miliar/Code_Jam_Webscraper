import fileinput
import logging
import sys
import heapq
import math
import random

logging.basicConfig(stream=sys.stderr,level=logging.ERROR)


nTest = 0
line_no = 0
instances = []
first_instance_line = True

D = 0


for line in fileinput.input():
    if line_no == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    elif first_instance_line:
        first_instance_line = False
        a = line.split()
        L = int(a[0])
        X = int(a[1])
    else:
        first_instance_line = True
        P = line.rstrip()
        instances.append((L,X,P))

    line_no+=1


table = {('1','1'): '1', 
         ('1','i'): 'i', 
         ('1','j'): 'j', 
         ('1','k'): 'k',
         ('i','1'): 'i', 
         ('i','i'): '-1', 
         ('i','j'): 'k', 
         ('i','k'): '-j',
         ('j','1'): 'j', 
         ('j','i'): '-k', 
         ('j','j'): '-1', 
         ('j','k'): 'i',
         ('k','1'): 'k', 
         ('k','i'): 'j', 
         ('k','j'): '-i', 
         ('k','k'): '-1'}

def neg(a):         
    return a[0] == '-'

def positive(a):
    if neg(a):
        return a[1]
    else:
        return a
        
def negate(a):
    if neg(a):
        return positive(a)
    else:
        return '-'+a


def mult(a,b):
    if (a,b) in table:
        return table[(a,b)]
    value = '1'

    if neg(a) and neg(b):
         value =  table[(negate(a),negate(b))]
    elif neg(a) or neg(b):
         value =  negate(table[(positive(a),positive(b))])
    else:
         value =  table[(positive(a),positive(b))]
    table[(a,b)] = value
    return value

def my_reduce(exp):
    so_far = '1'
    for i in xrange(len(exp)):
        so_far = mult(so_far,exp[i])
    return so_far

def partial_reduce(so_far,exp):

    # for i in xrange(len(exp)):
    #     so_far = mult(so_far,exp[i])

    so_far = reduce(mult,exp,so_far)

    return so_far

#    so_far = fancy_reduce(so_far,exp,last_y,y,result,step)




def fancy_reduce(so_far,exp,start,finish,result,step):
    if finish-start < 2*step:
        return partial_reduce(so_far,exp[start:finish])
    else:
        next_step_index = start/step+1
        next_step = (next_step_index)*step
        prev_step_index = finish/step
        prev_step = prev_step_index*step
        logging.debug("start %d, finish %d, len %d" % (start,finish, len(exp)))
        logging.debug("length of helper %d" % len(result))
        logging.debug("index1 %d, index2 %d" % (next_step_index, prev_step_index))
        logging.debug("start_to %d, finish_from %d" % (next_step, prev_step))
        # for i in xrange(start, next_step):
        #     so_far = mult(so_far,exp[i])
        so_far = reduce(mult, exp[start:next_step],  so_far)
        # for i in xrange(next_step_index,prev_step_index):
        #     so_far = mult(so_far,result[i])
        so_far = reduce(mult, result[next_step_index:prev_step_index], so_far)
        # for i in xrange(prev_step,finish):
        #     so_far = mult(so_far, exp[i])
        so_far = reduce(mult, exp[prev_step:finish], so_far)
        return so_far
            

def match_pattern(exp,pattern,backward=False):
    so_far = '1'
    result = []
    logging.debug("Backward")
    logging.debug(backward)
    if not backward:
        for i in xrange(len(exp)):
            logging.debug("%d %s %s" % (i, exp[i:i+2], so_far))
            so_far = mult(so_far,exp[i])
            if so_far == pattern:
                result.append(i)
    else:
        for i in xrange(len(exp)):
            j = len(exp)-1-i
            logging.debug("%d %s %s" % (j, exp[j:j+2], so_far))
            so_far = mult(exp[j],so_far)
            if so_far == pattern:
                result.append(j)

    logging.debug("match_pattern result: %s" % pattern)
    logging.debug(result)
    return result

def i_points(exp):
    return match_pattern(exp,'i')

def minus_i_points(exp):
    return match_pattern(exp,'-i')

def k_points(exp,backward=True):
    return match_pattern(exp,'k',backward)

def minus_k_points(exp,backward=True):
    return match_pattern(exp,'-k',backward)

def pre_process(exp,step):
    result = []
    for i in xrange(0,len(exp),step):
        result.append(my_reduce(exp[i:i+step]))

    return result
    
def check_result(exp,end_i,start_k):
    val1 = my_reduce(exp[0:end_i+1])
    val2 = my_reduce(exp[end_i+1:start_k])
    val3 = my_reduce(exp[start_k:])
    logging.debug("Produced %s %s %s \n" % (val1, val2, val3))

    assert((val1 == 'i' or val1 == '-i'))
    assert((val2 == 'j' or val2 == '-j'))
    assert((val3 == 'k' or val3 == '-k'))


def test_fancy_reduce(exp, result,step):
    trials = 100
    for x in xrange(trials):
        i = random.randint(0,len(exp)-1)
        j = random.randint(i,len(exp)-1)
        so_far = '1'
        val1 = fancy_reduce(so_far,exp,i,j,result,step)
        so_far = '1'
        val2 = partial_reduce(so_far,exp[i:j])
        logging.debug("Hello %s %s\n" % (val1, val2))
        assert(val1 == val2)
    
def instance(inst):
    global fancy_table
    fancy_table = {}

    L = inst[0]
    X = inst[1]
    P = inst[2]
    exp = P
    for i in xrange(X-1):
        exp += P
    logging.debug(exp[0:10])
    ipoints = i_points(exp)
    minus_ipoints = minus_i_points(exp)
    kpoints = k_points(exp)
    minus_kpoints = minus_k_points(exp)

    kpoints.reverse()
    minus_kpoints.reverse()

    logging.debug("ipoints")
    logging.debug(ipoints)

    step = max(30,int(math.sqrt(len(exp))))
    result = pre_process(exp,step)
    logging.debug("result")
    logging.debug(result)
    test_fancy_reduce(exp,result,step)

    logging.error("first set")
    for x in ipoints:
        so_far = '1'
        last_y = -1
        for y in kpoints:
            if y > x:
                if (last_y > 0):
                    so_far = fancy_reduce(so_far,exp,last_y,y,result,step)
                else:
                    so_far = fancy_reduce(so_far,exp,x+1,y,result,step)
                last_y = y
            if so_far == 'j':
                check_result(exp,x,y)
                logging.debug("Worked with %d and %d\n" % (x,y))
                return True

    logging.error("seconc set")

    for x in minus_ipoints:
        so_far = '1'
        last_y = -1
        for y in minus_kpoints:
            if y > x:
                if (last_y > 0):
                    so_far = fancy_reduce(so_far,exp,last_y,y,result,step)
                else:
                    so_far = fancy_reduce(so_far,exp,x+1,y,result,step)
                last_y = y
            if so_far == 'j':
                check_result(exp,x,y)
                logging.debug("Worked with %d and %d\n" % (x,y))
                return True

    logging.error("third set")
    for x in minus_ipoints:
        so_far = '1'
        last_y = -1
        for y in kpoints:
            if y > x:
                if (last_y > 0):
                    so_far = fancy_reduce(so_far,exp,last_y,y,result,step)
                else:
                    so_far = fancy_reduce(so_far,exp,x+1,y,result,step)
                last_y = y
            if so_far == '-j':
                check_result(exp,x,y)
                logging.debug("Worked with %d and %d\n" % (x,y))
                return True

    logging.error("fourth set")
    for x in ipoints:
        so_far = '1'
        last_y = -1
        for y in minus_kpoints:
            if y > x:
                if (last_y > 0):
                    so_far = fancy_reduce(so_far,exp,last_y,y,result,step)
                else:
                    so_far = fancy_reduce(so_far,exp,x+1,y,result,step)
                last_y = y
            if so_far == '-j':
                check_result(exp,x,y)
                logging.debug("Worked with %d and %d\n" % (x,y))
                return True
        
    return False

out_line_no = 1
for x in instances:
    logging.error("Instance %d" % out_line_no)
    if (instance(x)):
        print "Case #%d: YES" % (out_line_no)
    else:
        print "Case #%d: NO" % (out_line_no)

    out_line_no+=1



