numcases = input()
for i in range(numcases):
    stalls,ppl = map(int,raw_input().split())
    #import pdb;pdb.set_trace()
    row = ppl.bit_length()-1
    col = ppl-(1<<row)
    rowsum = max(0,stalls-(1<<(row+1))+1)
    filled = rowsum%(1<<row)
    minfill = rowsum/(1<<row)
    leftpart = int((minfill+1)/2.)
    rightpart = minfill/2
    if col<filled:
        if leftpart>rightpart:
            rightpart+=1
        else:
            leftpart+=1
    print "Case #%d: %d %d"%(i+1,leftpart,rightpart)
    