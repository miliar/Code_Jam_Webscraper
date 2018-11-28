#!/usr/bin/python
cases = input()
for T in range(cases):
    n = input()
    inputString = raw_input()
    inputString = inputString.split(' ')

    xor = int(inputString[0])
    inputString.pop(0)
    min_num = xor
    sum_num = xor
    for num in inputString:
        xor = int(num) ^ xor
        min_num = min(min_num,int(num))
        sum_num += int(num)

    if xor!=0:
        print 'Case #%(T)d: NO'% {'T':T+1}
    else:    
        print 'Case #%(T)d: %(ans)d'% {'T':T+1,'ans':sum_num-min_num}


