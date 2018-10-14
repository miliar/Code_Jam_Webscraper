def palin(n):
    if n%10==n:
        return True
    elif n%10==n/10:
        return True
    else:
        line=repr(n)
        v=True
        for x in range(len(line)/2):
            if line[x]!=line[len(line)-x-1]:
                v=False
                break
        return v
    
foo=open("input.in")
l=foo.readline().strip()
index=int(l)
for i in range(index):
    l=foo.readline().strip()
    min=int(str.split(l," ")[0])
    max=int(str.split(l," ")[1])
    numbers=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]
    revised=[]
    for x in numbers:
        if x>=min and x<=max:
            revised.append(x)
        if x>max:
            break
    count =0
    for x in revised:
        if palin(x) and palin(int(x**0.5)):
            count+=1
    print "Case #"+repr(i+1)+": "+repr(count);

