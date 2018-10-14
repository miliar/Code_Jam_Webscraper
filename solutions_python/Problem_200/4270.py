t=int(raw_input())
k=1
while t>0:
    n = str(raw_input())
    temp=[]
    long_int_string =str(n)
    for x in long_int_string:
        temp.append(int(x))
    while(1):
        if sorted(temp)==temp:
            magic = lambda nums: int(''.join(str(i) for i in temp))
            print("Case #%s: %s") % (str(k),magic(temp))
            k += 1
            break
        else:
            for i in range(len(temp)):
               try:
                    if temp[i]>temp[i+1]:
                        temp[i]=temp[i]-1
                        for j in range(i+1,len(temp)):
                            temp[j]=9
                    else:
                        continue
               except IndexError:
                    continue
    t-=1