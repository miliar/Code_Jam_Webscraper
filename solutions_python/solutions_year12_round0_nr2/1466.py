fptr = open('B-small-attempt1.in','r')
fptr2=open('xyz.txt','w')


test_cases=int(fptr.readline())
line_no=1
for line in fptr:
    tcase=line.split()
    i=0
    while i<len(tcase):
        tcase[i]=int(tcase[i])
        i=i+1
    #print tcase
    p=tcase[2]
    sc=tcase[1]
    count=0
    for score in tcase[3:]:
        print "score:",
        print score,
        if score>=p*3:
            print "####case1 "
            count+=1
            continue
        if ((score-p)/2) >(p-2):
            print "####case2 "
            count+=1
            continue
        if sc>0 and score-p>0 and score-p-p+2>=p-2 and p-2>=0:
            print "####case3 "
            count+=1
            sc-=1
            continue
        print "nothing"
    print count
    case="Case #"+str(line_no)+": "+str(count)
    if line_no!=test_cases:
        case = case+"\n"
    fptr2.write(case)
    line_no+=1

fptr.close()
fptr2.close()
