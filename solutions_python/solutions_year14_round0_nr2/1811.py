cases = input()
j=0
answer_list=[]
while (j<cases):
    x= raw_input()
    lst = x.split()
    cost = float(lst[0])
    inc = float(lst[1])
    final = float(lst[2])
    cps = 2
    seconds = 0
    while(1):
        if final/cps > ((cost/cps) + (final/(cps + inc))):
            
            seconds += float(cost/cps)
            cps+=inc
            #print seconds
        else:
            seconds+= final/cps
            break
    answer_list.append(seconds)
    j+=1
i=0
while i<cases:
    print "Case #"+(str)(i+1)+":"+" "+(str)(answer_list[i])
    i+=1
