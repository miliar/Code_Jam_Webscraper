s = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
t = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"
s = "".join(s.split())
t = "".join(t.split())

p = {}
for i in range(len(s)):
    p[s[i]] = t[i]
p['y'], p['e'], p['q'] = 'a', 'o', 'z'

q = {}
for i in range(len(s)):
    q[t[i]] = s[i]
q['a'], q['o'], q['z'] = 'y', 'e', 'q'

for i in range(ord('a'), ord('z')+1):
    if not (chr(i) in p):
        c1 = chr(i)

for i in range(ord('a'), ord('z')+1):
    if not (chr(i) in q):
        c2 = chr(i)

p[c1] = c2

n = int(input())
a = [[i for i in input().strip()] for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if ord('a') <= ord(a[i][j]) <= ord('z'):
            a[i][j] = p[a[i][j]]
for i in range(len(a)):
    print ("Case #%d: "%(i+1) + "".join(a[i]))
