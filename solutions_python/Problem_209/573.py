import math

f = open("A-large (3).in","r").readlines()
g = open("A-large-out.txt",'w')
testcases = int(f[0])
line_no = 0

for j in range(1,testcases+1):
    line_no +=1
    n , kk = map(int, f[line_no].strip().split())
    arr = []
    for i in range(n):
        line_no += 1
        arr.append(list(map(int, f[line_no].strip().split())))
    
    arr_sor = sorted(arr, key = lambda x: 2*math.pi*x[0]*x[1])
    arr_sor.reverse()
    
    ans = [0 for q in range(n)]
    for k in range(n):
        base = arr_sor[k]
        cnt= 1
        area = math.pi * base[0] * base[0] + 2*math.pi*base[0]*base[1]
        for l in range(n):
            if l != k:                
                    if cnt == kk:
                        break
                    if arr_sor[l][0] <= base[0]:
                        area += 2*math.pi*arr_sor[l][0]*arr_sor[l][1]
                        cnt += 1
                    if cnt == kk:
                        break
        if cnt == kk:
            ans[k] = area
    print(ans)
    ans = round(max(ans),8)
    g.write("Case #"+ str(j) + ": " + str(ans) + "\n")     
                
        
        
        