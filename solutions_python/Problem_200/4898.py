def isTidy(s):
    for i in range(len(s)-1):
        if(s[i] < s[i+1]):
            return False
    return True
def MakeTidy(s):
    # s.reverse()
    i = 0
    while(True):
        length = len(s)
        # print s[i], s[i+1]
        if(s[i] < s[i+1] and s[i+1] != '0'):
            s[i] = '9'
            s[i+1] = str(int(s[i+1])-1)
            i=i+1
        elif (s[i] < s[i+1] and s[i+1] == '0'):
            s[i] = '9'
            if( i+1 < length-1):
                s = s[:i+1]+s[i+2]
                s[i+1] = '9'
                i=i+1
            else:
                s[i+1] = '9'
                i=i+1
        else:
            i=i+1
        if(i == length-1):
            return s
def getResult(z):
    ind = -1
    if(not isTidy(z)):
        i= 0
        while(True):
            if(z[i] < z[i+1]):
                ind = i
                break
            i = i+1
    else:
        return ''.join(a for a in z[-1::-1])
    first  = []
    for j in range(i):
        first.append('9')
    result= first + MakeTidy(z[i:])
    if result[len(result)-1] == '0':
        result = result[-1::-1]
        result = result[1:]
        final = ''.join(x for x in result)
    else:
        result=result[-1::-1]
        final = ''.join(x for x in result)
    return final
if __name__ == '__main__':
    noOfTestCases = int(raw_input())
    for i in range(noOfTestCases):
        x= str(raw_input())
        x= x[-1::-1]
        z= [a for a in x]
        print "Case #"+str(i+1)+": "+getResult(z)

