lines = open("input.txt","r").readlines()
f = open('workfile', 'a+')
k = 0
for line in lines[1:]:
    a = int(line)
    k+=1
    for i in range(a,0,-1):
        b = str(i)
        c = ''.join(sorted(b))
        if(b==c):
            f.write(("Case #%s: "%k)+(str(i)+'\n'))
            break
