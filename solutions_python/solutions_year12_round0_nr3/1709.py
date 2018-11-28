#!/usr/bin/env python

'''
Input

Output

3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

Case #1: 6
Case #2: 100
Case #3: 4
'''



def do(seq):
    print 'seq',seq
    limit1=int(seq[0])
    limit2=int(seq[1])

    ans=[]
    ansr=[]
    print 'START-------------------------'
    for i in xrange(limit1,limit2+1):
    ##    print i
        i=`i`
        r=i
        r1=r
        for j in xrange(len(i)):
    ##        print 'r',r
            r1=r1[-1]+r1[:-1]


            rnum=int(r)
            r1num=int(r1)


            if rnum>=r1num:continue
            if rnum>limit2 or rnum<limit1:continue
            if r1num>limit2 or r1num<limit1:continue

            if rnum in ans:
                rindex=ans.index(rnum)
                if ansr[rindex]==r1num:
    ##                print 'already at',rindex, ans[rindex],ansr[rindex]
                    continue

            ans.append(rnum)
            ansr.append(r1num)

    ##        print 'added', rnum,r1num

    print 'found',len(ans),len(ansr)
    return len(ans)

###seq=[("O",2),("B",1),("B",2),("O",4)]
####seq=[("O",5),("O",8),("B",100)]
####seq=[("B",2),("B",1)]
###
###print 'result', do(seq)





##print 'the end'
##sys.exit(0)

import sys
fname=sys.argv[1]

print 'fname',fname
input=[]
f=open(fname+'','r')
fout=open(fname+'.out','w')
numLine=int(f.readline())
for num in xrange(1,numLine+1):
    line=f.readline().strip()
    input=line.split()
    print 'linee',line
    print 'input',input

    print 'Case #'+`num`+': '+`do(input)`
    fout.write('Case #'+`num`+': '+`do(input)`+'\n')
fout.close()

