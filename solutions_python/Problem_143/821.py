TXT=open('2b.in')
inputlist=TXT.readlines()
TXT.close()

testCases=int(inputlist[0].strip())

line_cnt=1
OUT=open("2b.out",'w')
for tc in xrange(1,testCases+1):
    lineList=inputlist [line_cnt ].strip().split()
    A=int (lineList[0])
    B=int (lineList[1])
    K=int (lineList[2])
    line_cnt+=1
    cnt=0
    for i in xrange(0,A):
        for j in xrange(0,B):
            if i&j<K:
                cnt+=1
    OUT.write(  "Case #%d: %d\n" %(tc,cnt))


OUT.close()

