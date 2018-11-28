t = int(raw_input())
for i in xrange(1, t+1):
  n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  length = 0
  count = 0
  l=list(n)
  while length < len(l):
    if l[length] == "-":
        if (length+int(m)-1) >= len(l):
            break
        j = 0
        while j < int(m) and length+j < len(l):
            if l[length+j]=="-":
                l[length+j]="+"
            else:
                l[length+j]="-"
            j+=1
        count+=1
    length+=1
  for j in range(len(l)):
    if l[j]=="-":
        count = "IMPOSSIBLE"
        break
  print "Case #{}: {}".format(i, count)
  # check out .format's specification for more formatting options