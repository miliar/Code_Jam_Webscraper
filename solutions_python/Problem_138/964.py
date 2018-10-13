import sys

def deceitful_war(naomi,ken):
    #print naomi
    #print ken
    score = 0
    while len(naomi) > 0:
        ind = binary_search(ken,naomi[-1],0,len(ken)-1)
        if ind != -2:
            it_naomi = naomi.pop(0)
            it_ken = ken.pop()
            if it_naomi > it_ken:
                score += 1
        else:
            naomi.pop()
            ken.pop()
            score += 1
    return score                

def binary_search(arr,value,left,right):
    if left > right:
        if value < arr[0]:
            return -1    
        return -2
    mid = (left+right)/2
    if arr[mid] > value and arr[mid-1] < value:
        return mid
    elif arr[mid] < value:
        return binary_search(arr,value,mid+1,right)
    return binary_search(arr,value,left,mid-1)
def war(naomi,ken):
    #return -99
    score = 0
    while len(naomi) > 0:   
        it_naomi = naomi.pop()
        ind = binary_search(ken,it_naomi,0,len(ken)-1)
        #print "xxx",ind
        if ind == -1:
            ken.pop(0)
        elif ind == -2:
            score += 1
            ken.pop(0)
        else:
            ken.pop(ind)
    return score
T = int(sys.stdin.readline())
case = 1
for _ in xrange(T):
    n = int(sys.stdin.readline())
    naomi = map(float,sys.stdin.readline().strip().split())
    ken = map(float,sys.stdin.readline().strip().split())
    sorted_naomi = sorted(naomi)
    sorted_ken = sorted(ken)
    sorted_naomi1 = sorted_naomi[:]
    sorted_ken1 = sorted_ken[:]
    print "Case #%d: %d %d" %(case,deceitful_war(sorted_naomi,sorted_ken),war(sorted_naomi1,sorted_ken1))
    case += 1
