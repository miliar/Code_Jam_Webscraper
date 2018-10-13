#!/usr/bin/python
cases = int(input())
for T in range(cases):
    inputString = raw_input()
    inputString = inputString.split()
    
    n = int(inputString[0])
    combine={}
    for i in range(n):
        key = inputString[i+1][0:2]
        combine[key]=inputString[i+1][2]
        key = inputString[i+1][1::-1]
        combine[key]=inputString[i+1][2]


    m = int(inputString[n+1])
    oposed=[]
    for i in range(m):
        oposed += [inputString[i+n+2]]


    invoke = (inputString[n+m+3])

    list=""
    len = 0
    for s in invoke:
        list += s
        tail = list[-2:]
        if tail in combine:
            list = list.replace(tail,combine[tail])
   #         print list
        
        has_opsed = 0
        for op in oposed:
            if list.find(op[0])!=-1 and list.find(op[1])!=-1:
                has_opsed=1
                break;
        
        if has_opsed==1:
            list=""




    ans = '['+', '.join(list)+']'
    print 'Case #%(T)d: '%{'T':T+1} + ans
