from collections import  namedtuple
from  heapq import *


templ = '/home/tocarip/Downloads/ProgrammingAssignment4Files/'


file_gr = open(templ+'qaz')

ln = file_gr.readlines()

num_cases = int(ln[0])


mul = 1
for j,l in enumerate(ln[1:]):
    if j % 2 == 0:
        mul = int(l.split()[1])
        continue
    res = False
    target = 'i'
    sign = False
    state = ''
    for i in l[0:].strip()*mul:
        if i == target and state == '':
            if target == 'i':
                target = 'j'
            elif target == 'j':
                target = 'k'
            elif target == 'k':
                target = 'x'
            state = ''
        else:
            if state == '':
                state = i
            else:
                if state == '1':
                    tmp = {'1':'1','i':'i','j':'j','k':'k'}
                    tmp2 = {'1':False,'i':False,'j':False,'k':False}
                    if tmp2[i]:
                        sign = not sign
                    state = tmp[i]
                elif state == 'i':
                    tmp = {'1':'i','i':'1','j':'k','k':'j'}
                    tmp2 = {'1':False,'i':True,'j':False,'k':True}
                    if tmp2[i]:
                        sign = not sign
                    state = tmp[i]
                elif state == 'j':
                    tmp = {'1':'j','i':'k','j':'1','k':'i'}
                    tmp2 = {'1':False,'i':True,'j':True,'k':False}
                    if tmp2[i]:
                        sign = not sign
                    state = tmp[i]
                elif state == 'k':
                    tmp = {'1':'k','i':'j','j':'i','k':'1'}
                    tmp2 = {'1':False,'i':False,'j':True,'k':True}
                    if tmp2[i]:
                        sign = not sign
                    state = tmp[i]
                if state == target and not sign:
                    if target == 'i':
                        target = 'j'
                    elif target == 'j':
                        target = 'k'
                    elif target == 'k':
                        target = 'x'
                    state = ''
    if target == 'x' and (state == '' or state == '1') and  not sign:
        print 'Case #'+ str(j/2+1) +  ': Yes'
    else:
        print 'Case #'+ str(j/2+1) +  ': No'

