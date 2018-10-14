f = open('B-large.in', 'r')
fout = open('B-large-out.txt', 'w')

ncases = f.readline()
cases = f.readlines()

for i in range(len(cases)):

  fout.write("Case #%d: " %(i+1))
  ans = list(cases[i].strip())

  for c in range(len(ans)-1, 0, -1):
    if (ans[c] < ans[c-1]):
      for ci in range(c, len(ans)):
        ans[ci] = '9'
      ans[c-1] = str(int(ans[c-1])-1)

  out = ''.join(ans)
  fout.write(str(int(out))+'\n')