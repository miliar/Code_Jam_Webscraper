f = open("/storage/emulated/0/Download/B-large.in")
o = open("/storage/emulated/0/Download/B-large.out", "w")
t = int(f.readline().strip())

for case in range(t):
  n = f.readline().strip()
  
  for i in range(len(n) - 1, 0, -1):
    if int(n[i]) < int(n[i - 1]):
      n = n[:i - 1] + str(int(n[i - 1]) - 1) + ("9" * (len(n) - i))
  
  o.write("Case #{}: {}\n".format(case + 1, int(n)))

f.close()
o.close()