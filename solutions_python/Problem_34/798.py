import re
linhas=open('A-large.in').readlines()
saida=open('A-large.out','w')
l,d,n=eval(','.join(linhas[0].split(' ')))
palavras=linhas[1:1+d]
padroes=linhas[1+d:]
for padrao in enumerate(padroes):
    padrao2=padrao[1].replace('(','[').replace(')',']')
    rexp=re.compile(padrao2)
    l=len(filter(None,[rexp.match(i) for i in palavras]))
    saida.write('Case #%d: %d\n' % (1+padrao[0],l))
