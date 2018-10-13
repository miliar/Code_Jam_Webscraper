import sys

test = lambda n, k : (k%(1<<n)==(1<<n)-1)

f = sys.argv[1]
fin = open(f)
fout = open(f.replace('in','out'), 'w')
T = int(fin.next())
i = 1
for l in fin:
	[n, k] = l.split(' ')
	fout.write("Case #%d: %s\n"%(i, 'ON' if test(int(n),int(k)) else 'OFF'))
	i += 1
fin.close()
fout.close()
