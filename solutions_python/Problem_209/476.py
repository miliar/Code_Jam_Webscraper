import sys

f = sys.stdin

PI = 3.14159265359

for cas in range(1,1+int(f.readline())):
    (n,k) = map(int,f.readline().split())
#    print(n,k)
    rhlist = [tuple(map(int,f.readline().split())) for _ in range(n)]
#    print(rhlist)
    rhlista = sorted([(r*h,r,h)  for r,h in rhlist], reverse = True)
#    print(rhlista)
    ans1 = []
    for i in range(0,n-k+1):
        rhsum =sum( [2*rh for (rh,r,h) in  rhlista[i:i+k]])
        rmax = max([r for (rh,r,h) in rhlista[i:i+k]])
        ans1.append(PI*(rhsum + rmax*rmax))
    max1 = max(ans1)

    ans2 = []
    for i in range(0,n-(k-1)+1):
        rhsum = [2*rh for (rh,r,h) in rhlista[i:i+k-1]]
        other = [2*rh + r*r for (rh,r,h) in rhlista[0:i]+rhlista[i+k-1:n]]
#        print("rhsum",rhsum)
#        print("other",other)
        ans2.append(PI*(sum(rhsum) + max(other)))
#    print("ans2",ans2)
    max2 = max(ans2)
    print("Case #{}: {}".format(cas,max(max1,max2)))
