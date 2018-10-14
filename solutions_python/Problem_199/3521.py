#!/usr/bin/env python

t = int(raw_input())  # read a line with a single integer
ans_num=['']*(t+1)
s=['']*(t+1)
k=[0]*(t+1)

def convert(pm):
    if pm=='+':
        conv_pm='-'
    else:
        conv_pm='+'
    return conv_pm

for i in xrange(1, t + 1):
    s[i],k[i]=raw_input().split()
    s[i]=list(s[i])
    k[i]=int(k[i])


for i in xrange(1,t+1):
    start=0
    cnt=0
    num=0
    while(num!=len(s[i])-(k[i]-1)-0):
#        print '---------condition: '+str(len(s[i])-(k[i]-1)-1)
#        print num
        for j in range(start,len(s[i])-(k[i]-1)):
            if s[i][j]=='-':
                for l in range(k[i]):
                    s[i][j+l]=convert(s[i][j+l])

                start=j
                cnt+=1
#                print 'new sequence: '+str(s)
#                print 'start: '+ str(start)
#                print 'cnt: '+str(cnt)
                break
        num+=1
#        if num>10:
#            break
    if '-' in s[i]:
        ans_num[i]='IMPOSSIBLE'
    else:
        ans_num[i]=cnt

for i in xrange(1,t+1):
    print "Case #{}: {}".format(i, ans_num[i])