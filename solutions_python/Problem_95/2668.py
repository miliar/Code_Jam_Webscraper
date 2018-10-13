import sys;
d = dict()
s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
s2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
s3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

b1 = 'our language is impossible to understand'
b2 = 'there are twenty six factorial possibilities'
b3 = 'so it is okay if you want to just give up'

#c1 = 'y n f i c w l b k u o m x s e v z p d r j g a t h a q'
#a1 = 'a b c d e f g h i j k l m n o p q r s t u v w x y z

for i in range(len(s1)):
	d[s1[i]] = b1[i]

for i in range(len(s2)):
	d[s2[i]] = b2[i]

for i in range(len(s3)):
	d[s3[i]] = b3[i]
	
#Cases not accounted for above	
d['z'] = 'q'
d['q'] = 'z'
d['\n'] = ''
		
fIn = open(sys.argv[1])
fIn.readline()

fOut = open(sys.argv[2], 'w')
i = 1
for line in fIn:
	s = 'Case #'+str(i)+': '
	for char in line:
		s+=d[char]
	fOut.write(s+'\n')
	i+=1
	print(s)

fIn.close()
fOut.close()
print('DONE')
