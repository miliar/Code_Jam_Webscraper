def func(x,j):
    lst = x.split()
    cost = float(lst[0])
    inc = float(lst[1])
    final = float(lst[2])
    CookieRate = 2
    time = 0
    while(1):
        if final/CookieRate > ((cost/CookieRate) + (final/(CookieRate + inc))):
            
            time += float(cost/CookieRate)
            CookieRate+=inc
            #print time
        else:
	    #print time 
            time+= final/CookieRate
            break
    print "Case #"+(str)(j+1)+": "+(str)(time)
    answer_list.append(time)
cases = input()
j=0
answer_list=[]
while (j<cases):
    x= raw_input()
    func(x,j)
    j+=1


