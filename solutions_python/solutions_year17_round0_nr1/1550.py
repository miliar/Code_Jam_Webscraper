

def parsedToNormal(parsed):
    return "".join(map(lambda x: x*"+" if x >0 else abs(x)*"-",parsed))

def result(pans,parsed,n):
    flips = 0
    
    funcs = [flipmultiple,flipleft]
    while not (len(parsed)==1 and parsed[0]>0):
        for f in funcs:            
            pans,parsed, flipsToAdd = f(pans,parsed,n)
            #print(pans,parsed, flipsToAdd)
            if flipsToAdd <0:                
                return "IMPOSSIBLE"
            parsed = repair(parsed)
            flips += flipsToAdd
            if flipsToAdd > 0: break         

    return flips
    


def flipmultiple(pans,parsed,n):
    res = []
    flips = 0
    for k in parsed:
        if k < 0 and k % n == 0:
            res.append(-k)
            flips+= -int(k/n)
        else: 
            res.append(k)
    return parsedToNormal(res),res,flips

def flipleft(pans,parsed,n): 
    table = {"+":"-","-":"+"}
    res = ""
    while pans and pans[0]=="+":
        res+="+"
        pans=pans[1:]
    if len(pans) > n:
        for i in range(n):
            res+=table[pans[i]]
        res+=pans[n:]
    else:
        return None,None,-1
        
    
    return (res,parse(res),1)
    
    

def repair(pans):
    res = []
    func = [lambda x: x > 0, lambda x: x < 0]
    while pans:
        for f in func:
            if pans and f(pans[0]):
                taken = takeWhile(f,pans)
                pans = pans[len(taken):]
                res.append(sum(taken))
    return res

def parse(pans):
    res = []
    while pans:
        if pans[0] == '+':
            count = len([k for k in takeWhile(lambda x: x == '+',pans)])
            pans = pans[count:]
            res.append(count)
        else:
            count = len([k for k in takeWhile(lambda x: x == '-',pans)])
            pans = pans[count:]
            res.append(-count)
    return res


def takeWhile(pred, x):
    res = []
    for k in x:
        if pred(k):
            res.append(k)
        else:
            break
    return res
        

t = int(input()) 
for i in range(1, t + 1):
    
    #print(str(flip("++++++",2,3)))
    
    pans0, n0 = input().split(" ")
    pans00 = parse(pans0)
    n00 = int(n0)
    #print(pans0, pans00)
    print("Case #{}: {}".format(i, result(pans0,pans00,n00)))
