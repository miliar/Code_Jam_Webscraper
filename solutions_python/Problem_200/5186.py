def tidy(num):
    num = str(num)
    # print "for value " + num
    flag = True
    i = 1
    while i < len(num):
        if(int(num[i])<int(num[i-1])):
             flag = False
             break
        i+=1
    return flag

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        a = input()
        while(a >= 1):
            if(tidy(a)):
                print("Case #%i: %s" % (caseNr,a))
                break;
            a-=1
