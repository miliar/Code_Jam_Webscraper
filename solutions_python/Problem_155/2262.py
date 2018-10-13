foo = open("A-large.in",'r')
bar = open("output-big.txt",'w')
t = int(foo.readline().strip())
z=0
while t:
    t-=1
    z+=1
    total = 0
    frnds = 0
    a =  foo.readline().strip().split()
    no = int(a[0])
    shy = list(a[1])

    for i in range (no+1):
        if total<i:
            frnds += i-total
            total=i
        total += int(shy[i])


    res = "Case #"+str(z)+": "+str(frnds)
    print res
    bar.write(res+'\n')
    

bar.close()
foo.close()
 
