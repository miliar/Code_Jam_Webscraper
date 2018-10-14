fin = file("A-large.in","r")
fout = file("A-large.out","w")
ls = [e.strip() for e in fin.readlines()]

T = int(ls.pop(0))
#print T
for case in xrange(T):
    li = ls.pop(0).split()
    n,k = int(li[0]), int(li[1])
        

    if ((k+1)%(2**n)==0): answer = "ON"
    else:                 answer = "OFF"
    

    temp = "Case #"+str(case+1)+": "+str(answer)+"\n"
    # temp
    fout.write(temp)
fout.close()

    
    
