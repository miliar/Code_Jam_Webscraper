def flip(arr, j, k):
    for i in range(j, j+k):
        arr[i]=1-arr[i]

f = open('C:\\Users\\djspence\\Downloads\\A-large.in', 'r')

tries = int(f.readline())

for i in range(0, tries):
    a = f.readline().split(' ')
    pans = a[0]
    arr = []
    for j in range(0, len(pans)):
        if pans[j]=="+":
            arr.append(1)
        else:
            arr.append(0)
    k = int(a[1])
    flips = 0
    for l in range(0, len(pans)-k+1):
        if arr[l]==0:
            flip(arr, l, k)
            flips += 1
    if 0 in arr:
        print("Case #"+str(i+1)+": IMPOSSIBLE")
    else:
        print("Case #"+str(i+1)+": " + str(flips))
        