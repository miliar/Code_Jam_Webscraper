fout = open('abc.txt', 'w')
inp = 'yeq'
inp += 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
inp += 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
inp += 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
outp = 'aoz'
outp += 'our language is impossible to understand'
outp += 'there are twenty six factorial possibilities'
outp += 'so it is okay if you want to just give up'
d = {}
for i in range(len(inp)):
    d[inp[i]] = outp[i]
googlang = d.keys()
normlang = d.values()
abc = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for i in abc:
    if i not in normlang:
        lastnorm = i
    if i not in googlang:
        lastgoog = i
d[lastgoog] = lastnorm

fin = open('a-small.in','r')
T = int(fin.readline())
for i in range(T):
    inp = fin.readline();
    if inp[-1] == '\n':
        inp = inp[:-1]
    fout.write('Case #' + str(i+1) + ': ')
    for j in inp:
        fout.write(d[j])
    fout.write('\n')
fin.close()
fout.close()
        
