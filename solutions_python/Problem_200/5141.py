def is_tidy(num):
    last = "0"
    for n in str(num):
        if n >= last:
            last = n
        else:
            return False
    return True

f = open("C:\Users\ondre\Downloads\\B-small-attempt0.in","r")
g = open("C:\Users\ondre\Downloads\\B-small-attempt0.out","w")
t = int(f.readline())
for i in xrange(1, t + 1):
  num = int(f.readline())
  while not is_tidy(num):
      num -= 1
  g.write("Case #{}: {}".format(i, str(num))+"\n")
f.close()
g.close()
