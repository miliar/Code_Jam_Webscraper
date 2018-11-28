import math 

def solve(a, b, k):
    res = 0
    for p1 in a:
        x =      p1[0] ** 2
        x += 2 * p1[0] * p1[1]
        size = 1
        r = p1[0]
        i = p1[2]
        
        for p2 in b:
            if (size == k):
                break          
            if (p2[1] <= r) and (p2[2] != i):
                x += p2[0]
                size += 1
        if (size == k) and (x > res):
            res = x
            
    return res * math.pi  
    

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())
for case in range(1, t + 1):
    n, k = map(int, fin.readline().strip().split())
    a = []
    b = []
    for i in range(n):
        a.append(list(map(int, fin.readline().strip().split())))
        a[i].append(i) 
        b.append([2 * a[i][0] * a[i][1], a[i][0], i])       
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = solve(a, b, k)
    fout.write("Case #" + str(case) + ": " + str(ans) + "\n")

fin.close()
fout.close()