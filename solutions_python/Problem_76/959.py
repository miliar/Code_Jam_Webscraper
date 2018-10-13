T = int(raw_input())
i = 0
def to_binary(x):
    bin = []
    i=0
    while i<30:
          bin.append(x%2)
          x=x/2
          i+=1
    return bin
def is_nonzero(a):
    for i in a:
        if i == 1:
           return 1
    return 0 
def bitwise_xor(a,b):
    return (a+b)%2
def xor(a,b):
    ans=[]
    j = 0
    for j in range(30):
           ans.append(bitwise_xor(a[j],b[j]))
    return ans

while i < T:
      #print i
      N = int(raw_input())
      inp = raw_input().split()
      count1 = 1
      sum = int(inp[0])
      min = int(inp[0])
      res = to_binary(int(inp[0]))
      while count1 < N:
            y = int(inp[count1])
            sum = sum + y
            if y < min:
               min = y
            temp = to_binary(int(inp[count1]))
            res = xor(res,temp)
            count1 = count1 + 1 
      i = i+1
      if is_nonzero(res) == 1:
         print "Case #%d: NO" %i
      else:
           fres = sum - min
           print "Case #%d: %d" %(i,fres)
      
