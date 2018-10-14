t = int(raw_input())

for i in xrange(1, t+1):
    digits = [int(d) for d in list(raw_input())]
    for j in reversed(xrange(1, len(digits))):
        if (digits[j-1] > digits[j]):
            digits[j-1] -= 1
            for k in xrange(j,len(digits)): 
                digits[k] = 9
    
    answer = ''.join(map(str,digits))

    for h in xrange(len(answer)):
        if answer[h] != '0':
            break

    answer = answer[h:] 
    print "Case #{}: {}".format(i,answer)  
