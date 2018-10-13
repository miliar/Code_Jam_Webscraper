data = open('B-large.in','r')
d = open('B-large.out','w')
tc = int(data.readline())
#tc = int(raw_input())
for t in range(tc):
    numb = map(int,str(int(data.readline())))
#    numb = map(int,raw_input())
    numb2 = list(numb)
    numb2.sort()
    numb2.reverse()
    numb.reverse()
    i = 0
    cf = 0
    while (numb != numb2 or cf == 1) and i != len(numb) :
        if i == 0:
            if numb2[0] > numb[i]:
                numb[i] = 9
                cf =1
        else:
            if cf == 1:
                cf = 0
                numb[i] = numb[i]-1
                re = str(numb[i]+10)
                if numb[i] != int(re[len(re)-1]): cf = 1
                numb[i] = int(re[len(re)-1])
            if numb[i] > numb[i-1]:
                numb[i] = numb[i]-1
                re = str(numb[i]+10)
                if numb[i] != int(re[len(re)-1]): cf = 1
                numb[i] = int(re[len(re)-1]) 
                numb[:i] = [9] *(i)
        i += 1
        numb2 = list(numb)
        numb2.sort()
        numb2.reverse()
    if cf ==1 : numb[len(numb)-1] = 0
    numb.reverse()
    numb = "".join(map(str,numb))
    numb = int(numb)
    print >>d, ("Case #" + str(t+1)+ ": " + str(numb))
#    print "Case #" + str(t+1)+ ": " + str(numb)
d.close()
        
    
    
    
