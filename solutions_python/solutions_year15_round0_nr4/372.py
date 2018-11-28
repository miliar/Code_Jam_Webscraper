f = open('D-small-attempt0.in')
o = open('output.txt', 'w')
n = int(f.readline())
for i in range(n):
  x,r,c = [int(x) for x in f.readline().strip().split(" ")]
  if (r*c)%x != 0 or max(r,c) < x or min(r,c) < (x+1)/2 or x >= 7:
    ans = "RICHARD"
  elif x == 2 or x == 3:
    ans = "GABRIEL"
  elif min(r,c) == 2 and x%2 == 0:
    ans = "RICHARD"
  elif min(r,c) == 2 and x%2==1 and max(r,c) == x:
    ans = "RICHARD"
  else:
    ans = "GABRIEL"
  o.write("Case #"+str(i+1)+": "+ans+"\n")
f.close()
o.close()