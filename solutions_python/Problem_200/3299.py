file_object  = open('B-small-attempt0.in', 'r')
t = (file_object.readlines())
st = int(t[0].split()[0])
file_object.close()
file = open('testfile2_1.txt', 'w')
for z in range(1, st + 1):
    num = int(t[z].split()[0])
    bit=[]
    while(num!=0):
        bit.append(num%10)
        num=int(num/10)
    leng= len(bit)
    bit.reverse()
    res=[]
    res.append(bit[0])
    if leng==1:
        file.write("Case #{}: {}\n".format(z, res[0]))
    else:
        k=leng
        for i in range(1,leng):
            if bit[i]>bit[i-1]:
                res.append(bit[i])
                k=leng
            elif bit[i]<bit[i-1]:
                if k==leng:
                    res[-1]-=1
                    for j in range(leng-len(res)):
                        res.append(9)
                else:
                    res[k]-=1
                    for j in range(k+1,leng):
                        if j>len(res)-1:
                            res.append(9)
                        else:
                            res[j]=9
                break
            else:
                if k==leng:
                    k=i-1
                res.append(bit[i])
        
        l=len(res)
        fres=0
        for r in range(l):
            fres=10*fres+res[r]
        file.write("Case #{}: {}\n".format(z, fres))
file.close()
