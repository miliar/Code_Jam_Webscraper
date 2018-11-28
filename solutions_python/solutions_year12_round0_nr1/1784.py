fin= open('Ain')
fout= open('Aout', 'w')
N=int(fin.readline())

#fstring= fin.read()
fsout=''

translate=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f', 'm','a','q']

for i in range(N):
    flout=fin.readline()
    fsout='Case #'+ str(i+1) +": "
    for i in flout:
        if i==' ':
            fsout+=' '
        elif i=='\n':
            fsout+='\n'
        else:
            fsout+= translate[ord(i)-97]
    fout.write(fsout)

fin.close()
fout.close()
    

