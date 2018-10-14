#!/usr/bin/python
mp={}
mp={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

a=open("ggrese.txt",'r')
f=a.read()
f=f.split('\n')
g=['']*int(f[0])
c=0
#print g
for i in f[1:]:
    for j in i:
        if j!=' ':
            g[c]+=mp[j]
        else:
            g[c]+=' '
    c+=1
b=open("output.txt","w+")
c=1
for i in g:
    st="Case #"+str(c)+': '+i+"\n"
    b.write(st)
    c+=1

b.close()


