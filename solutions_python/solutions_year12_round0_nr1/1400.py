s1='abcdefghijklmnopqrstuvwxyz'
s2='ynficwlbkuomxsevzpdrjgthaq'
f=open('1a_small.txt')
f2=open('1a_small_out.txt','w')
f.readline()
for n,line in enumerate(f):
    f2.write('Case #'+str(n+1)+': ')
    s3=''
    for c in line.strip('\n'):
        if c==' ':
            s3+=' '
        else:
            s3+=s1[s2.find(c)]
    f2.write(s3+'\n')
f.close()
f2.close()
