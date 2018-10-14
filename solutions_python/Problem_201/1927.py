t=int(input())
for q in range(0,t):
    lit=input().strip().split(" ")
    n=int(lit[0])
    k=int(lit[1])
    n=n+int(2)
    brr=[int(0)] * n
    brr[0]=1
    brr[n-1]=1
    for x in range(0,k):
      a=int(0)
      b=int(0)
      gaup=int(-1)
      for y in range(1,n):
        if brr[y]==1:
          tgaup=y-b
          a=b
          b=y
          if tgaup>gaup:
            gaup=tgaup
            a1=a
            b1=b
      mid=int((a1+b1)/2)
      brr[mid]=int(1)
    for i in range(mid-1,-1,-1):
      if brr[i]==1:
        break
    for j in range(mid+1,n):
      if brr[j]==1:
        break
    lt=mid-i-1
    rt=j-mid-1
    if lt>rt:
      print("Case #"+str(q+1)+": "+str(lt)+" "+str(rt))
    else:
      print("Case #"+str(q+1)+": "+str(rt)+" "+str(lt))