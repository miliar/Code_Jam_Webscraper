input_list = []
f1 = open('B-small-attempt3.in')
for line in f1:
    intList = line.strip().split()
    input_list.append(intList[0])
f1.close
f2 = open('B-small-attempt3.out','w')
t = int(input_list[0])
for a0 in range(1,t+1):
    n = int(input_list[a0])
    if(len(str(n))==1):
        f2.write('Case #'+str(a0)+': '+str(n)+'\n')
        continue
    while(True):
        lst = list(str(n))
        if(lst==sorted(lst)):
            f2.write('Case #'+str(a0)+': '+str(n)+'\n')
            break
        n-=1
f2.close()
        
        
