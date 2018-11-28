import math
from collections import  Counter

def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    return [reader(f, *args, **kwargs) for i in range(R)]

def solve(solver, fn, out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i+1, res)

################################################################################

def read_case(f):
    no_lines = read_int(f)
    strings = read_arr(f, no_lines, reader=read_word)
    return strings

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def solve_small(case):
    print case
    # remove repeats
    sample = case[0]
    noR = noRepeat(sample)
    print noR
    
    eleList = [x[0] for x in noR]
    print "eleList=%s"%eleList
#     minLen = len(sample)
#     maxLen = len(sample)
    #base = "".join(noRepeat(sample))
    noRxList = []
    for i in range(0,len(case)):
        #maxLen = max(maxLen,len(case[i]))
        noRx = noRepeat(case[i])
        eleListx = [x[0] for x in noRx]
        noRxList.append(noRx)
        if eleList!=eleListx:
            print "Fegla Won"
            return "Fegla Won"
        
    print "noRxList=%s"%noRxList
      
    grandSum = 0    
    for i in range(len(eleList)):
        sum = 0
        for l in noRxList:
            sum += l[i][1]
        avg = sum/len(case)
        print ("i=%s, sum=%s, avg=%d"%(eleList[i],sum,avg))
        sum0 = 0
        sum1 = 0
        for l in noRxList:
            sum0 += abs(l[i][1]-avg)
            sum1 += abs(l[i][1]-(avg+1))
        print ("sum0=%d, sum1=%d"%(sum0,sum1))
        minSum = min(sum0,sum1)
        grandSum += minSum
    print "grandSum=%s"%grandSum
    return grandSum
        
        
    
#     print "minLen=%d"%minLen
#     print "maxLen=%d"%maxLen
    
    #minSum = maxLen * len(case)    
    #for ll in range (minLen,maxLen+1):  
#     sum = 0  
#     for i in range(len(case)):
#         #print "ll=%d, case[%d]=%d"%(ll,i,len(case[i]))
#         
#         sum += abs(len(sample)-len(case[i]))
#     #minSum = min(minSum,sum)
#     print sum
    #print "----------"
    
    #for c in case
    
def noRepeat(s):
    res = []
    lastChar=s[0]
    cnt = 1
    
    for i in range(1,len(s)):
        if s[i]!=lastChar:
            res.append((lastChar,cnt))
            lastChar=s[i]
            cnt = 1
        else:
            cnt +=1
    res.append((lastChar,cnt))
    return res
    

def solve_large(case):
    return solve_small(case)

DEBUG = 'i'

solve(solve_small,"a")
