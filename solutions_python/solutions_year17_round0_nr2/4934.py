t=int(input())
for i in range(1,t+1):
    n=int(input())
    for j in range(n,0,-1):
        st=[int(x) for x in str(j)]
        if sorted(st)==st :
            print("Case #{}: {}".format(i,j))
            break
    #print(arr)