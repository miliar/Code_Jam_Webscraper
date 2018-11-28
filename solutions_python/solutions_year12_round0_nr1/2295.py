x= "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
y= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

import sets;
x2= ''.join( x.split() );
y2= ''.join( y.split() );
z= zip(x2,y2);
S= sorted(sets.Set(z));
#D= dict((S));
'''
'''

r= "abcdefghijklmnopqrstuvwxyz "
m= "abcdefghijklmnopzrstuvwxyq "
m= list(m); # ['?'] * len(r); # ?????????????????????????"

#print "|S|= %d"%len(S);
for sym in (S):
#	print sym[0], sym[1];
	i= r.index(sym[0]);
#	print i,m[i],sym[1]
	m[i]= sym[1] 
m= ''.join( m ); 
'''
for d,w in D.items():
	print d,w;
'''
#print x;

def translate(gs):
	g= list(gs);
	for j,c in enumerate(g):
		i= r.index(c)
#		print c , i, m[i]
		if(i!=None): g[j]= m[i];
	return ''.join(g);
'''
for i,c in enumerate(D):
	
	print i,c;
'''
'''
print r;
print m,''.join(sorted(m));
# ejp mysljylc kd kxveddknmc re jsicpdrysi
# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# de kr kd eoya kw aej tysr re ujdr lkgc jv


# our language is impossible to understand
# there are twenty six factorial possibilities
# so it is okay if you want to just give up

print "r= %s"%r;
print "m= %s"%m;

print "tr=",translate(' de kr kd eoya kw aej tysr re ujdr lkgc jv');

'''
raw= raw_input();
if raw.strip() == "": 
	print "N error.";
	exit()
N= int(raw);
u= 1;
while u<=N:
	raw= raw_input();
	t= translate(raw);
	print "Case #%d: %s"%(u,t);		
	u=u+1;
#
'''
'''
