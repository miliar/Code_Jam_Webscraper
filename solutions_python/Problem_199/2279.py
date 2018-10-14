# 2017 Google code Jam first problem\

def PRINT(num, re):
    #print(re)
    if re[0] == 'no':
        print("Case #%d: IMPOSSIBLE" % (num+1))
    else:
        print("Case #%d: %d" %(num+1, re[1]))

def countflip(stt, gnum):
    plusC = stt.count('+')
    count=0
    result='yes'
    value=['yes', 0]
    stt1=[]
    for i in range(len(stt)):
        if stt[i]=='+':
            stt1.append(True)
        else:
            stt1.append(False)

    if len(stt)==plusC:
        return value
        

    while True:
        for i in range(gnum-1,len(stt1), 1):
            if stt1[i-(gnum-1)] == False:
                for j in range(gnum):
                    stt1[i-((gnum-j)-1)] = not stt1[i-((gnum-j)-1)]
                #    print(i-(gnum-j)-1)
                #print(stt1)
                count +=1
                    
        if (stt1.count(False) < gnum) and ((stt1.count(False) >= 1)):
            result='no'
            break
        if stt1.count(True)==len(stt1):
            break
    #print(stt1)
    #print(count)
    value[0]=result
    value[1]=count
    return value

def makestr():
    str1=input()
    list1=str1.split()
    str_ori=list1[0]
    str_count=list1[1]
    gril = int(str_count)
    
    R_1 = countflip(str_ori, gril)
    #return countflip(str_ori, gril)
    return R_1

testcase = int(input())

for i in range(testcase):
    PR=makestr()
    PRINT(i, PR)
