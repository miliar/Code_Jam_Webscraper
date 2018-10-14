import sys

with open(sys.argv[1]) as f:
    for n in range(int(f.readline().strip())):
        dim = int(f.readline().strip())
        arr  = []
        for row in range(dim):
            line = reversed(f.readline().strip())
            i = dim
            for letter in line:
                if letter == '1':
                    break
                else:
                    i -= 1
            arr.append(i-1)
        swaps = 0
#        print(arr)
        for i in range(len(arr)):
            if arr[i]>i:
                ind = i
                for x in range(i,len(arr)):
                    if arr[x]<= i:
                        ind = x
                        break
#                print (arr)
                swaps += x-i
#                print("swapping ",i,x)
                arr.insert(i,arr.pop(x))

#        print(arr)
#        done = False
#        while not done:
#            done = True
#            for i in range(len(arr)):
                
#                if (not i == dim-1) and arr[i] > arr[i+1]:#arr[i]>i and arr[i] > arr[i+1]:
#                    done = False
#                    arr[i],arr[i+1]=arr[i+1],arr[i]
#                    swaps += 1
#                    print (arr, i)
        print("Case #",str(n+1),": ",str(swaps),sep="")
#        print(arr)
#        print()
