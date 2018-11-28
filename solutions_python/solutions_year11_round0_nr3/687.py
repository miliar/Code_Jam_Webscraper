from itertools import combinations

def psum(list,selected):
    sums = 0
    sumns = 0
    i = 0
    for n in list:
        if i in selected:
            sums ^= n
        else:
            sumns ^= n
        i+=1
    return sums == sumns
def rsum(list, selected):
    sum = 0
    for n in selected:
        sum += list[n]
    return sum
def ssum(list, selected):
    sum = 0
    i=0
    for n in list:
        if not i in selected:
            sum += n
        i+=1
    return sum

t = input()
i=0
while i<t:
    i+=1
    n = input()
    s = []
    p = []
    for num in raw_input().split():
        s+=[int(num)]
    s.sort()
    j=1
    sol = []
    minsum = 0
    minsumtupl = -1
    while j<=n/2:
        for e in combinations(range(n),j):
            if psum(s,e):
                csum = rsum(s,e)
                if minsum > csum or minsum==0:
                    minsumtupl = e
                    minsum = csum
                
            
        j+=1
    print "Case #"+str(i)+":",
    if minsum == 0:
        print "NO"
    else:
        print ssum(s,minsumtupl)

    
    
    
