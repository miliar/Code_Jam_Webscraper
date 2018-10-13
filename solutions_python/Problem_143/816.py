test = input()
for t in range(1,test+1):
    count=0
    s=raw_input()
    l=s.split()
    l=map(int,l)
    for i in range(0,l[0]):
        for j in range(0,l[1]):
            if i&j < l[2]:
                count+=1
    print "Case #"+str(t)+": "+str(count)
