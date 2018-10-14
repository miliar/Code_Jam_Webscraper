t=int(input())
for s in range(0,t):
    listt=input().strip().split(" ")
    n=int(listt[0])
    k=int(listt[1])
    n=n+int(2)
    myarray=[int(0)] * n
    myarray[0]=1
    myarray[n-1]=1
    for x in range(0,k):
      a=int(0)
      b=int(0)
      gap=int(-1)
      for y in range(1,n):
        if myarray[y]==1:
          tgap=y-b
          a=b
          b=y
          if tgap>gap:
            gap=tgap
            a1=a
            b1=b
      mid=int((a1+b1)/2)
      myarray[mid]=int(1)
    for i in range(mid-1,-1,-1):
      if myarray[i]==1:
        break
    for j in range(mid+1,n):
      if myarray[j]==1:
        break
    left=mid-i-1
    right=j-mid-1
    if left>right:
      print("Case #"+str(s+1)+": "+str(left)+" "+str(right))
    else:
      print("Case #"+str(s+1)+": "+str(right)+" "+str(left))