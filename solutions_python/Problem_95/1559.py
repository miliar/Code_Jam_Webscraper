'''
Created on 2012-4-14

@author: Matrix
'''
import sys
dict={}
dict['a']='y';dict['b']='h';dict['c']='e';dict['d']='s'
dict['e']='o';dict['f']='c';dict['g']='v';dict['h']='x'
dict['i']='d';dict['j']='u';dict['k']='i';dict['l']='g'
dict['m']='l';dict['n']='b';dict['o']='k';dict['p']='r'
dict['q']='z';dict['r']='t';dict['s']='n';dict['t']='w'
dict['u']='j';dict['v']='p';dict['w']='f';dict['x']='m'
dict['y']='a';dict['z']='q'
#sys.stdin=open("A-small-attempt0.in","r")
#sys.stdout=open("out.txt","w")
n=int(raw_input())
for t in xrange(n):
    data=raw_input().split()
    ans=[]
    for d in data:
        str=""
        for j in d:str+=dict[j]
        ans.append(str)
    print "Case #%d: %s" % (t+1," ".join(ans))