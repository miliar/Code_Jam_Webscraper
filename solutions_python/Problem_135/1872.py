TXT=open('ain.txt')
inputlist=TXT.readlines()
TXT.close()

testCases=int(inputlist[0].strip())

line_cnt=1
OUT=open("aout.txt",'w')
for tc in xrange(1,testCases+1):
    first_ans=int(inputlist[line_cnt].strip())
    first_set=inputlist[line_cnt+first_ans].strip().split(' ')
    line_cnt+=5
    second_ans=int(inputlist[line_cnt].strip())
    second_set=inputlist[line_cnt+second_ans].strip().split(' ')
    line_cnt+=5
    found=0
    card=0
    for item in first_set:
        if item in second_set:
            found+=1
            card=item
    if found==1:
        OUT.write( "Case #%d: %s\n" %(tc,card))
    elif found>1:
        OUT.write(  "Case #%d: Bad magician!\n" %tc)
    else:
        OUT.write(  "Case #%d: Volunteer cheated!\n" %tc)

OUT.close()

