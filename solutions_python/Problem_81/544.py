def wp(a,i,l):
    j=0
    count=0
    k=0
    while j<l:
        if a[i][j]=='1':
           count+=1
        if a[i][j]!='.':
          k+=1
        j+=1
    p=float(count)
    q=float(k)
    return p/q 
def owp1(a,k,i,l): 
    j=0
    count=0
    count1=0
    while j<l:
        if a[k][j]=='1' and j!=i:
           count+=1
        if a[k][j]!='.' and j!=i:
           count1+=1 
        j+=1
    p=float(count)
    q=float(count1)
    return p/q 
def owp(a,i,l):
    j=0
    count=0
    sum=0
    while j<l:
       if j!=i and a[i][j]!='.':
         sum+=owp1(a,j,i,l)
         count+=1
       j+=1
    k=float(count)
    return sum/k
def oowp(a,i,l):
    j=0
    sum=0
    count=0
    while j<l:
        if j!=i:
          if a[i][j]!='.':
            count+=1
            sum+=owp(a,j,l)
        j+=1 
    k=float(count)
    return sum/k
t1=raw_input()
T=int(t1)
i=1
while i<=T:
      a=[]
      b=[]
      c=[]
      d=[]
      N1=raw_input()
      N=int(N1)
      for j in xrange(N):
          a.append([])
      j=0
      while j<N:
          str=raw_input()
          k=0
          while k<len(str):
               a[j].append(str[k])
               k+=1
          j+=1
      j=0
      l=len(str)
      while j<len(str):
            b.append(wp(a,j,l))
            c.append(owp(a,j,l))
            d.append(oowp(a,j,l))
            j+=1
      print "Case #%d:" %i
      j=0
      while j<l:
            print 0.25*b[j]+0.50*c[j]+0.25*d[j]
            j+=1
      i+=1       
