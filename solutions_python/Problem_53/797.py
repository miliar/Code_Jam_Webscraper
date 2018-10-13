def f(a,b): return b%(2**a)==(2**a-1)
input=file('A-large.in').read().split('\n')
output=file('A-large.out','wb+')
for l in range(1,int(input[0])+1):
 curr=input[l].split(' ')
 output.write('Case #'+str(l)+': '+['OFF','ON'][f(int(curr[0]),int(curr[1]))]+'\n')
output.close()