def leftright(n):
    r = (n - 1) // 2
    l = (n - 1 - r)
    return (l,r)

def insertgap(gaps, gap, k):
    if gap in gaps:
        gaps[gap] += k
    else:
        gaps[gap] = k


def process(gaps, k):
    maxgap = max(gaps.keys())
    mult = gaps[maxgap]
    (leftgap, rightgap) = leftright(maxgap)
#   print("leftgap, rightgap", (leftgap,rightgap))
    if k <= mult:
        return [leftgap, rightgap] #finished
    else:
        del gaps[maxgap]
    
#   print("removedbig", gaps)
   
    insertgap(gaps,leftgap,mult)
#   print('addedleft', gaps)

    insertgap(gaps,rightgap,mult)
#   print('addedright', gaps)

    return process(gaps, k - mult)
    
    
    
    
    
    
t = int(input())


for i in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]  
    gaps = {n:1}
#   print("n k ", n, k)
    res = process(gaps,k) 
    print("Case #{}: {} {}".format(i,res[0],res[1]))
    



