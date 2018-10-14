#Meet Shah - DAIICT
#GCJ Qualification B
def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

t = int(input())
for i in range(t):
    n = input()
    arr = list(n)
    #print(arr)
    foo = True
    
    arr = list(map(int, arr))
    for x in range(1,len(arr)):
        for j in range(len(arr)):
            foo = True
            for k in range(j+1,len(arr)):
                #print(j,k,arr[j],arr[k])
                if(arr[j]>arr[k]):
                    if(foo):
                        arr[j]-=1
                        foo = False
                        for xx in range(j+1,len(arr)):
                            arr[xx] = 9
                break
    print("Case #",i+1,": ",magic(arr),sep='')
                
    