##


# initialization 

sample_in = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
'''

sample_out = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
'''

m =dict()

for i in range(len(sample_in)):
	m[sample_in[i]]=sample_out[i]

# input file caching


with open('/Users/Jerrygao/Desktop/code_jam/small.in','r') as f:
	cin = f.read()

cin = cin.split('\n')

# core algorithm

# user huristics
sw = True
m['q'] = 'z' if sw else 'q'
m['z'] = 'q' if sw else 'z'

cout =['Output']

for i in range(1,len(cin)-1):
	out = ''.join([m[x] for x in cin[i]])
	cout.append('Case #%d: ' % i + out)

cout = '\n'.join(cout)

# output printing 

with open('/Users/Jerrygao/Desktop/code_jam/out.txt','w') as f:
	f.write(cout)


##


