i=1
f=open("input")
l=f.readline()
while 1:
  l=f.readline()
  if l=='': break
  s=l.split(" ")
  n=int(s[0])
  k=int(s[1])
  ans1 = k % pow(2,n)
  if ans1==pow(2,n)-1:
    ans="ON"
  else:
    ans="OFF"

  print "Case #%i: %s" % (i,ans)
  i+=1
