import sys;
testcase = int(input())
result = []
def checkArray(st):
    for i in range(0,len(st)):
        if(st[i] == '-' ):
            return False
    return True
case_counter = 0
while(testcase >= 1):
    testcase = testcase -1
    case_counter = case_counter + 1
    newvalue = input()
    s,k = newvalue.split()
    k = int(k)
    s= list(s)
    count = 0

    for i in range(0,len(s)):
        if(s[i]=='+'):
            continue
        else:
            if(k+i <= len(s)):
                count = count +1
                temp = k
                while(temp > 0):
                    temp = temp -1
                    if(s[i+temp]=='-'):
                        s[i+temp]='+'
                    else:
                        s[i+temp]='-'
            
    if(checkArray(s)==True):
        result.append("Case #"+str(case_counter)+": "+str(count))
    else:
        result.append("Case #"+str(case_counter)+": IMPOSSIBLE")

for word in result:
    print(word)
    
