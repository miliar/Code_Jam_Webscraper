import sys
def findAllSibs(num,start,end):
  s = set()
  s.add(num)
  strNum = str(num)
  l =  len(str(num))
  for i in range(1,l):
    temp = strNum[l-i:]+strNum[0:l-i]
    tempNum = int(temp)
    if(strNum[0]!='0' and tempNum >= start and tempNum <= end):
      #print tempNum
      s.add(tempNum)
  return s

def solve(a,b):
  check = [-1 for i in range(0,b+1)]
  for i in range(a,b+1):
    if(check[i]!=-1):
      continue
    s = findAllSibs(i,a,b)
    check[i] = len(s)
#    print "the siblings of ",i,"is ",s
#    print "the len of siblings of ",i,"is ",check[i]
    for j in s:
      if(j!=i):
        check[j] = 1
  ans = 0
  for i in range(a,b+1):
    if(check[i]>1):
      #print "the check is ",check[i]
      #print "the check is ",check[i]
      ans = ans + (check[i]*(check[i]-1))/2
  return ans


def compute():
  n = int(raw_input())
  for i in range(0,n):
    a,b = (raw_input()).split(' ')
    a = int(a)
    b = int(b)
    ans = solve(a,b)
    print "Case #%d: %d"%(i+1,ans)


compute()
      





  

