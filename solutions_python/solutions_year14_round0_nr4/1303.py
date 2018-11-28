

def get_line():
    return raw_input().strip()
     
formatFloatList = lambda s: list(map(float,s.split(' ')))

def standard_input():
    count = int(get_line())
    for i in range(count):
        N = int(get_line())
        naomi = formatFloatList(get_line())
        ken = formatFloatList(get_line())
        yield (i+1,(N,naomi,ken))

def first_over(lst, n):
    for i in lst:
        if i > n:
            return i
    return None
        
def warOutput(N, naomi, ken):
    result = 0
    for i in range(N):
        nmax = naomi[len(naomi) - 1]
        naomi.remove(nmax)
        kls = first_over(ken, nmax)
        if kls:
            ken.remove(kls)
        else:
            result += 1
            ken.remove(ken[0])  
    return result
        
def decitfulWarOutput(N, naomi, ken):
    best = 0
    for i in range(N):
        breakFlag = False
        for j in range(N-i):
            if ken[j] >= naomi[i + j]:
                breakFlag = True
                break
        if breakFlag:
            continue
        best = N - i
        break
    return max(best, warOutput(N, naomi, ken))
   
def handle_case(case):
    N, naomi, ken = case
    naomi.sort()
    ken.sort()
    o1 = decitfulWarOutput(N, naomi[:], ken[:])
    o2 = warOutput(N, naomi[:], ken[:])
    return "%d %d" % (o1, o2)
    
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))
        

if __name__ == '__main__':
    main()