f1 = open("C-small-2-attempt3.in","r")
f2 = open("results.txt","w")
data = f1.readlines()
k = int(data[0])
for ii in range(k):
    #print ii
    line=data[ii+1].split()
    n=int(line[0])
    k=int(line[1])
    left, right = 0,0
    maxheap=[None]*1000000
    maxheap[0]=n
    l=1
    if 3*k>2*n+9:
        f2.write("Case #"+str(ii+1)+": 0 0\n")
        continue
    for i in range(k):
        mx=maxheap[0]
        maxheap[0]=maxheap[l-1]
        # Adjusting heap
        j=0
        while 2*j+1<l-1:
            if 2*j+2<l-1 and maxheap[2*j+2]>maxheap[2*j+1] and maxheap[2*j+2]>maxheap[j]:
                temp=maxheap[j]
                maxheap[j]=maxheap[2*j+2]
                maxheap[2*j+2]=temp
                j=2*j+2
            elif maxheap[2*j+1]>maxheap[j]:
                temp=maxheap[j]
                maxheap[j]=maxheap[2*j+1]
                maxheap[2*j+1]=temp
                j=2*j+1
            else:
                break
        # Heap adjusted
        l-=1
        right = (mx-1)/2
        left = mx-1-right
        if left>0:
            maxheap[l]=left
            l+=1
            # Adjusting heap
            j=float(l-1)
            while j>0:
                par=int((j-1)/2.0)
                if maxheap[par]<maxheap[int(j)]:
                    maxheap[int(j)], maxheap[par] = maxheap[par], maxheap[int(j)]
                    j=float(par)
                else:
                    break
            # Heap adjusted 
        if right>0:
            maxheap[l]=right
            l+=1
            # Adjusting Heap
            j=float(l-1)
            while j>0:
                par=int((j-1)/2.0)
                if maxheap[par]<maxheap[int(j)]:
                    maxheap[int(j)], maxheap[par] = maxheap[par], maxheap[int(j)]
                    j=float(par)
                else:
                    break
            # Heap adjusted
    f2.write("Case #"+str(ii+1)+": "+str(left)+" "+str(right)+"\n")
f1.close()
f2.close()
