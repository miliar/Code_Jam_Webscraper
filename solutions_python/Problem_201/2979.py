import sys
i = int(sys.stdin.readline()[:-1])
def best(ar):
    index = -1
    score = -1,-1
    l = -1
    h = -1
    for i in range(len(ar)):
        if(ar[i]):
            #print(i)
            l = h
            h = i
            for j in range(l+1,h):
                s = (h-j-1,j-l-1)
                if(min(s) > min(score) or (min(s) == min(score) and max(s) > max(score))):
                    score = s
                    index = j
    return index,score
                
            
                

for i in range(i):
    n,k = tuple([int(i) for i in sys.stdin.readline()[:-1].split(" ")])
    l = [False]*n + [True]
    s = None
    for j in range(k):
        s = best(l)
        l[s[0]] = True
    print("Case #" + str(i+1) + ": "+(str(s[1][0]) + " " + str(s[1][1])))
    
