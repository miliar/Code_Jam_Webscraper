import sets
file=open("inputC.txt", 'r')
output=open("outC.txt",'w')

input=iter(file)
X=input.readline()


b=0
for b, k in enumerate(input):    
    a= k.split(' ')
    A=int(a[0])
    B=int(a[1].rstrip())

    dict1={}
    dict2={}
    dict3={}
    size=len(str(A))
    for i in range (A,B+1):
        if size==2:
            ters1=int(str(i)[-1]+str(i)[0:-1])
            if (i<ters1 and ters1<B+1):
                dict1.update({i:ters1})
        elif size==3:
            ters1=int(str(i)[-1]+str(i)[0:-1])
            ters2=int(str(i)[-2:]+str(i)[0:-2])
            if (i<ters1 and ters1<B+1):
                dict1.update({i:ters1})
            if (i<ters2 and ters2<B+1):
                dict2.update({i:ters2})
        elif size==4:
            ters1=int(str(i)[-1]+str(i)[0:-1])
            ters2=int(str(i)[-2:]+str(i)[0:-2])
            ters3=int(str(i)[-3:]+str(i)[0:-3])
            if (i<ters1 and ters1<B+1):
                dict1.update({i:ters1})
            if (i<ters2 and ters2<B+1):
                dict2.update({i:ters2})
            if (i<ters3 and ters3<B+1):
                dict3.update({i:ters3})
    count1=0
    count2=0
    count3=0
    #print dict1
    #print dict2
    for i in dict1:
        count1+=1
    for i in dict2:
        count2+=1
    for i in dict3:
        count3+=1

    count_shared_item=0
    if size == 3:
        shared_item = set(dict1.items()) & set(dict2.items() )
        count_shared_item=len(shared_item)
    if size == 4:
        shared_item1 = set(dict1.items()) & set(dict2.items() )
        shared_item2 = set(dict1.items()) & set(dict3.items() )
        shared_item3 = set(dict2.items()) & set(dict3.items() )
        count_shared_item=len(shared_item1)+ len(shared_item2) + len(shared_item3)

    count = count1+count2+count3-count_shared_item
#    print count
    print >>output, "Case #%d:" % (b+1), count
file.close()
output.close()
