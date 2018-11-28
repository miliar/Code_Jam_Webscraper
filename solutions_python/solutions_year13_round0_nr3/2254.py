f=open(r'C-small-attempt1.in','r')
test_cases=int(f.readline())
#test_cases=int(raw_input())
import math
#print test_cases
def fands(a,b,x):
    count=0
    for y in range(a,b+1):
        sr=math.sqrt(y)
        if int(sr)==sr:
            srnum=str(int(sr))
            lsr=list(srnum)
            #print lsr
            rsr=[n for n in reversed(lsr)]
            if lsr==rsr:
                num=str(y)
                l=list(num)
                r=[m for m in reversed(l)]
                if l==r:
                    count+=1
                    #print num
    print 'Case #%d: %d'%(x,count)
        
for x in range(1,test_cases+1):
    line=f.readline()
    #line=raw_input()
    line=line.split()
    #print line
    a=int(line[0])
    b=int(line[1])
    fands(a,b,x)
    #print "\n"
f.close()