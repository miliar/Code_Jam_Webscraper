f = open('B-large.in','r')
o = open('testB.out','w')

runs = int(f.readline())
for i in range(runs):
    N = f.readline()
    dig = len(N)-1
    if(dig == 1):
        out = 'Case #'+str(i+1)+': '+str(int(N))+'\n'
        o.write(out)
        continue

    out = ''
    while dig > 0:
        count = 0
        while count <= 10:
            num = out+str(count)*dig
            if(int(num) > int(N)):
                out += str(count-1)
                break
            count+=1
        dig-=1
    out = 'Case #'+str(i+1)+': '+str(int(out))+'\n'
    o.write(out)
