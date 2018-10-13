text_file = open("samp.txt", "r")
lines = text_file.read().splitlines()
text_file.close()
x=len(lines)
result = open("res.txt", "w")
for i in range(1,x):
    b=lines[i]
    c=b.split()
    z=0
    y=0
    ff=len(c)
    print ff
    print c[0]
    d=str(c[1])
    p=int(d[0])
    e=len(d)
    z=z+p
    for j in range(1,e):
        s=int(d[j])
        if(z>=j):
            z=z+s
        else:
            y=y+j-z
            z=s+j
    print "Case #1:",y
    s=str(y)
    v='case #'+str(i)+': '+str(y)+'\n'
    result.write(v)
        