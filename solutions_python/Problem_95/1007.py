x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print 'Invalid Number'

gdic = {}

gdic['a']='y';
gdic['b']='h';
gdic['c']='e';
gdic['d']='s';
gdic['e']='o';
gdic['f']='c';
gdic['g']='v';
gdic['h']='x';
gdic['i']='d';
gdic['j']='u';
gdic['k']='i';
gdic['l']='g';
gdic['m']='l';
gdic['n']='b';
gdic['o']='k';
gdic['p']='r';
gdic['q']='z';
gdic['r']='t';
gdic['s']='n';
gdic['t']='w';
gdic['u']='j';
gdic['v']='p';
gdic['w']='f';
gdic['x']='m';
gdic['y']='a';
gdic['z']='q';
gdic[' ']=' ';	

for i in range(x):
	s = raw_input();
	trans_s ='Case #'+str(i+1)+': '
	for j in range(len(s)):
		trans_s = trans_s+gdic[s[j]]
	print trans_s