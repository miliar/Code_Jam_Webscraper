out1 = '''Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up'''

in1 = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

in1 = in1.replace(' ','')
in1 = in1.replace('\n','')

out2 = ''
for line in out1.split('\n'):
    out2+= line.split(': ')[1]
out1 = out2
out1 = out1.replace(' ','')
out1 = out1.replace('\n','')

lang = {}
for n in range(len(in1)):
	inkey = in1[n]
	if inkey not in lang:
		lang[inkey] = out1[n]

lang['z'] = 'q'
lang['q'] = 'z'
lang[' '] = ' '
T = 1
while T <= 30:
    in0 = input('Input\n')
    for line in in0.split('\n'):
        if line.replace(' ','').isalpha():
            out0 = ''.join(list(char.replace(char,lang[char])
                                for char in line))
            print('Case #{}: {}'.format(T,out0))
            T += 1
