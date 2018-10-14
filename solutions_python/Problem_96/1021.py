import sys
wt=sys.stdout.write
f=open('a2.in')
NUM=int(f.readline())
i=0
while i<NUM:
    i+=1
    l=map(int,f.readline().split(' '))
    wt('Case #%d: '%i)
    person_count=l[0]
    suprising=l[1]
    p=l[2]
    l=l[3:]
    r=0
    for total in l:
        if p<1:a=0
        else: a=p+p-1+p-1
        if a<=total:
            r+=1
        elif p>=2 and suprising>0:
            a=p+p-2+p-2
            if a<=total:
                r+=1
                suprising-=1
    print r
