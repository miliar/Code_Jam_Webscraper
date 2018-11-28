s = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
sa = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'

ans = {}
for i in range(len(s)):
  ans[s[i]] = sa[i];
S = set([])
for k in ans:
  S.add(k)
#for w in range(26):
#  if chr(w+97) not in S:
#    print chr(w+97)

# q and z not in input so they must map to each other
ans['q'] = 'z'
ans['z'] = 'q'

f = open('A-small-attempt0.in', 'r')
L = f.readlines()
tc = 0
for i in range(1, len(L)):
  s = L[i]
  S = ''
  for j in range(len(s)):
    if s[j] == '\n':
      continue
    S += ans[s[j]]
  tc += 1
  print('Case #',tc,': ',S,sep='')
