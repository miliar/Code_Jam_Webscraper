def is_largest(arr):
    tmp = arr[0]
    for n in arr:
        if n < tmp:
            return False
        tmp = n
    return True


"""
def resolve(num,flagnum,idx):
    if num <= 0:
        #print "num:{0},idx:{1} in resolve".format(num,idx)
        if idx == 0:
            return 0
        else:
            return flagnum
    return min(num,flagnum)
"""
def solve(arr):
    if is_largest(arr):
        return arr
    ans = []
#1233321 -> 1233299 -> 1232999 -> 1229999
#1234554321 -> 1234549999 -> 1234499999
    for i in xrange(0,len(arr)):
        if arr[i+1] < arr[i]:
            arr[i] -= 1
            ans = arr[:i+1] + [9]*(len(arr)-i-1)
            break
    return ans

for t in xrange(1,input()+1):
    arr = map(int,list(raw_input()))
    while True:
        ans = solve(arr)
        #print ans
        if is_largest(ans):
            break
    print "Case #{0}: {1}".format(t,reduce(lambda acc,x:acc*10+x,ans))
