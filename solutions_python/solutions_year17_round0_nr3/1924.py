t=int(input())
for s in range(0,t):
    li=input().strip().split(" ")
    n=int(li[0])
    k=int(li[1])
    n=n+int(2)
    ar=[int(0)] * n
    ar[0]=1
    ar[n-1]=1
    for x in range(0,k):
      a=int(0)
      b=int(0)
      gap=int(-1)
      for y in range(1,n):
        if ar[y]==1:
          tgap=y-b
          a=b
          b=y
          if tgap>gap:
            gap=tgap
            a1=a
            b1=b
      mid=int((a1+b1)/2)
      ar[mid]=int(1)
    for i in range(mid-1,-1,-1):
      if ar[i]==1:
        break
    for j in range(mid+1,n):
      if ar[j]==1:
        break
    left=mid-i-1
    right=j-mid-1
    if left>right:
      print("Case #"+str(s+1)+": "+str(left)+" "+str(right))
    else:
      print("Case #"+str(s+1)+": "+str(right)+" "+str(left))