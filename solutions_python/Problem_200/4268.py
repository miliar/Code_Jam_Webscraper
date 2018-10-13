T = int(input())

def solve(nlist):
    c = 0
    for i in range(len(nlist)-1):
        j = i+1
        
        while nlist[i] > nlist[j]:
            l = int(nlist[j])
            d = int(nlist[i])
            l -= 1
            if l == -1:
                l = 9
            nlist[j] = str(l)
            if l == 9 and c == 0:
                c += 1
                d -= 1
                nlist[i] = str(d)

    
    if ''.join(nlist) != ''.join(sorted(nlist)):
        solve(nlist)

for c in range(1,T+1):
    num = input()
    nlist = list(num)
    solve(nlist)

    num = ''.join(nlist)
    n = int(num)
    print("Case #"+str(c)+":",n)
