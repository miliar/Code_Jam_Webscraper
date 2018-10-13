__author__ = 'rui'
import math
def solve_1(dn, mlst):
    eat = 0
    pre = mlst[0]
    for m in mlst[1:]:
        delta = pre-m
        print ('delta',pre, m,delta)
        pre=m
        if delta>0:
            eat+=delta
        #print ('eat',eat)
    return eat
def solve_2(dn, mlst):
    eat=0
    eat0=0
    rate = 0
    #print ('rate',rate)
    for i in range(1,len(mlst)):
        delta=mlst[i-1]-mlst[i]
        mrate = delta*1.0/10
        if delta>0:
            eat0+=delta
        rate =max(rate,mrate)
        #print('rate',rate,mrate)
    for m in mlst[:-1]:
        if m-10*rate>0:
            eat+=10*rate
        else:
            eat+=m
        #print(m,rate*10,eat)
    return [ eat0,int(eat)]
infile = 'A-small-attempt3.in'
infile = 'A-large.in'
#infile = 'Atest.txt'
outfile = infile[:infile.find('.')]+'_out1.in'
output = open(outfile,'w')
with open(infile, 'r') as inf:
    n = int(inf.readline().replace('\n',''))
    for i in range(1,n+1):
        for j in range(2):
            tmp = inf.readline().replace('\n','')
            #output1.write('new case:'+'\t')
            if j ==0:
                dn = int(tmp)
                #output1.write('\t'.join(tmp.split(' '))+'\t')
            else:
               mlst = [int(x) for x in tmp.split(' ')]
                #output1.write('\t'.join(tmp.split(' '))+'\n')
        #print('new case',i, dn , mlst)
        #ret = solve_1(dn, mlst)
        ret,ret1 = solve_2(dn,mlst)
        #print('result',ret,ret1)
        tret = 'Case #%s: %s %s'%(str(i),str(ret),str(ret1))
        output.write(tret+'\n')