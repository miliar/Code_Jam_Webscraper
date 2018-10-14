t = {}
t['a']='y'
t['b']='h'
t['c']='e'
t['d']='s'
t['e']='o'
t['f']='c'
t['g']='v'
t['h']='x'
t['i']='d'
t['j']='u'
t['k']='i'
t['l']='g'
t['m']='l'
t['n']='b'
t['o']='k'
t['p']='r'
t['q']='z'
t['r']='t'
t['s']='n'
t['t']='w'
t['u']='j'
t['v']='p'
t['w']='f'
t['x']='m'
t['y']='a'
t['z']='q'
t[' ']=' '

c = int(raw_input())
for case in range(1,c+1):
    s = raw_input()
    ans=" "
    for c in s:
        ans+=t[c]
    print "Case #"+str(case)+":"+ans
