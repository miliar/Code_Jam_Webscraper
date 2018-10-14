f = [
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
]

t = [
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
]

mp = {'y':'a','e':'o','q':'z'}
for i in range(3):
  for j in range(len(f[i])):
    try:
      if mp[f[i][j]] != t[i][j]:
        print ":("
        break
    except:
      mp[f[i][j]] = t[i][j]

def remove(s, c):
  i = s.find(c)
  if i < 0:
    return s
  return s[:i]+s[i+1:]

s1 = 'qwertyuioplkjhgfdsazxcvbnm'
s2 = 'qwertyuioplkjhgfdsazxcvbnm'
for k in mp.keys():
  s1 = remove(s1, mp[k])
  s2 = remove(s2, k)
try:
  if mp[s2] != s1:
     print ":("
except:
  mp[s2] = s1

t = int(raw_input())
for ti in range(1, t+1):
  sin = raw_input()
  sout = ""
  for c in sin:
    sout += mp[c]
  print "Case #%d: %s" % (ti, sout)

