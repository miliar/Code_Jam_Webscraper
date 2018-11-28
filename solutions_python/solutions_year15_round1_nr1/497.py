T = int(raw_input())
def first(M):
    last = -1
    total = 0
    for m in M:
        if m < last:
            total += last-m
        last = m
    return total
        
def second(M):
    #get biggest diff
    last = M[0]
    biggest = 0
    for m in M:
        if last - m > biggest:
            biggest = last-m
        last = m
    
    total = 0
    for index,m in enumerate(M):
        if index == len(M)-1:continue
        calc = m - biggest
        if calc >=0 :
            total += biggest
        else:
            total += (biggest+calc)
    return total

for case in range(T):
    N = int(raw_input())
    M = map(int,raw_input().split())
    
    print "Case #"+str(case+1)+": "+str(first(M)) + " "+str(second(M))