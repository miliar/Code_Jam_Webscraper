t = int(raw_input())
for i in xrange(1, t+1):
  innum = raw_input()
  num = list(innum)
  k = len(num)-1
  result = 0
  count = 0
  while count!=len(num)-1:
    count = 0
    k=len(num)-1
    while k>0:
        if int(num[k-1])>int(num[k]):
            if k==1:
                num[0]=str(int(num[k-1])-1)
                for j in range(1,len(num)):
                    num[j]="9"
                break
            else:
                num[k]="9"
                num[k-1]=str(int(num[k-1])-1)
        else:
            count+=1
        k-=1
    if num[0]=="0":
        for l in range(1,len(num)):
            num[l]="9"
        break
  if num[0]=="0":
    result = ''.join(num[1:])
  else:
    result = ''.join(num)
  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options