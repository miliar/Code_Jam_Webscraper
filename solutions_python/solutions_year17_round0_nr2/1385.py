#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def isTidy(A):
    """
    :type A: string 
    """
    length = len(A)
    for x in xrange(length-1):
        #print str(A[x]) + " " + str(A[x+1])
        if A[x] > A[x+1]: 
            return 0
    return 1;
        
def minusOne(A):
    """
    :type A: string 
    """
    length = len(A)
    #print A
    minus_done = 0
    result = ""
    temp_list = []
    for x in xrange(length-1, -1, -1):
        if minus_done == 1:
            result += A[x]
            continue
        if A[x] == '0':
            result += str(9)
            #print "A[x]: " + str(A[x])
            #print "result: " + str(result)
        else:
            result += str(int(A[x])-1)
            minus_done = 1
    result = result[::-1]
    #print "A-1: " + str(int(result))
    temp_list = list(result)
    #print temp_list
    return temp_list


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input()  # read string, 1 in this case
    length = len(s)
    target = length-1
    s_list = list(s)
    final_result = int(s)
    while isTidy(s_list) == 0:
        s_list[target] = "9"
        #print "before -1: " + ''.join(s_list[0:target])
        s_list[0:target] = minusOne(s_list[0:target])
        #print int(''.join(s_list))
        final_result = int(''.join(s_list))
        target = target -1
    print "Case #{}: {}".format(i, final_result)
    #print "Case #{}: {}".format(i, final_result)
    # check out .format's specification for more formatting options
