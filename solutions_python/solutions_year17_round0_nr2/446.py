def numberfy(arr):
    out = 0
    for i in arr:
        out = out+i
        out = out*10
    out = out/10
    return out
    
def fix(arr, loc):
    arr[loc] = arr[loc] - 1
    for i in range(loc+1, len(arr)):
        arr[i]=9

f = open('C:\\Users\\djspence\\Downloads\\B-large.in', 'r')

tries = int(f.readline())

for case in range(0, tries):
    num = f.readline().strip()
    arr = []
    for i in num:
        arr.append(int(i))
    for j in range(0, len(arr)-1):
        testingLoc = len(arr)-1-j
        if arr[testingLoc]<arr[testingLoc - 1]:
            fix(arr, testingLoc - 1)
    print("Case #"+str(case+1) + ": " + str(numberfy(arr)))