fi = open("input.txt")

inp = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
out = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

alpha = [chr(ord('a')+i) for i in range(26)]


assert len(inp)==len(out)
f = {}
for i in range(len(inp)):
    if inp[i]==' ': continue
    f[inp[i]] = out[i]
f['q'] = 'z'
f['z'] = 'q'
f[' '] = ' '

nTest = int(fi.readline())
for test in range(nTest):
    line = list(fi.readline().strip())
    print "Case #"+str(test+1)+":","".join([f[c] for c in line])
    