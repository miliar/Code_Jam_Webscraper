def solve(l):
 l.sort()
 t=0
 for n in l: t=t^n
 if t!=0: return 'NO'
 else: return str(sum(l[1:]))

input=file('C-large.in','rb+').read().split('\n')
output=file('C-large.out','wb+')
input.reverse()
for x in range(int(input.pop())):
 n=int(input.pop())
 m=[int(k) for k in input.pop().strip().split(' ')]
 output.write('Case #'+str(x+1)+': '+solve(m)+'\n')