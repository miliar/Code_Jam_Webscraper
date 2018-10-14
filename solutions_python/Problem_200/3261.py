def maketidy(line):
  found = None
  for i in range(len(line)):
    if found is not None: line[i] = '9'
    elif i<len(line)-1 and line[i] > line[i+1]:
      line[i] = chr(ord(line[i])-1)
      found = i
  if found is not None:
    found -= 1
    while found >= 0:
        if line[found] > line[found+1]:
            line[found] = chr(ord(line[found])-1)
            line[found+1] = '9'
            found -= 1
        else: break
  
t = int(input())
ret = []
for i in range(t):
  line = input()
  arr = list(line)
  maketidy(arr)
  ret.append(''.join(arr).lstrip('0'))

for i in range(len(ret)):
  print('Case #%d: %s'%(i+1,ret[i]))