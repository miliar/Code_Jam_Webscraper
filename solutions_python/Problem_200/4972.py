cases = raw_input()
for i in xrange(int(cases)):
    num = raw_input()
    if int(num) < 20:
        print "Case #"+str(i+1)+": "+num
    else:
        j=0
        while j <= len(num)-2:
            if int(num[j]) <= int(num[j+1]):
                j+=1
            else:
                if j!=0 and int(num[j])-1 >= int(num[j-1]):
                    result = str(int(num[:j+1])-1)
                    for k in xrange(len(num[j+1:])):
                        result += '9'
                    print "Case #"+str(i+1)+": "+result
                    break
                else:
                    if int(num[0])-1 > 0:
                        result = str(int(num[0])-1)
                        for k in xrange(len(num[1:])):
                            result += '9'
                        print "Case #"+str(i+1)+": "+result
                        break
                    else:
                        result='9'
                        for k in xrange(len(num[2:])):
                            result += '9'
                        print "Case #"+str(i+1)+": "+result
                        break
                j+=1
        if(j==len(num)-1):
            print "Case #"+str(i+1)+": "+num
            
