fil=open('C-small-attempt0.in','r')
x = fil.readline()
i = 0
p = open('rev.in','w')
fsq = [1,4,9,121,484]

while i<int(x):
    
    count=0
    y = fil.readline().split()
    print y
    for e in fsq:
        if e>=int(y[0]) and e<=int(y[1]):
            count+=1
    p.write("Case #"+str(i+1)+": "+str(count)+"\n")
    i+=1
p.close()
fil.close()
