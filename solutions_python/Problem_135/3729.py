ins = raw_input("???")
slines = ins.splitlines()
no_pros = int(slines.pop(0))

tl = -1
for pro in range(no_pros):
    ans_ln1 = None
    ans_ln2 = None
    
    ln1 = None
    ln2 = None
        
    for line in range(10):
        tl +=1
        if line < 5:
            if line == 0:
                ln1 =  int(slines[tl])
                continue
            
            if line ==  ln1:
                ans_ln1 = slines[tl]
                

        if line >= 5:
            if line == 5:
                ln2 =  int(slines[tl])
                continue
            
            if(line - 5) ==  ln2:
                ans_ln2 = slines[tl]
                
                
##    print ans_ln1,"aaaaaaa",ans_ln2
    ans_ln1 = ans_ln1.split(' ')
    ans_ln2 = ans_ln2.split(' ')
    ans = list(set(ans_ln1) & set(ans_ln2))
##    print ans

##    print len(ans),ans
    if len(ans) == 0:
        print "Case #{}: Volunteer cheated!".format(pro+1)

    elif(len(ans) == 1):
        print "Case #{}: {}".format(pro+1,ans[0])
    
    elif(len(ans) > 1) :
        print "Case #{}: Bad magician!".format(pro+1)
        
        
##    while tl > 0:
##
##        tl -= 1
    
