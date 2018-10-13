# yay for one line solutions
(lambda f:f.write('\n'.join((lambda l: [l[i] and 'Case #{0}: {1}'.format(i+1,(lambda x,y: (y+1)%2**x==0)(*l[i]) and 'ON' or 'OFF') or '' for i in xrange(len(l))])([map(int,i.split()) for i in open('snapper.in').read().split('\n')[1:]]))) and f.close())(open('snapper.out','w'))
