import sys

def rec(arr,last):
    while last>=0 and arr[last]==0:
        last -= 1
    if last == -1:
        return 0
    if last in [1,2,3]:
        return last
    
    mn = last
    left = 2
    while left<=last/2:
        recarr = arr[:]
        recarr[last] -= 1
        recarr[left] += 1
        recarr[last-left] += 1
        time = rec(recarr,last)
        if time+1 < mn:
            mn = time+1
        left += 1
    return mn


f=open(sys.argv[1],'r')
g=open(sys.argv[2],'w')

cases = int(f.readline().split()[0])
case=1
while case<=cases:
    diners = int(f.readline().split()[0])
    cakes = f.readline().split()
    arr = [0]*10
    for cake in cakes:
        arr[int(cake)] += 1
    result = rec(arr,9)
    g.write("Case #{}: {}\n".format(case,result))
    case += 1
    

f.close()
g.close()


