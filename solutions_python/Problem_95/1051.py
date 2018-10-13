def writer(op, case, toprint):
    op.write('Case #'+str(case+1)+': '+str(toprint)+'\n')

mapping = 'yhesocvxduiglbkrztnwjpfmaq'
alphabets = 'ynficwlbkuomxsevqpdrjgthaz'
tt = ' '*97+mapping+' '*133
ip = open('A-small-attempt0.in');
op = open('A-out.out', 'w')
n = int(ip.readline())
for i in xrange(n):
    l = ip.readline().strip()
    writer(op, i, l.translate(tt))
ip.close()
op.close()
