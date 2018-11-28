a=int(input())
b=a
f = open('out.txt', 'w')
while a>0:
    a-=1
    x=int(input())
    largest=x
    if len(str(x))>1:
        for j in range(x,9,-1):
            chk=0
            l=[int(d) for d in str(j)]
            for i in range(len(l)-1):
                if l[i] > l[i+1]:
                    chk=1
                    break
            if chk==0:
                largest=j
                break
    print('Case #'+str(b-a)+': '+str(largest))
    f.write('Case #'+str(b-a)+': '+str(largest)+'\n')
f.close()
