# -*- coding: utf-8 -*-



def recycle(num):
    s=str(num)
    global count
    setnum=set()
    for i in range(len(s)):
        recycled_s=s[i:]+s[:i]
        recycled_num=int(recycled_s)
        if recycled_num in setnum:
            continue
        setnum.add(recycled_num)
        if n <= num and num < recycled_num and recycled_num <= m:
            count = count + 1

infile=open('C-small-attempt0.in')
outfile=open('C-small-attempt0.out','w')
T=int(infile.readline().strip())
for case in range(1,T+1):
    n,m=infile.readline().split(' ')
#    print n,m
    n=int(n)
    m=int(m)
    count=0
    for num in range(n,m+1):
        recycle(num)
#    print count
    outfile.write('Case #%i: %d\n'%(case,count))
    
infile.close()
outfile.close()

    

