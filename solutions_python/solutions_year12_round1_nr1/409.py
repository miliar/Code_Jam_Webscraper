'''
Created on 2012-4-28

@author: islight
'''
def keystrokes(a,b,p):
    cases = (1<<a)-1
    exp = []
    for caseint in range(cases+1):
        case = bin(caseint)[2:]
        case = '0'*(a-len(case)) + case
        #print 'c:'+case,
        prob = 1
        for i in range(a):
            if case[i]=='1':
                prob = prob * p[i]
            else:
                prob = prob * (1.0-p[i])
        #print prob
        bexp = []
        for btime in range(a+1):
            modified = bin(caseint >> btime)[2:]
            modified = '0'*(a-len(modified)-btime) + modified
            #print 'm:'+modified
            if(a==btime):
                bexp.append( (btime + b+1)*prob)
            elif ('0' in modified):
                bexp.append( (btime*2+(b-a+1) +(b+1))*prob)
            else:
                bexp.append( (btime*2+(b-a+1))*prob)
        #print bexp
        exp.append(bexp)
    result = [0]*(a+1)                     
    for i in range(len(exp)):
        for j in range(len(exp[i])):
            result[j]+=exp[i][j]
    result.append(2+b)
    return min(result)


if __name__ == '__main__':
    file_name = "A-small-attempt0"
    f = open(file_name+'.in')
    f_out = open(file_name +'.out','w')
    num_of_cases = int(f.readline())
    for i in range(1,num_of_cases+1):
        s = f.readline()
        a,b = [int(x) for x in s.split()]
        s = f.readline()
        p = [float(x) for x in s.split()]
        expected = keystrokes(a,b,p)
        res = 'Case #%d: %f\n' % (i,expected)
        print res,
        f_out.write(res)
    f.close()
    f_out.close()