f = open('input.txt','r')
g = open('output.txt','w')

ntest = int(f.readline())

l=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']

for i in range(ntest):
        s=list(f.readline())
        for j in range(len(s)-1):
                if s[j]!=' ':
                        s[j]=l[ord(s[j])-97]
        s=''.join(s)
        g.write((''.join(['Case #',str(i+1),': ',s])))
f.close()
g.close()
