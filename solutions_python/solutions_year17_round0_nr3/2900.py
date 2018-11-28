def bathroom(n,k):
    ns = "0"*n
    last_t = []
    for j in range(k):
        max_1 =0
        max_2 =0
        selected = []
        for i in xrange(0,n):
            if(ns[i]=="0"):
                t = find_limits(ns,i)
                #print t
                if t[2]>max_1 or t[2]==max_1 and t[1]>max_2:
                    max_1 = t[2]
                    max_2 = t[1]
                    selected = [t]
                elif t[2]==max_1 and t[1]==max_2:
                    selected.append(t)
        last_t = selected[0]
        ns = ns[:last_t[0]] + "1"+ ns[(last_t[0]+1):]
        #print ns
    return str(last_t[1])+ " "+ str(last_t[2])

            
def find_limits(s,i):
    ls = i-s[:i].rfind("1")-1 if s[:i].rfind("1") != -1 else len(s[:i])  
    rs = s[(i+1):].find("1") if s[(i+1):].find("1") != -1 else len(s[(i+1):])
    return (i,max(ls,rs), min(ls,rs))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    print("Case #{}: {} ".format(i, bathroom(n,k)))