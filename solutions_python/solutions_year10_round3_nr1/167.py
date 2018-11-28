
def toadd(l1,l2):
    if (l1[0]-l2[0])*(l1[1]-l2[1])<0:
        return 1
    return 0

def solve(lst):
    tot = 0
    for i in range(len(lst)-1):
        cur = lst[i]
        for j in range(i+1,len(lst)):
            tot += toadd(cur,lst[j])
    return tot
            

T=int(input())
for case in range(1,T+1):
    nlines = int(input())
    lst = []
    for i in range(1,nlines+1):
        lst.append([int(w) for w in input().split()])
    print("Case #{0}: {1}".format(case, solve(lst)))
