""" imports """
import glob, pprint, pickle, os, time, sys
from copy import copy
from numpy import array, sin, cos
""" global variables """
""" classes """
def optimize(Emax, Estart, Eend, R, v, N):
    #step 1: find rightmost maximum
    if N==0:
        return []
    index = -1
    maximum = -1
    for i in xrange(N):
        if v[i]>=maximum:
            maximum=v[i]
            index = i
    #rightmost maximum is pivot
    #find out how much we can spend at pivot
    haveatmost = index*R+Estart
    if haveatmost > Emax:
        haveatmost = Emax
    needatleast = Eend - (N-index)*R
    if needatleast<0:
        needatleast = 0
    spending = haveatmost - needatleast
    
    answer = [0]*N
    answer[:index-1] = optimize(Emax, Estart, haveatmost, R, v[:index],index)
    answer[index] = spending
    answer[index+1:] = optimize(Emax, needatleast+R, Eend, R, v[index+1:],N-index-1)
    return answer
""" functions """
def solve(E,R,v,N):
    spending = optimize(E,E,0,R,v,N)
    s = 0
    for i in xrange(len(v)):
        s += v[i]*spending[i]
    return s
""" parse input """
output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):
        ### parse input ###
        E, R, N = read_ints()
        v = read_ints()
        ### calculate answer ###
        answer = solve(E,R,v,N)
        ### output ###
        #print "Calculating case #{}...".format(questionindex+1)
        answer_str = "Case #{}: {}".format(questionindex+1, answer)
        output += answer_str + '\n'
        print answer_str
ofile = open('output', 'w').write(output)
TOC = time.time()
print "done in {} s".format(TOC-TIC)
