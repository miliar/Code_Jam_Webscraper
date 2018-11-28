pals = open('palsquares2.txt','r')
palins = map(int,pals.readlines())
pals.close()

fin = open('in.txt','r')
fout = open('out.txt','w')

n = int(fin.readline())
for i in range(n):
    a,b = map(int,fin.readline().split())
    c =0
    for pal in palins:
        if pal >= a and pal <= b:
            c+= 1
    fout.write('Case #%d: %d\n'%(i+1,c))

fin.close()
fout.close()
