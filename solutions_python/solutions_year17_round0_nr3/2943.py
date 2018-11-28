import bisect
def BathroomStalls(nOfToilets, nOfPersons):
#    print("number of toilets" + (str)(nOfToilets))
    a = [0,nOfToilets]
    start = 0
    gap = 0
    for i in range(0,nOfPersons - 1):
        start = 0
        gap = 0
 #       print(i)
   #     print(a)
        #find largest gap
        a1 = 0
#        print(a)
        for num in a:
            if(num-a1 > gap):
                gap= num - a1
                start = a1
            a1 = num
#        print((str)(start) + " " + (str)(gap))
        bisect.insort(a, (int)(start + gap/2))
#        print("inserting")
#        print(a)
    a1 = 0
    gap = 0
    start = 0
    for num in a:
        if(num-a1 > gap):
            gap= num - a1
            start = a1
        a1 = num
#    print(a)
    print("gap is" + str(gap))
    if(nOfPersons == 1 and gap%2 == 0):
        return [int(gap/2 - 1), int(gap/2)]

    if(nOfPersons == 1 and gap%2 == 1):
        return [int(gap/2), int(gap/2)]       
    if(gap == 1):
        return [0, 0]
    print(str(start) + " " + str(gap) + " " + str(a[len(a)-1]))
    if(start != 0):
        gap -= 1
    print(gap)
    if(gap%2 == 0):
        return [int(gap/2), int(gap/2 - 1)]
    
    if(gap%2 == 1):
        return [int(gap/2), int(gap/2)]        


a = []
k = 0
#with open("test.txt") as fin:
with open("C-small-1-attempt4.in") as fin:
    for line in fin:
#        print(k)
        a.append(line)
        k += 1
#print(a)
f = open('out.txt','w')
cases = a[0]
#print(cases)
for i in range(1,(int)(cases) + 1):
#    print("newCase")
    f.write("Case #" + (str)(i) + ":")
    b = a[i].split(' ')
#    print(b)
    num = BathroomStalls((int)(b[0]),(int)(b[1]))
    if((int)(num[0]) < (int)(num[1])):
        min = (int)(num[0])
        max = (int)(num[1])
    else: 
        min = (int)(num[1])
        max = (int)(num[0])
#    print(a[i])
#    print(num)
    f.write(" " + (str)(max) + " " + (str)(min) + "\n")
f.close()
