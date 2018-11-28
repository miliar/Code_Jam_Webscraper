#!/usr/bin/env python

t = int(raw_input().strip())
n=[0]*t
n_list=[]
ans_num=0
wcnt=0
for i in xrange(t):
    n[i]=int(raw_input().strip())

for i in xrange(t):
    stop=0
    if n[i]<10:
        ans_num=n[i]
    while(n[i]>9):
        n_list=[int(x) for x in str(n[i])]
        for j in xrange(len(n_list)-1):
            diff=n_list[len(n_list)-j-1] - n_list[len(n_list)-(j+1)-1]
#            print 'diff: '+str(diff)
            if diff < 0:
                n[i]-=1
#                print 'number: '+str(n[i])
                break
            else:
                pass
#                stop=1
        ans_num=n[i]
        wcnt+=1
        if diff>=0:
            break
    print "Case #{}: {}".format(i+1, ans_num)
