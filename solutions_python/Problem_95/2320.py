import string

d = {'a':'y','o':'e','z':'q'}

inp = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv']

out = ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up']

for i in range(len(inp)):
    s = inp[i]
    t = out[i]
    for j in range(len(s)):
        if s[j] != ' ':
            d[s[j]] = t[j]

missing_in = string.letters[:26]
missing_out = string.letters[:26]
for key, val in d.iteritems():
    if key in missing_in:
        missing_in = ''.join(missing_in.split(key))
    if val in missing_out:
        missing_out = ''.join(missing_out.split(val))

d[missing_in] = missing_out

f = open('A-small-0.in','r')

n = int(f.readline())
out_s = ''
for case in range(n):
    out_s += 'Case #'+str(case+1)+': ' + ''.join([d[c] if c in d else ' ' for c in f.readline().strip()])+'\n'

f = open('A-small-0.out','w')
f.write(out_s)
