infile = open('/home/suguman/Downloads/B-large.in','r')
outfile = open('/home/suguman/Desktop/output2.txt','w')

x = int(infile.readline())

for i in range(x):
    l = (infile.readline()).split()
    C = float(l[0])
    F = float(l[1])
    X = float(l[2])
    '''print(C, F, X)'''
    
    ans = X
    next_ans = X/2
    farm_time = 0
    k = 0
    den = 2
    while (next_ans < ans):
        ans = next_ans
        farm_time = farm_time + C/den
        den = den + F 
        next_ans = farm_time + X/den

    '''outfile.write('Case #'+str(i+1)+': ' + str(ans)+'\n')'''
    
    dec = ans - int(ans)
    dec = str(dec)
    '''print(dec)'''
    if (len(dec) > 8):
        last = int(dec[9])
        if (last >= 5):
            last = str(int(dec[8]) + 1)
        else:
            last = dec[8]
        
        ans = str(int(ans)) + '.' + dec[2:8] + last
    elif (len(dec) == 8):
        ans = str(ans)
        
    else:
        while(len(dec) < 8):
            dec = dec + '0'
        ans = str(int(ans)) + dec[1:]
        
        
    outfile.write('Case #'+str(i+1)+': ' + ans+'\n')
    
