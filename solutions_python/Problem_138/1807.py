TXT=open('din.txt')
inputlist=TXT.readlines()
TXT.close()

testCases=int(inputlist[0].strip())

line_cnt=1
OUT=open("dout.txt",'w')
for tc in xrange(1,testCases+1):
    numOfEle=int (inputlist[line_cnt ])
    line_cnt+=1
    AList_t=inputlist [line_cnt ].strip().split(' ')
    BList_t=inputlist [line_cnt+1 ].strip().split(' ')
    line_cnt+=2
    AList=[]
    BList=[]
    AList_o=[]
    BList_o=[]
    d_count=0
    o_count=0
    for i in xrange(0,numOfEle):
        AEle=float(AList_t[i])
        BEle=float(BList_t[i])
        AList.append(AEle)
        BList.append(BEle)
        AList_o.append(AEle)
        BList_o.append(BEle)

    ignoredList=[]
    o_count=0
    AList_o.sort(reverse=True)
    BList_o.sort()
    for ae in BList_o:
        big_ele=''
        min_ele=''
        for be in AList_o:
            if be not in ignoredList :
                if big_ele=='':
                    big_ele=be
                if ae>be:
                    min_ele=be
        if min_ele =='':
            ignoredList.append(big_ele)
        else:
            ignoredList.append(min_ele )
            o_count+=1
    o_count=numOfEle-o_count

    ignoredList=[]
    print sorted(AList)
    print sorted(BList)
    AList.sort()
    BList.sort(reverse=True)
    for ae in AList:
        big_ele=''
        min_ele=''
        for be in BList:
            if be not in ignoredList :
                if big_ele=='':
                    big_ele=be
                if ae>be:
                    min_ele=be
        if min_ele =='':
            ignoredList.append(big_ele)
        else:
            ignoredList.append(min_ele )
            d_count+=1
    OUT.write(  "Case #%d: %d %d\n" %(tc,d_count,o_count))

OUT.close()

