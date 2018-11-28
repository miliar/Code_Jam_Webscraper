def checkTidy(num):
    count = flag = temp = 0
    length = len(num)
    index = 0
    while(index != length - 1):
        if(int(num[index]) > int(num[index + 1])):
            return False
        index = index + 1
    return True

def getTidy(num):
    length = len(num)
    flag = index = 0
    while(index != length):
        if(index != length - 1 and int(num[index]) > int(num[index + 1]) and flag == 0 ):
           if(int(num[index+1])==0):
               num[index] = int(num[index]) - 1
               num[index+1] = 9
           else:
               num[index] = int(num[index]) - 1
           flag = 1
        else:
            if(flag==1):
                num[index] = 9
        index= index + 1
    return num
        

testcase = int(input())
result = []
case_counter = 0
while(testcase >= 1):
    testcase = testcase - 1
    case_counter = case_counter + 1
    n = int(input())
    
    if( int(n % 10) == n):
        result.append('Case #'+str(case_counter)+": "+str(n))
    else:
        n = list(str(n))
        while(checkTidy(n)!= True):
            n = getTidy(n)
        n = int(''.join(str(x) for x in n))
        result.append('Case #'+str(case_counter)+": "+str(n))

for word in result:
    print(word)
